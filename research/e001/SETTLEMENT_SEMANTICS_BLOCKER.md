# E001 Settlement Semantics Blocker

Date checked: 2026-09-19
Experiment: E001 — Prospective Structural Mispricing Census
Decision: STOP / REJECT — BLOCKED / SEMANTICALLY UNPROVABLE

## Question

Can the selected Kalshi daily-temperature family be proven, from current authoritative rules, to resolve on a final settlement value whose granularity, endpoint semantics, and exceptional-resolution behavior make the displayed buckets a true exhaustive partition with a fixed basket payoff?

## Answer

No.

The proof fails on two independent grounds.

## 1. Final settlement lattice is not proven

Current Kalshi series metadata for KXHIGHNY identifies:
- category: Climate and Weather
- tag: Daily temperature
- contract family: GLOBALTEMPERATURE
- settlement source: The Weather Company
- settlement URL: https://weather.com/kalshi

Located current market-rule text defines contracts using Fahrenheit comparisons such as strict less-than / greater-than and named two-degree ranges. Kalshi also warns that preliminary Weather Company readings can differ from the final reported value due to rounding and conversion.

No located current venue-authoritative rule specifies the exact numerical transformation that creates the final settlement value used by this family. In particular, the proof does not establish whether the final value is always an integer Fahrenheit degree, how any decimal source value is rounded or transformed, or whether range wording closes every possible decimal interval.

The Weather Company public APIs cannot substitute for this missing contract rule. Their documentation supports optional decimal precision in weather values, which demonstrates why integer settlement cannot be inferred from labels or examples.

Therefore superficially adjacent labels do not prove collective exhaustiveness.

## 2. Exceptional no-data resolution breaks the fixed-payoff proof

The current Kalshi series metadata states:

- a material error in the initial non-preliminary publication can delay expiration until a non-materially-erroneous revision or the expiration date; and
- if no data is available at the end of that period, all markets resolve to the last fair price determined by Kalshi.

E001 requires the completed ALL-YES basket to have a guaranteed $1 payoff per one-contract exhaustive basket, and ALL-NO to have a guaranteed $(n-1) payoff.

No located authoritative rule proves that the last-fair-price fallback across all legs is constrained to preserve those basket payoffs. It therefore creates an additional contractual state that is outside the proven binary partition model.

## Exact findings by required field

1. Settlement measurement: maximum/minimum temperature for the named location/date, as reported by The Weather Company.
2. Integer/decimal transformation: NOT PROVEN.
3. Exact rounding rule: NOT PROVEN.
4. Unit: Fahrenheit for the selected U.S. daily-temperature rule family.
5. Station/location: market-specific named location/source identifier; for NYC current rule copies identify CLINYC.
6. Observation/time period: market-specific date/day; exact feed methodology was not sufficiently documented for the proof.
7. Endpoints: lower/upper variants use strict comparisons; middle variants use named ranges. Decimal-boundary behavior is NOT PROVEN.
8. Every possible settlement value in exactly one bucket: NOT PROVEN.
9. Numeric gaps: cannot be ruled out without the settlement lattice.
10. Numeric overlaps: cannot be ruled out without the settlement lattice/endpoint transformation.
11. Exceptional state: YES — material-error delay and no-data last-fair-price fallback.
12. Guaranteed-payoff effect: NOT PROVEN under the fallback; therefore E001 fails closed.
13. Same current family: YES — KXHIGHNY / GLOBALTEMPERATURE live series metadata checked on 2026-09-19.

## Authoritative sources

- Kalshi live series API:
  https://external-api.kalshi.com/trade-api/v2/series/KXHIGHNY
- Kalshi Weather Markets:
  https://help.kalshi.com/en/articles/13823837-weather-markets
- Kalshi / The Weather Company partnership:
  https://news.kalshi.com/p/kalshi-weather-company-partnership
- The Weather Company API documentation:
  https://developer.weather.com/docs/openapi/pws-daily-summary-7-day-2-0/get-v2-pws-dailysummary-7day

Supporting non-authoritative copies of individual market rules were reviewed only to understand wording patterns; they were not accepted as sufficient proof.

## Experimental consequence

- No SETTLEMENT_SEMANTICS_PROOF.md is created because the proof did not succeed.
- No Stage 2 collector is built.
- No scheduler or persistence architecture is activated for E001.
- No official E001 start timestamp exists.
- No evidence observation exists.
- No performance/economic threshold was changed.
- A new category or relationship design requires a separate preregistered decision before evidence is viewed.
