# Project State

Last updated: 2026-09-19

## Status
- Foundation: COMPLETE
- Venue research: COMPLETE for minimum viable scope
- E001: PREREGISTERED
- E001 data collection: NOT STARTED
- Paper execution: NOT APPROVED
- Live execution: PROHIBITED

## Authoritative decisions
1. Kalshi only for E001.
2. Mechanically verifiable daily-temperature partitions only.
3. NLP/LLM similarity cannot make a relationship trade-eligible.
4. Last trade, midpoint, and displayed probability are never executable pricing.
5. No real-money orders, deposits, or funded execution.
6. E001 profitability is not evaluated before this preregistration is committed.

## Blocking semantic proof before E001 may run
AMENDMENT_001 requires venue-authoritative evidence that the final settlement value's granularity makes the structured temperature buckets collectively exhaustive on the actual settlement state space. Adjacent display labels alone are not proof. Until that evidence is recorded and encoded, live profitability scanning remains disabled.

## Next step
Resolve and document the settlement-value granularity proof required by AMENDMENT_001, encode it as a fail-closed semantics gate, then add durable append-only raw/derived observation storage and episode reconstruction. Only after both are complete may E001 move from PREREGISTERED to RUNNING.
