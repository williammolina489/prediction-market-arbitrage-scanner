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
