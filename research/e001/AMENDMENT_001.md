# E001 Preregistration Amendment 001 — Settlement-Value Granularity

Date: 2026-09-19
Status: EFFECTIVE BEFORE DATA COLLECTION
Parent preregistration: research/e001/PREREGISTRATION.md

## Reason

A foundation audit found an implicit assumption in the temperature-partition parser: structured integer strike labels were being treated as proof that the settlement state space itself is integer-valued. That is not sufficient. A continuous or differently rounded settlement value could create semantic gaps even when labels look adjacent.

No E001 opportunity profitability, prospective observation set, or experiment result was evaluated before this amendment. This amendment only makes the semantics gate stricter.

## Amendment

Before E001 may move from PREREGISTERED to RUNNING, the project must preserve venue-authoritative evidence showing the final settlement value's reporting/resolution granularity and boundary interpretation for the selected daily-temperature contract family.

The evidence must establish that:
1. the final settlement value can belong to exactly one frozen bucket;
2. the lower tail, intermediate ranges, and upper tail have no uncovered settlement values;
3. endpoint inclusion/exclusion matches the deterministic parser;
4. the evidence applies to the same current settlement source and contract family being scanned.

If this cannot be established mechanically and durably, the relationship is ineligible.

## Operational consequence

- Live market discovery and metadata validation may continue.
- Live opportunity-profitability scanning is disabled.
- No E001 observations count toward the evidence window until this gate is implemented.
- No economic threshold, cost assumption, or promotion criterion is relaxed.

This amendment preserves the project's fail-closed principle and preference for false negatives over semantic false positives.
