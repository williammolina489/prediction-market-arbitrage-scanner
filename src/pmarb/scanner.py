from decimal import Decimal
from typing import Any

from .core import (
    Direction,
    InsufficientDepth,
    eligible_series,
    parse_book,
    price_basket,
    validate_partition,
)
from .kalshi import Client


def discover(client: Client) -> list[dict[str, Any]]:
    out = []
    for stub in client.series_list("Climate and Weather"):
        ticker = str(stub.get("ticker") or "")
        if not ticker:
            continue
        series = client.series(ticker)
        if not eligible_series(series):
            continue
        for event in client.events(ticker):
            event_ticker = str(event.get("event_ticker") or event.get("ticker") or "")
            markets = event.get("markets") or client.markets(event_ticker)
            try:
                out.append(validate_partition(event, markets))
            except ValueError:
                continue
    return out


def scan_once(client: Client | None = None) -> list[dict[str, Any]]:
    raise RuntimeError(
        "E001 is PREREGISTERED, not RUNNING. "
        "Resolve AMENDMENT_001 settlement-granularity proof and persistence first."
    )

    client = client or Client()  # pragma: no cover
    observations = []
    for rel in discover(client):
        books = {t: parse_book(client.orderbook(t)) for t in rel["market_tickers"]}
        for direction in (Direction.ALL_YES, Direction.ALL_NO):
            try:
                result = price_basket(books, direction)
            except InsufficientDepth:
                continue
            result.update({
                "event_ticker": rel["event_ticker"],
                "series_ticker": rel["series_ticker"],
                "semantics_fingerprint": rel["fingerprint"],
                "gross_candidate": result["gross_edge"] / result["quantity"] >= Decimal("0.02"),
                "after_cost_executable": result["net_modeled_edge"] > 0,
            })
            observations.append(result)
    return observations
