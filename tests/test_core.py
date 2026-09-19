from decimal import Decimal
import pytest
from pmarb.core import (
    Book, Direction, InsufficientDepth, Level, SemanticsError, Side,
    asks, fee, price_basket, validate_partition, walk,
)

def market(ticker, kind, floor=None, cap=None):
    return {
        "ticker": ticker, "event_ticker": "EVT", "series_ticker": "SER",
        "strike_type": kind, "floor_strike": floor, "cap_strike": cap,
        "rules_primary": ticker, "rules_secondary": "same exceptional rules",
        "close_time": "2026-09-20T05:00:00Z",
        "expiration_time": "2026-09-26T14:00:00Z",
        "expected_expiration_time": "2026-09-20T19:00:00Z",
        "latest_expiration_time": "2026-09-26T14:00:00Z",
        "occurrence_datetime": "2026-09-20T14:00:00Z",
        "early_close_condition": "same close condition",
        "price_level_structure": "linear_cent", "status": "active",
    }

def event(mx=True):
    return {"event_ticker": "EVT", "mutually_exclusive": mx, "settlement_sources": [{"name": "source"}]}

def test_valid_partition():
    rel = validate_partition(event(), [
        market("LOW", "less", cap=71),
        market("MID1", "between", floor=71, cap=72),
        market("MID2", "between", floor=73, cap=74),
        market("HIGH", "greater", floor=74),
    ])
    assert rel["market_tickers"] == ("LOW", "MID1", "MID2", "HIGH")
    assert len(rel["fingerprint"]) == 64

def test_reject_gap():
    with pytest.raises(SemanticsError, match="gap or overlap"):
        validate_partition(event(), [
            market("LOW", "less", cap=71),
            market("MID", "between", floor=72, cap=73),
            market("HIGH", "greater", floor=73),
        ])

def test_reject_nonexclusive():
    with pytest.raises(SemanticsError):
        validate_partition(event(False), [
            market("LOW", "less", cap=71),
            market("MID", "between", floor=71, cap=72),
            market("HIGH", "greater", floor=72),
        ])

def book(yes_bid="0.40", no_bid="0.55", qty=100):
    return Book((Level(Decimal(yes_bid), qty),), (Level(Decimal(no_bid), qty),))

def test_opposite_bid_ask():
    assert asks(book(), Side.YES)[0].price == Decimal("0.45")
    assert asks(book(), Side.NO)[0].price == Decimal("0.60")

def test_no_depth_extrapolation():
    with pytest.raises(InsufficientDepth):
        walk(book(qty=4), Side.YES, 5)

def test_fee_rounds_up():
    assert fee(1, Decimal("0.50")) == Decimal("0.02")

def test_basket_math():
    books = {k: book("0.68", "0.70") for k in ("A", "B", "C")}
    r = price_basket(books, Direction.ALL_YES, 10)
    assert r["guaranteed_payoff"] == Decimal("10")
    assert r["acquisition_cost"] == Decimal("9.00")
    assert r["gross_edge"] == Decimal("1.00")
    assert r["slippage_reserve"] == Decimal("0.10")
    assert r["non_atomic_buffer"] == Decimal("0.20")
