# E001 — Prospective Structural Mispricing Census

Status: PREREGISTERED
Date: 2026-09-19

## Hypothesis
Structurally valid prediction-market pricing inconsistencies occur prospectively with sufficient frequency, executable depth, and after-cost margin to justify development of a separate paper-execution experiment.

This is not a claim that prediction-market arbitrage is profitable.

## Frozen scope
- Venue: Kalshi only.
- Category: standardized daily-temperature bucket events in GLOBALTEMPERATURE.
- Relationship: PARTITION / MUTUALLY_EXCLUSIVE_EXHAUSTIVE only.
- Multivariate/combination events: excluded.
- Cross-venue, fuzzy duplicates, and semantic implication chains: excluded.
- Common quantity: 10 contracts per leg.
- Observation cadence: 60 seconds.
- Leg count: 3 through 8.

## Frozen semantics gate
Eligible only when the event is explicitly mutually exclusive; settlement source is resolved; all legs share event/series, occurrence, close, expected/latest expiration, early-close and exceptional-resolution semantics; pricing is linear-cent; there is exactly one lower and one upper tail; intermediate structured strike ranges are integer-valued, contiguous, non-overlapping and collectively exhaustive. Otherwise fail closed.

## Frozen executable pricing
Evaluate long-only ALL_YES and ALL_NO baskets. ALL_YES guaranteed payoff is $1 per one-contract exhaustive basket. ALL_NO guaranteed payoff is $(n-1) per one-contract basket for n exhaustive legs.

Executable YES asks come from 1 - NO bids. Executable NO asks come from 1 - YES bids. Walk depth for the full common quantity. Never use midpoint, last trade, or extrapolated top-of-book.

Record all eligible observations. Label a gross discrepancy candidate only at at least $0.02 gross edge per one-contract basket.

## Frozen costs
For quadratic fee type, multiplier 1:
fee = ceil_to_cent(0.07 * contracts * price * (1-price))

Per 10-contract basket reserves:
- slippage: $0.10 total
- non-atomic execution risk: $0.20 total

If live fee metadata conflicts, reject rather than substitute a cheaper model.

net modeled edge = guaranteed payoff - executable acquisition cost - fees - slippage reserve - non-atomic buffer

## Frozen non-atomic fields
Record leg count, weakest executable depth, maximum capital committed before a hypothetical final leg, conservative worst-case loss if one final leg disappears, and observation timestamp. Never assume simultaneous fills.

## Persistence / duplicates
Identity: venue + relationship + sorted market IDs + direction.
Persistent means three consecutive scheduled positive after-cost observations spanning at least 120 seconds. Consecutive observations of one identity are a single episode. The episode ends when a scheduled observation is no longer executable after costs.

## Evidence window
30 calendar days and at least 20 eligible-event days. If 30 days is insufficient, continue to the 20th eligible-event day, hard cap 45 calendar days.

## False-positive audit
Audit every after-cost episode plus a reproducible random sample of 50 non-opportunity validated relationship instances, or all if fewer.

## Promotion — all required
1. At least 20 unique executable after-cost episodes.
2. At least 10 persistent episodes.
3. Qualifying episodes on at least 10 distinct event-days.
4. Median net modeled edge at least $0.10 per 10-contract basket.
5. Median weakest-leg executable depth at least 20 contracts.
6. Audited semantic false-positive rate at most 1%.
7. No single series contributes more than 50% of qualifying episodes.
8. At least 90% of qualifying episodes have final-leg-failure loss no greater than 10x that episode's maximum net modeled edge.
9. Reproducible from preserved raw data and the pinned code commit.

## Rejection
If any promotion gate fails at the end of the frozen window, mark E001 STOP / REJECT. Do not rescue it by changing quantity, thresholds, cost assumptions, using midpoint/last, ignoring depth, adding fuzzier relationships/venues, cherry-picking, parameter sweeping, or assuming simultaneous fills.

## Boundary
E001 is observational and read-only. A PASS may justify a separately preregistered E002 paper experiment; E001 does not silently become execution testing.
