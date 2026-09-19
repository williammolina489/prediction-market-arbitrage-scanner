# E003 — Nested-Threshold Payoff-Invariant Blocker

Date checked: 2026-09-19
Experiment candidate: E003 — Prospective Nested-Threshold Arbitrage Census
Decision: STOP / REJECT — PAYOFF INVARIANT UNPROVABLE
Branch: research/e003-nested-thresholds

## Research boundary

This document records a foundation-only contract-semantics investigation. No historical or prospective opportunity profitability was inspected. No scanner, collector, paper execution, or live execution was run.

E001 remains failed and unchanged. E002 remains the dormant paper-execution experiment that was gated on E001.

## Selected current family

Kalshi series KXBTCD.

Current series metadata:
- asset: BTC;
- category: Crypto;
- frequency: hourly;
- title/family: Bitcoin price Above/below;
- settlement source: CF Benchmarks;
- benchmark: CF Bitcoin Real-Time Index (BRTI);
- fee type: quadratic;
- fee multiplier: 1;
- contract terms: BTC.pdf;
- 60 RTI observations during the final minute are averaged into the official/final value.

Primary sources:
- https://api.elections.kalshi.com/trade-api/v2/series/KXBTCD
- https://assets.kalshi.com/contract_terms/BTC.pdf
- https://help.kalshi.com/en/articles/13823838-crypto-markets
- https://kalshi.com/regulatory/rulebook

## Normal settlement semantics

BTC.pdf defines the Underlying as the spot USD price of one Bitcoin at the specified time according to a simple average of the CF Bitcoin Real-Time Index for the preceding minute (60 seconds). Revisions after Expiration are ignored. CF Benchmarks is the Source Agency.

The Payout Criterion supports above, below, and between price thresholds. The selected candidate relationship only considered same-event ordered above-threshold markets.

For one real-valued settlement variable X and two identically defined thresholds L < H:

    A := X is above L
    B := X is above H

Under a common operator, B implies A. Decimal precision does not break this ordering.

Under ordinary $0/$1 binary resolution:

| Settlement state | YES(lower) | NO(higher) | Pair payout |
|---|---:|---:|---:|
| below lower | 0 | 1 | $1 |
| between thresholds | 1 | 1 | $2 |
| above higher | 1 | 0 | $1 |

So the SUBSET relation itself is valid in the ordinary binary state space.

## No-data rule

BTC.pdf states that if no data is available on the Expiration Date at the Expiration Time, the market resolves No.

Applied consistently to both same-event threshold legs, this state would pay:

    YES(lower) = 0
    NO(higher) = 1

Total = $1.

The explicit no-data rule is therefore not the blocker.

## Fatal exceptional-resolution state

BTC.pdf also states that before Settlement, Kalshi may at its sole discretion initiate the Market Outcome Review Process pursuant to Rule 6.3(c).

Current Rulebook v1.24 Rule 6.3(c) states that when Kalshi cannot determine whether an Expiration Value is inside the Payout Criterion (or what payout proportion applies), Kalshi determines payouts. The permitted methodologies include:
1. using the Contract's last traded price to determine proportional long/short payout; or
2. a binding fair allocation by the Outcome Review Committee if the last price is unavailable or considered unfair.

These are non-binary settlement possibilities.

Let:
- p_L = exceptional YES payout for the lower-threshold contract;
- p_H = exceptional YES payout for the higher-threshold contract.

Because a binary contract's YES and NO allocations sum to $1, the proposed basket receives:

    p_L + (1 - p_H)
  = 1 + p_L - p_H

A guaranteed minimum of $1 requires:

    p_L >= p_H

for every permitted Market Outcome Review resolution.

No current authoritative Kalshi source located imposes this cross-strike monotonicity constraint on last-traded-price settlement or Outcome Review Committee fair allocations. Contract-by-contract market prices can in principle differ independently, and the rule does not state that the committee must jointly preserve threshold ordering.

Therefore the required invariant is unproven.

This is sufficient to fail closed. No actual counterexample settlement needs to be observed, and no profitability data may be consulted to rescue the hypothesis.

## Other current mechanics recorded

- Issuance is recurrent; KXBTCD series metadata currently marks frequency hourly.
- The BTC terms permit price levels in consecutive $0.01 increments and state a $0.01 minimum contract tick.
- Settlement Value is $1.00 under the contract terms.
- Settlement normally occurs no later than the day after Expiration Date unless Market Outcome is under review.
- Expiration is tied to the first minute after the specified time that source data is available, subject to the one-week outer date in BTC.pdf.
- Current live pages show many simultaneously listed threshold markets for one event.
- Current orderbook API documentation returns YES and NO bids only and explains complementary ask mechanics.
- The current orderbook documentation examples require KALSHI-ACCESS authentication headers. No credentials were introduced.
- Current API documentation describes token-based authenticated read/write rate limits.

## Pair-selection research decision

If the payoff invariant had passed, E003 would have used ADJACENT ORDERED STRIKES ONLY. This rule was selected before viewing any opportunity evidence for methodological simplicity, reduced pseudo-replication, and a deterministic universe.

Because the invariant failed, this is not a frozen live-experiment parameter and no preregistration was created.

## Parameters not reached

The following were deliberately NOT frozen because the proof failed before preregistration:
- common quantity;
- gross discrepancy threshold;
- fee calculation assumptions beyond recording current series metadata;
- slippage reserve;
- non-atomic execution reserve;
- depth threshold;
- observation cadence;
- episode/persistence rule;
- evidence window;
- promotion criteria;
- rejection thresholds beyond the semantic stop.

Choosing any of these after viewing opportunity profitability would require a new clean preregistration process.

## Decision

E003 STOP / REJECT — PAYOFF INVARIANT UNPROVABLE.

Do not create research/e003/PREREGISTRATION.md.
Do not create a proof document claiming trade eligibility.
Do not build or start an E003 collector.
Do not immediately substitute another asset, category, pair direction, cross-venue construction, or wider pair search in this session.

## Integrity confirmation

- No profitability evidence viewed.
- No historical quote reconstruction.
- No performance-based tuning.
- No orders placed.
- No real money used.
- No authenticated trading credentials added.
- E001 preserved as failed.
- E002 preserved as dormant/gated.
