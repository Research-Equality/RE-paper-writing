---
name: ml-paper-writing
description: Write a full ML, AI, or systems paper from a research repository or mature result set. Use when the user needs a complete manuscript narrative, venue-aware section planning, citation-safety rules, or a proactive first draft rather than section-by-section editing.
argument-hint: [repo-or-draft]
---

# ML Paper Writing

Use this skill when the task is the whole manuscript, not just a single section.

## When to Use

- The user has a research repo, experiment folder, or notes and wants a full paper draft
- The core contribution exists, but the paper story, section ordering, and evidence packaging are still weak
- The user wants a venue-aware first draft for ML, NLP, CV, or systems-style papers

For isolated edits, prefer the narrower skills:
- `paper-writing-section` for one section
- `related-work-writing` for related work
- `citation-management` for bibliography repair
- `latex-writeup-loop` when the draft already exists inside a template-first LaTeX workflow
- `latex-formatting` and `paper-compilation` for submission readiness

## Workflow

### Step 1: Understand the Project
- Read the repo structure, README, result files, and existing notes.
- Identify the one-sentence contribution before drafting prose.
- Confirm the target venue if it materially changes page limits or paper style.

### Step 2: Build the Paper Story
- Define the paper's `What`, `Why`, and `So What`.
- Decide which results are the headline evidence and which belong in appendix or ablations.
- Draft the paper outline before writing full paragraphs.

### Step 3: Draft Proactively
- If the contribution and results are already clear, write a complete first draft instead of blocking on incremental questions.
- Flag uncertainty inline when needed, but keep momentum.
- Keep one paragraph for one message and one section for one job.

### Step 4: Protect Citation Integrity
- Never invent citations, BibTeX entries, venues, or years.
- If a citation cannot be verified, leave an explicit placeholder and report it.
- Use `citation-management` or the workflows in `references/citation-workflow.md`.

### Step 5: Iterate Like a Reviewer
- Re-read the draft as a skeptical reviewer.
- Check whether the abstract, introduction, and figures already make the paper understandable before the methods section.
- Use the review checklists before declaring the draft ready.

## References

Load only what the task needs:

- `references/writing-guide.md`: narrative, abstract, introduction, sentence-level clarity
- `references/checklists.md`: full-draft and submission checklists
- `references/reviewer-guidelines.md`: what reviewers optimize for
- `references/citation-workflow.md`: verified citation workflow
- `references/systems-conferences.md`: systems-paper framing differences
- `references/ml-paper-guide.md`: longer synthesis of paper-writing guidance

## Rules

- A paper is a claim package, not a dump of experiments.
- Lead with the strongest contribution and evidence; do not bury the result.
- Reduce or remove any claim that is not directly supported by results.
- Treat abstract, introduction, and Figure 1 as first-pass decision points for reviewers.
- Use placeholders rather than unverifiable citations.

## Related Skills

- Upstream: [research-planning](../research-planning/), [literature-review](../literature-review/), [systematic-review](../systematic-review/)
- Downstream: [paper-writing-section](../paper-writing-section/), [related-work-writing](../related-work-writing/), [citation-management](../citation-management/), [academic-plotting](../academic-plotting/), [paper-schematics](../paper-schematics/), [latex-writeup-loop](../latex-writeup-loop/)
- See also: [source-material-ingestion](../source-material-ingestion/), [experiment-report-bridge](../experiment-report-bridge/), [paper-memory-ledger](../paper-memory-ledger/), [paper-session-compaction](../paper-session-compaction/), [claim-rigor-audit](../claim-rigor-audit/), [manuscript-scorecard](../manuscript-scorecard/), [venue-submission-strategy](../venue-submission-strategy/), [reporting-guidelines-check](../reporting-guidelines-check/), [latex-formatting](../latex-formatting/), [paper-compilation](../paper-compilation/), [self-review](../self-review/), [review-ensemble](../review-ensemble/), [long-form-manuscript-polish](../long-form-manuscript-polish/), [submission-qa-gate](../submission-qa-gate/), [reverse-outline-flow-check](../reverse-outline-flow-check/), [claim-evidence-map](../claim-evidence-map/), [experiment-section-audit](../experiment-section-audit/)
