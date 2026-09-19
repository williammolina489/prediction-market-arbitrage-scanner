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


## E003 BTC nested-threshold research — 2026-09-19

### Candidate family

Current Kalshi series API:
- Series ticker: KXBTCD
- Title: Bitcoin price Above/below
- Category: Crypto
- Frequency: hourly
- Tags: Hourly, BTC
- Contract terms: https://assets.kalshi.com/contract_terms/BTC.pdf
- Fee type: quadratic
- Fee multiplier: 1
- Settlement source: CF Benchmarks
- Settlement-source index: CF Bitcoin Real-Time Index (BRTI)
- Series metadata states that 60 RTI prices are collected during the last minute before expiration and the official/final value is their average.

Kalshi's current Crypto Markets help independently states that crypto event contracts use 60 one-second CF Benchmarks RTI readings during the relevant expiration minute and average those readings.

### BTC contract terms

The current BTC contract terms define the Underlying as the USD spot price of one Bitcoin at the specified time according to a simple average of BRTI for the prior 60 seconds. Revisions after Expiration are ignored.

The terms support recurring iterations, price levels in $0.01 increments over the stated range, above/below/between payout criteria, a $0.01 contract tick, a $1.00 Settlement Value, and market-specific date/time placeholders.

If no data is available on the Expiration Date at the Expiration Time, the market resolves No. That specific no-data rule alone would preserve the proposed pair's $1 floor because both threshold markets resolving No makes YES(lower)=0 and NO(higher)=1.

However, the same BTC terms also state that, before settlement, Kalshi may at its sole discretion initiate Market Outcome Review under Rule 6.3(c).

### Rulebook exceptional settlement

Current Kalshi Rulebook v1.24 Rule 6.3(c) permits non-binary proportional payout when Kalshi cannot determine whether an Expiration Value falls within the Payout Criterion (or what payout proportion applies). It permits:
- use of the Contract's last traded price as the payout; or
- if that price is unavailable or deemed unfair, a binding fair allocation determined by the Outcome Review Committee.

The current materials located do not impose a cross-strike monotonicity invariant on these exceptional payout values.

For the proposed lower-YES / higher-NO pair, let p_L be the exceptional YES payout on the lower strike and p_H the exceptional YES payout on the higher strike. Total pair payout is:

    p_L + (1 - p_H) = 1 + p_L - p_H

The preregistered-style guarantee would require p_L >= p_H for every permitted exceptional resolution. That is not established. Therefore a minimum $1 payout cannot be proven across the complete permitted settlement state space.

### Market/API mechanics noted before stop

- Current KXBTCD pages show many simultaneous ordered threshold strikes within an hourly event.
- BTC contract terms specify $0.01 minimum tick.
- Current API orderbook documentation returns YES and NO bids; an ask on one side is the $1 complement of an opposite-side bid with the same quantity.
- Current orderbook documentation examples include API authentication headers. No credentials were added because E003 failed its contractual proof first.
- Current API rate-limit documentation uses separate Read/Write token budgets for authenticated requests; Basic event-contract tier lists a 200 token/second Read budget and 100 token/second Write budget, with most requests defaulting to 10 tokens unless an endpoint-specific cost applies.

No opportunity prices, historical returns, or pair profitability were evaluated.
