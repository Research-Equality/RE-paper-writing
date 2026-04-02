---
name: experiment-report-bridge
description: Turn experiment plans, logs, tables, and artifacts into a paper-ready Markdown report that can feed directly into manuscript drafting. Use when results exist locally but are not yet shaped into a coherent writing handoff.
argument-hint: [experiment-folder-or-artifacts]
---

# Experiment Report Bridge

Use this skill between "experiments finished" and "paper drafting starts."

## When to Use

- You have experiment folders, result tables, plots, and logs but no stable narrative report yet
- The team needs a Markdown handoff before writing LaTeX or section prose
- Results are partly complete and missing items need explicit TODOs rather than guesswork

For full-paper drafting, use `ml-paper-writing`.
For numeric consistency checks, use `paper-evidence-verifier`.

## Workflow

### Step 1: Gather the Local Evidence
- Read the experiment plan, run logs, metrics files, figures, tables, and QC notes.
- Keep file paths for every artifact that may later be cited in the paper.
- Separate completed evidence from missing or unreliable evidence.

### Step 2: Ground the Context Safely
- Inline only small text artifacts when helpful; keep large or binary assets referenced by path.
- Prefer workspace-local files and note when an artifact sits outside the main project tree.
- Preserve the original filenames so later drafting can trace every statement.

### Step 3: Draft the Report
- Write a clear Markdown report with these preferred sections:
  1. Summary and goals
  2. Experiment plan
  3. Setup
  4. Baselines and comparisons
  5. Results
  6. Analysis, limitations, and next steps
  7. Sources, only if web research was used
- Reference figure, table, and result paths directly in the Results section.

### Step 4: Handle Missing Pieces Explicitly
- Do not fabricate results, citations, or evaluation details.
- If something necessary is missing, write a TODO with the exact command or artifact still needed.
- Include negative results, failed runs, and QC caveats when they materially affect interpretation.

### Step 5: Hand Off to Manuscript Writing
- Use the Markdown report as the upstream input for `ml-paper-writing`, `paper-writing-section`, or `latex-writeup-loop`.
- Pass the artifact paths forward so later stages can verify tables, figures, and claims.

## References

- `references/report-structure.md`: section structure and evidence expectations
- `references/artifact-grounding.md`: how to reference local files, large assets, and missing evidence

## Rules

- Every claim must be backed by a local artifact path or marked as missing.
- Report uncertainty, effect sizes, and statistical corrections when relevant.
- Include negative results and limitations instead of hiding them.
- Keep the report Markdown-first and paper-ready, not notebook-style or chat-style.

## Related Skills

- Upstream: [research-planning](../research-planning/), [source-material-ingestion](../source-material-ingestion/), [table-generation](../table-generation/), [academic-plotting](../academic-plotting/)
- Downstream: [ml-paper-writing](../ml-paper-writing/), [paper-writing-section](../paper-writing-section/), [latex-writeup-loop](../latex-writeup-loop/)
- See also: [paper-evidence-verifier](../paper-evidence-verifier/), [claim-rigor-audit](../claim-rigor-audit/), [claim-evidence-map](../claim-evidence-map/), [experiment-section-audit](../experiment-section-audit/)
