import hashlib
import json
from dataclasses import dataclass
from decimal import ROUND_CEILING, Decimal
from enum import StrEnum
from typing import Any

CENT = Decimal("0.01")
ONE = Decimal("1")

@dataclass(frozen=True)
class Config:
    min_legs: int = 3
    max_legs: int = 8
    quantity: int = 10
    gross_candidate_per_unit: Decimal = Decimal("0.02")
    slippage_per_unit: Decimal = Decimal("0.01")
    non_atomic_per_unit: Decimal = Decimal("0.02")
    fee_coefficient: Decimal = Decimal("0.07")
E001 = Config()

class Side(StrEnum):
    YES = "yes"
    NO = "no"

class Direction(StrEnum):
    ALL_YES = "all_yes"
    ALL_NO = "all_no"

class SemanticsError(ValueError):
    pass

class InsufficientDepth(ValueError):
    pass

@dataclass(frozen=True)
class Level:
    price: Decimal
    quantity: int

@dataclass(frozen=True)
class Book:
    yes_bids: tuple[Level, ...]
    no_bids: tuple[Level, ...]

def eligible_series(series: dict[str, Any]) -> bool:
    return (
        "Climate and Weather" in set(series.get("categories") or [])
        and "Daily temperature" in set(series.get("tags") or [])
        and "GLOBALTEMPERATURE" in str(series.get("contract_terms_url") or "").upper()
        and series.get("fee_type") == "quadratic"
        and Decimal(str(series.get("fee_multiplier", 0))) == Decimal("1")
    )

def _integer(value: Any, name: str) -> int:
    if value is None:
        raise SemanticsError(f"missing {name}")
    d = Decimal(str(value))
    if d != d.to_integral_value():
        raise SemanticsError(f"{name} is not integer-valued")
    return int(d)

def _interval(m: dict[str, Any]) -> tuple[int | None, int | None]:
    kind = str(m.get("strike_type") or "").lower()
    if kind == "less":
        return None, _integer(m.get("cap_strike"), "cap_strike") - 1
    if kind == "greater":
        return _integer(m.get("floor_strike"), "floor_strike") + 1, None
    if kind == "between":
        lo = _integer(m.get("floor_strike"), "floor_strike")
        hi = _integer(m.get("cap_strike"), "cap_strike")
        if hi < lo:
            raise SemanticsError("inverted between range")
        return lo, hi
    raise SemanticsError("unsupported strike type")

def validate_partition(event: dict[str, Any], markets: list[dict[str, Any]]) -> dict[str, Any]:
    if not event.get("mutually_exclusive"):
        raise SemanticsError("event not explicitly mutually exclusive")
    if not event.get("settlement_sources"):
        raise SemanticsError("settlement source unresolved")
    if not E001.min_legs <= len(markets) <= E001.max_legs:
        raise SemanticsError("leg count outside frozen bounds")
    if any(m.get("status") not in {"active", "open"} for m in markets):
        raise SemanticsError("all legs must be active/open")
    if any(m.get("price_level_structure") != "linear_cent" for m in markets):
        raise SemanticsError("non linear-cent pricing")
    event_ticker = str(event.get("event_ticker") or event.get("ticker") or "")
    if not event_ticker or any(m.get("event_ticker") != event_ticker for m in markets):
        raise SemanticsError("event identity mismatch")

    common_fields = (
        "series_ticker", "close_time", "expiration_time", "expected_expiration_time",
        "latest_expiration_time", "occurrence_datetime", "early_close_condition", "rules_secondary"
    )
    for field in common_fields:
        vals = {str(m.get(field) or "") for m in markets}
        if len(vals) != 1 or "" in vals:
            raise SemanticsError(f"unresolved/inconsistent {field}")

    pairs = [(_interval(m), m) for m in markets]
    low = [x for x in pairs if x[0][0] is None]
    high = [x for x in pairs if x[0][1] is None]
    mid = [x for x in pairs if x[0][0] is not None and x[0][1] is not None]
    if len(low) != 1 or len(high) != 1:
        raise SemanticsError("need exactly one lower and upper tail")
    ordered = low + sorted(mid, key=lambda x: x[0][0]) + high
    for left, right in zip(ordered, ordered[1:], strict=False):
        if left[0][1] is None or right[0][0] is None or right[0][0] != left[0][1] + 1:
            raise SemanticsError("gap or overlap")

    canonical = {
        "event": event_ticker,
        "settlement_sources": event["settlement_sources"],
        "markets": [{
            "ticker": m.get("ticker"),
            "strike_type": m.get("strike_type"),
            "floor": m.get("floor_strike"),
            "cap": m.get("cap_strike"),
            "rules_primary": m.get("rules_primary"),
            "rules_secondary": m.get("rules_secondary"),
            "occurrence": m.get("occurrence_datetime"),
            "close": m.get("close_time"),
            "expiration": m.get("expiration_time"),
            "latest_expiration": m.get("latest_expiration_time"),
            "early_close": m.get("early_close_condition"),
        } for _, m in ordered],
    }
    fingerprint = hashlib.sha256(json.dumps(canonical, sort_keys=True).encode()).hexdigest()
    return {
        "event_ticker": event_ticker,
        "series_ticker": markets[0]["series_ticker"],
        "market_tickers": tuple(m["ticker"] for _, m in ordered),
        "fingerprint": fingerprint,
    }

def parse_book(payload: dict[str, Any]) -> Book:
    raw = payload.get("orderbook_fp") or payload.get("orderbook") or payload

    def parse(key: str) -> tuple[Level, ...]:
        out = []
        rows = raw.get(f"{key}_dollars") or raw.get(key) or []
        for row in rows:
            if isinstance(row, dict):
                p = row.get("price_dollars", row.get("price"))
                q = row.get("quantity", row.get("quantity_fp", row.get("qty", 0)))
            else:
                p, q = row[0], row[1]
                if isinstance(p, int):
                    p = Decimal(p) / 100
            out.append(Level(Decimal(str(p)), int(Decimal(str(q)))))
        return tuple(out)
    return Book(parse("yes"), parse("no"))

def asks(book: Book, side: Side) -> tuple[Level, ...]:
    opposite = book.no_bids if side == Side.YES else book.yes_bids
    return tuple(\n        sorted(\n            (Level(ONE - x.price, x.quantity) for x in opposite),\n            key=lambda x: x.price,\n        )\n    )

def walk(book: Book, side: Side, quantity: int) -> tuple[Decimal, Decimal, int]:
    levels = asks(book, side)
    available = sum(x.quantity for x in levels)
    if available < quantity:
        raise InsufficientDepth(f"need {quantity}, have {available}")
    remaining, cost, worst = quantity, Decimal("0"), Decimal("0")
    for level in levels:
        take = min(remaining, level.quantity)
        cost += level.price * take
        if take:
            worst = level.price
        remaining -= take
        if remaining == 0:
            break
    return cost, worst, available

def fee(contracts: int, price: Decimal) -> Decimal:
    raw = E001.fee_coefficient * contracts * price * (ONE - price)
    return raw.quantize(CENT, rounding=ROUND_CEILING)

def price_basket(\n    books: dict[str, Book], direction: Direction, quantity: int = 10\n) -> dict[str, Any]:
    side = Side.YES if direction == Direction.ALL_YES else Side.NO
    legs = []
    for ticker, book in books.items():
        cost, worst, available = walk(book, side, quantity)
        f = fee(quantity, cost / quantity)
        legs.append({"ticker": ticker, "cost": cost, "fee": f, "worst": worst, "depth": available})
    acquisition = sum((x["cost"] for x in legs), Decimal("0"))
    fees = sum((x["fee"] for x in legs), Decimal("0"))
    n = len(legs)
    guaranteed = Decimal(quantity if direction == Direction.ALL_YES else (n - 1) * quantity)
    gross = guaranteed - acquisition
    slippage = E001.slippage_per_unit * quantity
    non_atomic = E001.non_atomic_per_unit * quantity
    total = acquisition + fees
    max_pre_final = Decimal("0")
    worst_fail_loss = Decimal("0")
    for omitted in legs:
        committed = total - omitted["cost"] - omitted["fee"]
        max_pre_final = max(max_pre_final, committed)
        partial_floor = (\n            Decimal("0")\n            if direction == Direction.ALL_YES\n            else Decimal(max(n - 2, 0) * quantity)\n        )
        worst_fail_loss = max(worst_fail_loss, max(committed - partial_floor, Decimal("0")))
    return {
        "direction": direction.value, "quantity": quantity, "legs": legs,
        "guaranteed_payoff": guaranteed, "acquisition_cost": acquisition, "fees": fees,
        "slippage_reserve": slippage, "non_atomic_buffer": non_atomic,
        "gross_edge": gross, "net_modeled_edge": gross - fees - slippage - non_atomic,
        "weakest_depth": min(x["depth"] for x in legs),
        "max_pre_final_leg_capital": max_pre_final,
        "worst_case_final_leg_failure_loss": worst_fail_loss,
    }
