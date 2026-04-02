# Verification Layers

AutoResearchClaw verifies citations with a layered strategy.

## Layer 1: arXiv ID Lookup

- Best when an entry includes a trusted arXiv identifier
- Query arXiv directly by `id_list`
- Strong title similarity yields `verified`
- Weak title similarity yields `suspicious`

## Layer 2: DOI Resolution

- Query CrossRef using the DOI
- If the DOI resolves but metadata diverges, classify as `suspicious`
- If the DOI cannot be resolved, continue to title search

## Layer 3: Title Search

- Search Semantic Scholar and arXiv by title
- Use title similarity thresholds to distinguish:
  - `verified` for strong similarity
  - `suspicious` for partial but plausible matches
  - `hallucinated` when nothing credible is found

## Final Labels

- `verified`
- `suspicious`
- `hallucinated`
- `skipped`

The point is not just formatting correctness. The point is source reality.
