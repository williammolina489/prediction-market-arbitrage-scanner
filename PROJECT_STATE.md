# Project State

Last updated: 2026-09-19

# PROJECT STATUS

**CLOSED — STRICT ARBITRAGE THESIS NOT ADVANCED**

This repository is an archived research program for strict structural prediction-market arbitrage. It is not an active strategy-development project.

No real-money system exists.
No paper-execution system exists.
No profitability experiment was ever activated.

## Final experiment state

### E001 — STOP / REJECT — semantic proof failed

E001 tested whether Kalshi daily-temperature markets could be treated as mechanically exhaustive partitions with a fixed basket payoff.

It stopped before profitability collection because the required contract semantics could not be proven across the full permitted settlement state space:

1. the final settlement-value lattice / rounding transformation was not established; and
2. the exceptional no-data / last-fair-price resolution did not establish preservation of the ALL-YES / ALL-NO partition payoff invariant.

No E001 profitability evidence was collected.

Historical records are preserved under `research/e001/`.

### E002 — STOP / REJECT — prerequisite never reached

E002 was the separately gated paper-execution experiment that would only have been considered after an E001 pass.

E001 never passed, so E002's gate was never reached. No paper-execution system was built or run.

### E003 — STOP / REJECT — payoff invariant failed

E003 investigated same-event ordered BTC threshold contracts in Kalshi series KXBTCD.

Under ordinary binary settlement, the nested subset implication was established: for thresholds L < H on the same settlement variable and operator, the higher-threshold event implies the lower-threshold event.

The explicit no-data state also preserved the proposed pair payoff.

However, the BTC terms incorporate Kalshi Market Outcome Review under Rule 6.3(c), which permits proportional contract-level payouts. No authoritative cross-strike monotonicity guarantee was established for those exceptional payouts. Therefore the minimum $1 payoff of YES(lower) + NO(higher) could not be proven across every contractually permitted resolution state.

No E003 profitability evidence was viewed.
No E003 preregistration was created.
No E003 collector or execution system was built.

The blocker record is preserved at `research/e003/NESTED_THRESHOLD_BLOCKER.md`.

## What the failures mean

E001 and E003 are **contract-semantics / payoff-proof failures**.

They are **not negative P/L backtests** and are not empirical evidence that prediction-market arbitrage is unprofitable.

No historical or prospective profitability experiment was activated for either construction. The project therefore makes no claim that prediction-market arbitrage in general is profitable or unprofitable.

The narrower conclusion is:

> The two strict structural-arbitrage constructions investigated here could not establish their required guaranteed-payoff invariants across the full contractually permitted settlement state space.

Accordingly, this project cannot honestly characterize those constructions as guaranteed arbitrage.

## Permanent safety / execution state

- No order-placement capability is authorized.
- No authenticated trading workflow is part of this project.
- No real money was used.
- No deposits or withdrawals were made or enabled.
- No paper execution was run.
- No historical quote reconstruction or fabricated backfill was used.
- Existing source code is historical research scaffolding only and is not an approved execution system.

## Closure rule

No E004 is planned.

Do not convert this repository into relative-value, statistical-arbitrage, forecasting, or market-making research. Those are materially different projects.

The strict-arbitrage program should only be reopened if a materially new contractual structure is identified whose bounded payoff can be proven across **all** permitted settlement states before any profitability evidence is viewed.
