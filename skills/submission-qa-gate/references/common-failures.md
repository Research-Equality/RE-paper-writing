# Common Failures

## Hard Failures

- Missing citation keys
- Missing figure files
- `TODO`, `FIXME`, `TBD`, or placeholder text left in the manuscript
- Compile failure or unresolved bibliography pass
- Anonymization violations for double-blind venues

## Soft Failures That Often Become Hard Failures

- Unreferenced labels
- Figures or tables without labels
- Excessive compile warnings around references or floats
- Word or page budget drift after late revisions
- Bibliography entries that exist but are clearly suspicious or off-topic

## Triage Guidance

- Route citation problems to `citation-management` first.
- Route fabricated or suspicious references to `citation-verification-gate`.
- Route style or venue compliance issues to `latex-formatting`.
- Route build failures to `paper-compilation`.
- Route unsupported numbers or table values to `paper-evidence-verifier`.
