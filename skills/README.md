# Skill Catalog

This directory is the authoritative paper-writing skill set for this repository.

Most papers should use a subset of these skills. Treat the repository as a staged workflow, not a checklist that every project must exhaust end to end.

## Catalog

- `research-planning`: plan the paper structure, section goals, and writing dependencies
- `literature-search`: retrieve papers from Semantic Scholar, arXiv, OpenAlex, and CrossRef
- `systematic-review`: build a reusable literature corpus and export BibTeX plus synthesis artifacts
- `literature-review`: turn an existing corpus into structured review notes
- `source-material-ingestion`: convert papers, drafts, slides, and spreadsheets into Markdown inputs
- `citation-management`: validate, harvest, and repair references for LaTeX manuscripts
- `paper-memory-ledger`: keep stable project facts, venue constraints, and experiment conclusions across sessions
- `experiment-report-bridge`: turn local experiment artifacts into a paper-ready Markdown report
- `ml-paper-writing`: turn a research repo or result set into a full paper draft with a strong narrative
- `latex-writeup-loop`: complete a live `template.tex` draft using a template-first writeup loop
- `long-form-manuscript-polish`: turn bullet-heavy or slide-like long drafts into professional prose-first manuscripts
- `reverse-outline-flow-check`: diagnose section flow using reverse outlines, paragraph roles, and transitions
- `claim-evidence-map`: map headline claims to explicit supporting evidence and downgrade unsupported ones
- `experiment-section-audit`: redesign Experiments around baseline strength, ablations, and reviewer-facing evidence
- `related-work-writing`: draft a comparative Related Work section
- `survey-generation`: generate a full survey manuscript from a curated corpus
- `paper-writing-section`: draft or revise one section at a time
- `table-generation`: convert verified results into LaTeX tables
- `paper-schematics`: design graphical abstracts, method overviews, and other conceptual manuscript figures
- `academic-plotting`: generate reviewer-readable numeric plots and data-backed figures
- `paper-session-compaction`: compress long writing sessions into a reliable continuation brief
- `venue-submission-strategy`: align the draft to target-venue expectations, page budgets, and reviewer culture
- `reporting-guidelines-check`: audit compliance with study-type reporting standards
- `claim-rigor-audit`: check whether manuscript claims outrun the available evidence or statistics
- `manuscript-scorecard`: score manuscript quality across fixed dimensions and compare revisions
- `latex-formatting`: clean and check venue-facing LaTeX
- `submission-qa-gate`: run the last mechanical submission checks before export
- `paper-compilation`: compile papers and debug LaTeX failures
- `paper-evidence-verifier`: ensure manuscript numbers and condition names match real experiment data
- `citation-verification-gate`: verify bibliography entries against real APIs and prune hallucinated citations
- `self-review`: produce structured paper feedback before submission
- `review-ensemble`: produce stricter multi-reviewer and meta-review style feedback
- `paper-revision`: revise the manuscript against reviewer feedback
- `paper-redline-diff`: generate change-tracked manuscript diffs for revision review and rebuttals
- `rebuttal-writing`: write point-by-point reviewer responses

## Canonical Flow

1. Frame the paper and build the evidence base:
   `research-planning` -> `literature-search` -> `systematic-review` or `literature-review`
2. Normalize source material and keep durable context:
   `source-material-ingestion` -> `paper-memory-ledger`
3. Convert finished experiments into a writing handoff:
   `experiment-report-bridge`
4. Choose one primary drafting engine:
   `ml-paper-writing` for whole-manuscript drafting,
   `latex-writeup-loop` for in-template LaTeX drafting,
   `paper-writing-section` / `related-work-writing` / `survey-generation` for section-scoped work
5. Apply section-level specialists only where needed:
   `reverse-outline-flow-check`, `long-form-manuscript-polish`, `claim-evidence-map`, `experiment-section-audit`, `table-generation`, `paper-schematics`, `academic-plotting`
6. Run trust and compliance checks before export:
   `citation-management`, `paper-evidence-verifier`, `claim-rigor-audit`, `citation-verification-gate`, `reporting-guidelines-check`, `venue-submission-strategy`
7. Run the submission stack:
   `latex-formatting` -> `submission-qa-gate` -> `paper-compilation`
8. Run the review loop:
   `self-review` or `review-ensemble` -> `paper-revision` -> `paper-redline-diff` -> `rebuttal-writing`
9. Use continuity tools only when needed:
   `paper-session-compaction` for long-thread handoff, `paper-memory-ledger` for durable project facts

## Boundary Rules

- Choose one primary drafting engine at a time. Do not default to mixing `ml-paper-writing`, `latex-writeup-loop`, and `paper-writing-section` in the same step.
- Use `paper-schematics` for conceptual, non-numeric figures. Use `academic-plotting` for numeric or data-backed visuals.
- Use `claim-evidence-map` for paper-visible support mapping, `paper-evidence-verifier` for artifact-grounded numeric checks, and `claim-rigor-audit` for inference validity.
- Use `submission-qa-gate` for overall readiness. Use `paper-compilation` only when LaTeX build/debug is the bottleneck.
- Use `self-review` for a quick single pass. Use `review-ensemble` only when you need a stricter committee-like signal.
- Use `paper-memory-ledger` for stable cross-session facts. Use `paper-session-compaction` for one long thread that needs a compact handoff.
