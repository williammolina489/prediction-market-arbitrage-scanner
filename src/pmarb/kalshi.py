import time
from typing import Any

import httpx

BASE = "https://external-api.kalshi.com/trade-api/v2"


class Client:
    """Public GET-only client. Trading methods intentionally do not exist."""
    def __init__(self, base_url: str = BASE) -> None:
        self.base_url = base_url.rstrip("/")
        self.http = httpx.Client(timeout=20.0, headers={"User-Agent": "pmarb-e001/0.1"})

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        for attempt in range(3):
            r = self.http.get(self.base_url + path, params=params)
            if r.status_code != 429:
                r.raise_for_status()
                return r.json()
            if attempt == 2:
                r.raise_for_status()
            time.sleep(2 ** attempt)
        raise RuntimeError("unreachable")

    def series(self, ticker: str) -> dict[str, Any]:
        return self.get(f"/series/{ticker}").get("series", {})

    def series_list(self, category: str) -> list[dict[str, Any]]:
        return self.get("/series", {"category": category}).get("series", [])

    def events(self, series_ticker: str) -> list[dict[str, Any]]:
        return self.get("/events", {
            "series_ticker": series_ticker, "status": "open", "with_nested_markets": "true"
        }).get("events", [])

    def markets(self, event_ticker: str) -> list[dict[str, Any]]:
        data = self.get("/markets", {"event_ticker": event_ticker, "status": "open"})
        return data.get("markets", [])

    def orderbook(self, ticker: str) -> dict[str, Any]:
        return self.get(f"/markets/{ticker}/orderbook", {"depth": 100})
