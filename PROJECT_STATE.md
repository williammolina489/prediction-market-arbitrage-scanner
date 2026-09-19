# Project State

Last updated: 2026-09-19

## Status
- Foundation: COMPLETE
- Venue research: COMPLETE for minimum viable scope
- E001: STOP / REJECT — BLOCKED / SEMANTICALLY UNPROVABLE
- E001 data collection: NEVER STARTED
- E001 profitability evidence: NONE COLLECTED
- Paper execution: NOT APPROVED
- Live execution: PROHIBITED

## Authoritative decisions
1. Kalshi only was preregistered for E001.
2. E001 required mechanically provable daily-temperature partitions.
3. AMENDMENT_001 required venue-authoritative proof of the final settlement lattice before any profitability collection.
4. That proof did not succeed on 2026-09-19.
5. Stage 2 collector development and E001 activation are therefore prohibited under the preregistered stopping rule.
6. No real-money orders, deposits, funded execution, paper execution, or historical quote reconstruction occurred.

## Why E001 is blocked
Two independent issues prevent the guaranteed-payoff proof:

1. Settlement-lattice proof is incomplete. Current Kalshi series metadata identifies The Weather Company as the source, but the located authoritative public material does not specify the exact final-value rounding/transformation that maps the source measurement onto the integer-looking daily-temperature buckets. Public TWC APIs demonstrate that higher decimal precision can exist in TWC data products, so integer settlement cannot be inferred from labels or ordinary display precision.

2. Current Kalshi series metadata contains an exceptional no-data rule: if no data is available by the end of the allowed period, all markets resolve to a last fair price determined by Kalshi. The located rules do not prove that this fallback preserves the fixed ALL-YES or ALL-NO basket payoff required by E001.

Either issue is sufficient to fail closed.

## Exact next step
Do not build or run the E001 collector. Any move to a different category, a different relationship structure, or a redefined guarantee would require a separately documented preregistration amendment/new experiment decision before any evidence is viewed.


## E003 — Prospective Nested-Threshold Arbitrage Census

Status: STOP / REJECT — PAYOFF INVARIANT UNPROVABLE
Research date: 2026-09-19
Branch: research/e003-nested-thresholds

E003 investigated same-event ordered BTC threshold contracts in Kalshi series KXBTCD. Under ordinary binary settlement, two markets with the same settlement variable and operator and thresholds L < H have the implication event(H) => event(L), so YES(lower) + NO(higher) has a minimum binary-state payoff of $1 per matched pair.

The full contractual state space is broader. BTC contract terms expressly permit Kalshi to initiate Market Outcome Review pursuant to Rule 6.3(c). Current Rule 6.3(c) permits Kalshi, when ordinary determination is not possible, to determine proportional payouts using the contract's last traded price or a binding fair allocation determined by the Outcome Review Committee. No authoritative rule located requires those exceptional proportional payouts to remain monotone across strikes of one KXBTCD event.

For exceptional YES payouts p_L and p_H, the proposed pair pays p_L + (1 - p_H) = 1 + p_L - p_H. A $1 floor therefore requires p_L >= p_H in every permitted review outcome. That invariant is not established by the current rules.

No E003 profitability evidence was viewed. E003 was stopped before preregistration, economic parameter selection, code implementation, collector construction, or any credential use.
