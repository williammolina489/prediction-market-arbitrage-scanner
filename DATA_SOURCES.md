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
