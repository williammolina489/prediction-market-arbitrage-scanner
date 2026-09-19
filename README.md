# Prediction Market Arbitrage Scanner

A research-only, read-only scanner for structurally valid prediction-market pricing inconsistencies.

The project is deliberately closer to a theorem checker plus market-microstructure engine than a forecasting model. It only treats an opportunity as trade-eligible when the relationship between contracts is mechanically validated and the complete basket is executable at displayed depth after fees, slippage reserve, and an explicit non-atomic execution-risk buffer.

## Current scope

- Venue: Kalshi only.
- E001 category: standardized daily-temperature bucket events.
- E001 relationship: mechanically verified exhaustive partitions.
- Execution: disabled. No live orders, funded trading, or deposits.
- Data access: public read-only REST endpoints only for the foundation.
- Experiment status: E001 PREREGISTERED; not running.

## Quick start

```bash
python -m pip install -e '.[dev]'
pmarb validate-live
pytest
ruff check .
```

`validate-live` performs read-only market discovery/metadata validation. `scan-once` is intentionally blocked while E001 remains PREREGISTERED; it will not be enabled until AMENDMENT_001's settlement-granularity proof and the persistence layer are complete. No trading endpoint exists.

See `research/e001/PREREGISTRATION.md` before changing any E001 parameter.
