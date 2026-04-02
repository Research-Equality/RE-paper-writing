---
name: latex-writeup-loop
description: Write a complete paper directly inside an existing LaTeX template using a template-first section loop, citation passes, figure validation, and compile-fix iterations. Use when the repo already has `template.tex`, notes, figures, and logs, and the task is to turn them into a submission-shaped manuscript.
argument-hint: [paper-folder]
---

# LaTeX Writeup Loop

Use this skill when the manuscript already lives inside a LaTeX template and needs to be completed in-place.

## When to Use

- The project has `latex/template.tex` or an equivalent manuscript scaffold
- Figures, logs, and notes already exist, but the paper text is incomplete
- The task is not just editing prose, but managing the full template-first writeup loop

For broader manuscript strategy, use `ml-paper-writing`.
For standalone section edits, use `paper-writing-section`.
For bibliography repair, use `citation-management`.

## Workflow

### Step 1: Inspect the Scaffold
- Read `template.tex` and identify placeholder sections, current bibliography block, and referenced figures.
- Inventory available `.png`, `.pdf`, result logs, and notes before writing.

### Step 2: Fill the Paper in Section Order
- Draft sections in a stable order: Abstract, Introduction, Related Work, Background, Method, Experimental Setup, Results, Conclusion.
- Keep each section grounded in existing evidence and repo artifacts.
- Use the section guidance in `references/section-tips.md`.

### Step 3: Run Two Refinement Passes
- First pass: eliminate factual and LaTeX errors.
- Second pass: compress, remove duplication, and align the section with the rest of the paper.

### Step 4: Close Citation Gaps
- Identify the single most important missing citation each round.
- Search, verify, and add only real citations.
- Stop when the draft is adequately supported; do not add citations mechanically.

### Step 5: Validate Template Integrity
- Confirm every `\cite{}` resolves in the local bibliography.
- Confirm every `\includegraphics{}` points to a real file.
- Remove duplicate figure uses, duplicate section headers, bad environment closures, and placeholder captions.

### Step 6: Compile and Fix
- Run the full LaTeX pipeline.
- Use the minimal fix needed for each error.
- Repeat until the manuscript builds or a real blocker remains.

## References

- `references/section-tips.md`: section-specific writing expectations
- `references/quality-checks.md`: compile loop, citation checks, and template hygiene
- `references/template-structure.md`: canonical AI-Scientist-style LaTeX scaffold

## Rules

- Do not invent numerical results, ablations, or hardware details not present in logs.
- Do not add a citation unless it can be verified and placed in the bibliography.
- Keep each figure in the paper only where it contributes most.
- Fix LaTeX with the smallest safe change; do not destabilize packages or structure unnecessarily.

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [academic-plotting](../academic-plotting/), [citation-management](../citation-management/)
- Downstream: [latex-formatting](../latex-formatting/), [paper-compilation](../paper-compilation/)
- See also: [paper-writing-section](../paper-writing-section/), [review-ensemble](../review-ensemble/), [paper-evidence-verifier](../paper-evidence-verifier/), [citation-verification-gate](../citation-verification-gate/), [experiment-report-bridge](../experiment-report-bridge/), [paper-session-compaction](../paper-session-compaction/), [paper-memory-ledger](../paper-memory-ledger/), [submission-qa-gate](../submission-qa-gate/), [paper-redline-diff](../paper-redline-diff/)
