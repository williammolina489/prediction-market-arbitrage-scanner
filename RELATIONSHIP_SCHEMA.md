# Relationship Schema

Formal taxonomy:
- EXACT_COMPLEMENT
- MUTUALLY_EXCLUSIVE_EXHAUSTIVE
- SUBSET
- SUPERSET
- PARTITION
- DUPLICATE

Only PARTITION / MUTUALLY_EXCLUSIVE_EXHAUSTIVE daily-temperature relationships are eligible in E001. All other types are taxonomy-only during E001.

## E001 proof
All legs must share event and series identity, occurrence time, close time, expected/latest expiration semantics, early-close condition, exceptional-resolution rules, and standard linear-cent pricing. The event/series must provide a non-empty settlement source and the event must explicitly declare mutual exclusivity.

The integer buckets must contain exactly one lower tail (less), exactly one upper tail (greater), and any middle between-ranges must be contiguous, gap-free, and non-overlapping. Any missing or conflicting critical semantic field fails closed.

Each relationship receives a deterministic fingerprint. Episode identity is venue + relationship type + sorted market IDs + basket direction.

## E001 preregistration amendment: settlement lattice

AMENDMENT_001 tightens the partition proof before any E001 observation is collected. A venue-authoritative source must establish that the final settlement value is reported/resolved on a granularity compatible with the proposed bucket boundaries. The scanner may not infer exhaustiveness merely because labels look adjacent.

Until that proof is encoded, discovered temperature groups are structural candidates only and live profitability scanning is disabled.
