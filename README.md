# Prediction Market Arbitrage Scanner

> **PROJECT CLOSED — STRICT ARBITRAGE THESIS NOT ADVANCED**

This repository preserves the history of a research-only investigation into **strict structural prediction-market arbitrage**.

It is archived as a research record, not maintained as an active trading project.

## Final outcome

Two strict structural constructions were investigated:

1. **E001 — Daily-temperature exhaustive partitions**
   - STOP / REJECT.
   - The required settlement lattice / rounding semantics were not proven.
   - Exceptional no-data / fair-price resolution did not establish preservation of the fixed partition payoff invariant.

2. **E003 — Nested BTC thresholds**
   - STOP / REJECT.
   - The ordinary binary subset relationship was valid.
   - The explicit no-data state preserved the proposed pair payoff.
   - But Kalshi Market Outcome Review under Rule 6.3(c) permits proportional contract-level payouts, and no authoritative cross-strike monotonicity guarantee was established.
   - Therefore the proposed minimum $1 pair payoff could not be proven across every permitted settlement state.

**E002**, the separately gated paper-execution experiment, never started because its prerequisite was never reached.

## What this repository does not show

The project did **not** empirically demonstrate that prediction-market arbitrage is unprofitable.

E001 and E003 failed at the contract-semantics / payoff-proof stage. They were not negative P/L backtests.

- No E001 profitability evidence was collected.
- No E003 profitability evidence was viewed.
- No historical or prospective profitability experiment was activated.

The narrower conclusion is that the two investigated constructions could not honestly be characterized as guaranteed arbitrage under the full contractually permitted settlement state space.

## Safety and execution status

Permanently for this closed project:

- no order placement;
- no authenticated trading;
- no real money;
- no deposits or withdrawals;
- no paper execution;
- no historical quote reconstruction or fabricated backfill.

Some source files remain as historical research scaffolding. Their presence does not authorize restarting a scanner, collector, paper trader, or live execution system.

## Research history

- `research/e001/` preserves the E001 preregistration, amendment, and semantic blocker.
- `research/e003/NESTED_THRESHOLD_BLOCKER.md` preserves the E003 payoff-invariant failure.
- `EXPERIMENTS.md` records terminal experiment status.
- `PROJECT_STATE.md` is the final project-state authority.
- `ROADMAP.md` records that there is no active milestone and no E004 planned.

## Closure boundary

Do not repurpose this repository into relative-value, statistical-arbitrage, forecasting, or market-making research. Those are materially different projects.

The strict-arbitrage program should only be reopened for a materially new contractual structure whose bounded payoff can be proven across **all permitted settlement states before profitability evidence is viewed**.

For archival verification only:

```bash
python -m pip install -e '.[dev]'
pytest
ruff check .
```
