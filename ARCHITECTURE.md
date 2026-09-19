# Architecture

1. Read-only venue adapter.
2. Contract-semantics normalizer.
3. Deterministic relationship validator that fails closed.
4. Executable-pricing layer that walks displayed depth for every leg.
5. Cost/risk layer for fees, slippage reserve, and non-atomic execution buffer.
6. Scanner that emits explainable observations.
7. Persistence/episode layer, to be added before E001 starts.

Invariants: no trading endpoint exists; validation precedes pricing; unresolved critical semantics reject the relationship; all legs use one common quantity; top-of-book is never extrapolated; theoretical and executable after-cost edge are reported separately.
