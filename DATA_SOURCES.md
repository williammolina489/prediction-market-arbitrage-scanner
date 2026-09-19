# Data Sources and Venue Decision — 2026-09-19

## Selected venue: Kalshi
Current first-party material exposes public REST market data without authentication; structured series, event, and market metadata; rules and settlement sources; order books and trades; WebSocket market-data channels; demo and production environments; and fee metadata. Live daily-temperature markets expose structured strike types and floor/cap strikes suitable for deterministic partition validation.

E001 uses production public REST only. WebSocket and authenticated/batch endpoints are unnecessary for the foundation.

## Deferred venues
Polymarket US / QCX is a regulated U.S. venue with current public market/event/series API surfaces and authenticated order-book streaming/trading interfaces, but adding a second venue would add semantic/operational complexity before single-venue logic is proven.

ForecastEx is also regulated and exposes event-contract metadata through broker/API infrastructure, but its workflow is more broker/authentication-centric than the selected public Kalshi path.

## E001 category
Standardized daily-temperature markets in the GLOBALTEMPERATURE contract family, with Climate and Weather category, Daily temperature tag, quadratic fee type, and multiplier 1.

Only observations collected after the preregistration commit may be used for E001 profitability. Foundation-time live inspection validates schema/API feasibility only.

## Current weather-source conflict and fail-closed treatment

A July 22, 2026 Kalshi Help Center article still describes daily-temperature settlement as using the NWS final climate report, while current Kalshi market notices and live series/event metadata show a transition to The Weather Company for current daily-temperature contracts. E001 therefore never hardcodes a settlement source from category-level help text. The current series/event/market metadata and full market rules must agree for each relationship; otherwise the event is rejected.

A second unresolved foundation item is settlement-value granularity. Current market labels form apparently exhaustive two-degree ranges plus lower/upper tails, but E001 will not infer the underlying value lattice from labels alone. See research/e001/AMENDMENT_001.md.


## AMENDMENT_001 final research finding — 2026-09-19

Authoritative/current sources checked:
- Kalshi live series API for KXHIGHNY:
  https://external-api.kalshi.com/trade-api/v2/series/KXHIGHNY
- Kalshi Weather Markets help:
  https://help.kalshi.com/en/articles/13823837-weather-markets
- Kalshi / The Weather Company partnership announcement:
  https://news.kalshi.com/p/kalshi-weather-company-partnership
- The Weather Company API documentation, including explicit optional decimal precision:
  https://developer.weather.com/docs/openapi/pws-daily-summary-7-day-2-0/get-v2-pws-dailysummary-7day

What is established:
- The current KXHIGHNY series is Daily temperature / Climate and Weather.
- The live series metadata names The Weather Company (weather.com/kalshi) as the settlement source.
- The unit in the market rule family is Fahrenheit.
- Current market-rule wording uses strict lower/upper comparisons and range wording for middle buckets.
- Kalshi warns that preliminary Weather Company values may differ from the final reported value due to rounding/conversion.
- Kalshi series metadata states that a material error can delay expiration and that, if no data is available by the end of the period, all markets resolve to a last fair price determined by Kalshi.

What is NOT established to E001's required standard:
- The exact final-value numeric lattice used by weather.com/kalshi for this contract family.
- The exact transformation/rounding rule from underlying observation(s) to the final settlement number.
- A first-party rule proving that every possible final settlement value belongs to exactly one displayed bucket.
- A first-party invariant proving that the no-data last-fair-price fallback preserves the fixed ALL-YES or ALL-NO basket payoff.

The Weather Company public API documentation is not treated as proof of the Kalshi settlement feed's value lattice. Its decimal-precision option is used only to demonstrate why integer settlement cannot be inferred from generic TWC display examples.

Conclusion: AMENDMENT_001 FAILS CLOSED. E001 may not proceed to Stage 2.
