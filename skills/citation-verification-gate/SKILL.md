---
name: citation-verification-gate
description: Verify bibliography entries against real academic APIs, classify citations as verified, suspicious, hallucinated, or skipped, and prune or annotate the manuscript accordingly. Use when a draft already has references but their reality or topical relevance is uncertain.
argument-hint: [paper-and-bib]
---

# Citation Verification Gate

Use this skill after drafting, when the question is no longer "what should we cite?" but "are these citations real and defensible?"

## When to Use

- The paper already has a `.bib` file or inline citation set
- The draft was produced or expanded by an LLM and may contain hallucinated references
- You need a verification report, not just citation formatting cleanup

For missing-citation discovery or bibliography repair, use `citation-management`.

## Workflow

### Step 1: Parse the Bibliography
- Extract each BibTeX entry with its key, title, DOI, arXiv ID, authors, and year.
- Keep the original citation key mapping intact so the paper can be repaired later.

### Step 2: Verify Against Real APIs
- L1: verify by arXiv ID when available
- L2: verify by DOI through CrossRef
- L3: fall back to title search across Semantic Scholar and arXiv

### Step 3: Classify Each Entry
- `verified`: source exists and title match is strong
- `suspicious`: a nearby source exists but metadata diverges materially
- `hallucinated`: no real match or the match is too weak
- `skipped`: unverifiable because the entry lacks enough usable metadata

### Step 4: Repair the Paper
- Remove hallucinated citations from inline citation groups
- Rebuild a verified `.bib` that keeps verified entries and optionally suspicious ones
- Prune uncited or low-relevance entries after verification

### Step 5: Report Integrity
- Produce a summary with total, verified, suspicious, hallucinated, skipped, and an integrity score
- Surface exactly which entries need human intervention

## References

- `references/verification-layers.md`: API verification strategy and classification thresholds
- `references/postprocess-actions.md`: how to prune or annotate the manuscript after verification

## Rules

- Do not keep a hallucinated citation just because it fits the narrative.
- A suspicious citation is not equivalent to a verified citation.
- Preserve the audit trail: the paper should show what was removed or downgraded.
- Bibliography verification happens after drafting and before final export.

## Related Skills

- Upstream: [citation-management](../citation-management/), [ml-paper-writing](../ml-paper-writing/)
- Downstream: [latex-writeup-loop](../latex-writeup-loop/), [paper-compilation](../paper-compilation/)
- See also: [paper-evidence-verifier](../paper-evidence-verifier/)
