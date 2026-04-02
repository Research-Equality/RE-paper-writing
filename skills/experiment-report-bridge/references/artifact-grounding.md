# Artifact Grounding

## Local File Rules

- Small text files can be quoted or inlined when helpful.
- Large text files should be summarized with their path preserved.
- Binary assets such as images, PDFs, and model checkpoints should be referenced by path, not pasted inline.
- Files outside the workspace should be treated carefully and called out explicitly.

## Missing Evidence Rules

- If a result is expected but absent, write a TODO with the exact command or artifact needed.
- If a figure exists but the metric table does not, do not backfill numbers from memory.
- If QC failed or is incomplete, mention that near the affected result instead of burying it later.

## Good Result Line

`Validation F1 improved from 0.81 to 0.84; see artifacts/metrics/summary.csv and artifacts/plots/f1_curve.png.`

## Bad Result Line

`Validation quality improved substantially and is likely around the mid-80s.`
