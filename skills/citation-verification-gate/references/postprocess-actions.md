# Post-Process Actions

Once verification is complete, apply the bibliography gate to the manuscript.

## Verified BibTeX

- Rebuild a cleaned `.bib` that keeps verified entries
- Optionally keep suspicious or skipped entries for manual review, but do not treat them as safe by default

## Inline Citation Repair

- Remove hallucinated keys from `\cite{...}` groups
- If a citation group becomes empty, remove the entire citation
- Keep verified and still-acceptable suspicious keys intact

## Relevance Pruning

- After existence verification, prune obviously off-topic or uncited entries
- Avoid a bloated bibliography that no longer matches the paper text

## Reporting

Record:

- total entries
- verified count
- suspicious count
- hallucinated count
- skipped count
- integrity score

This turns citation cleanup into an auditable gate instead of a vague editing pass.
