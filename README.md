[English](README.md) | [简体中文](README.zh.md)

# RE-paper-writing

An authoritative skills repository for academic paper planning, literature grounding, section drafting, revision, and LaTeX-based submission workflows.

This repository is a curated home for skills that directly support writing and revising research papers. The canonical loadable skill set lives under [`skills/`](skills/). Other root-level directories are source snapshots and upstream references, not the normalized skill catalog.

Most projects should use a subset of these skills. The repository is intended as a staged workflow with clear entry points, not as a checklist that every paper must invoke from start to finish.

## Positioning

- Keep only skills that directly support paper planning, literature review for writing, section drafting, citation work, tables, LaTeX preparation, self-review, revision, and rebuttal writing
- Normalize upstream content into a portable repository layout with repository-relative paths instead of one author's local machine paths
- Treat [`skills/`](skills/) as the authoritative directory for future paper-writing-related skill work

## Included Skills

The curated collection currently contains 35 skills:

### Planning and Literature Grounding

- `research-planning`: turn a topic or draft idea into a paper plan and section architecture
- `literature-search`: multi-source academic search with structured JSONL output
- `systematic-review`: artifact-first systematic review pipeline for building a reusable paper corpus
- `literature-review`: synthesize a collected corpus through multi-perspective review
- `source-material-ingestion`: convert PDFs, DOCX, PPTX, XLSX, and related source files into Markdown writing inputs
- `citation-management`: validate, harvest, repair, and export BibTeX references
- `paper-memory-ledger`: persist stable project facts, venue choices, experiment conclusions, and writing conventions across sessions

### Drafting and Manuscript Construction

- `experiment-report-bridge`: turn local experiment artifacts into a paper-ready Markdown report before full manuscript drafting
- `ml-paper-writing`: orchestrate a complete paper draft from a research repo or mature result set
- `latex-writeup-loop`: write directly inside `template.tex` with section, citation, and compile loops
- `long-form-manuscript-polish`: convert bullet-heavy or slide-like long drafts into professional prose-first manuscripts
- `reverse-outline-flow-check`: diagnose section flow using reverse outlines, paragraph roles, and logical transitions
- `claim-evidence-map`: map headline claims to explicit support anchors and downgrade unsupported wording
- `experiment-section-audit`: redesign Experiments around contribution-linked validation, strong baselines, and reviewer-readable evidence
- `related-work-writing`: write thematic, comparative Related Work sections
- `survey-generation`: generate survey manuscripts from a curated literature corpus
- `paper-writing-section`: draft or revise one paper section at a time
- `table-generation`: convert result files into publication-ready LaTeX tables
- `paper-schematics`: design graphical abstracts, method flowcharts, and other conceptual manuscript figures
- `academic-plotting`: create numeric plots and other data-backed publication figures

### Submission, Review, and Revision

- `paper-session-compaction`: compact long drafting or revision sessions into a reliable continuation brief
- `venue-submission-strategy`: adapt framing, page budget, and reviewer-facing packaging to a target venue
- `reporting-guidelines-check`: audit compliance with study-type standards such as CONSORT, STROBE, and PRISMA
- `claim-rigor-audit`: stress-test claims for bias, confounding, evidence strength, and statistical overreach
- `manuscript-scorecard`: score manuscript quality dimension by dimension and track revision progress
- `latex-formatting`: venue-aware LaTeX cleanup and format checks
- `submission-qa-gate`: run deterministic pre-submission checks for labels, TODO markers, citation coverage, and compile readiness
- `paper-compilation`: compile papers and debug LaTeX build failures
- `paper-evidence-verifier`: verify that manuscript numbers and conditions match real experiment artifacts
- `citation-verification-gate`: verify references against real APIs and prune hallucinated citations
- `self-review`: run structured pre-submission paper review
- `review-ensemble`: run multi-reviewer, meta-review-style manuscript assessment
- `paper-revision`: map reviewer feedback to concrete manuscript edits
- `paper-redline-diff`: generate change-tracked manuscript diffs for revision review and rebuttal support
- `rebuttal-writing`: produce point-by-point reviewer responses

See [`skills/README.md`](skills/README.md) for the skill catalog and routing guidance.

## Canonical Workflow

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

Shared artifact conventions:

- `outputs/<topic-slug>/search_results/*.jsonl` for raw retrieval results
- `outputs/<topic-slug>/paper_db.jsonl` for the shared literature corpus
- `outputs/<topic-slug>/reading_notes.md`, `synthesis.md`, and `gaps.md` for intermediate review artifacts
- `references.bib` for the active bibliography

## Repository Layout

```text
skills/
  citation-management/
  latex-formatting/
  literature-review/
  literature-search/
  source-material-ingestion/
  paper-memory-ledger/
  experiment-report-bridge/
  ml-paper-writing/
  latex-writeup-loop/
  long-form-manuscript-polish/
  reverse-outline-flow-check/
  claim-evidence-map/
  experiment-section-audit/
  paper-session-compaction/
  claim-rigor-audit/
  manuscript-scorecard/
  paper-schematics/
  reporting-guidelines-check/
  venue-submission-strategy/
  paper-evidence-verifier/
  submission-qa-gate/
  paper-compilation/
  paper-revision/
  paper-redline-diff/
  paper-writing-section/
  rebuttal-writing/
  related-work-writing/
  research-planning/
  review-ensemble/
  self-review/
  survey-generation/
  systematic-review/
  table-generation/
  academic-plotting/
  citation-verification-gate/
```

## Usage

Commands below assume you run them from the repository root.

Example: search and build a portable literature corpus

```bash
python skills/systematic-review/scripts/search_semantic_scholar.py \
  --query "long-context reasoning agents" \
  --max-results 20 \
  --api-key "$S2_API_KEY" \
  -o outputs/long-context-reasoning-agents/search_results/s2.jsonl

python skills/systematic-review/scripts/bibtex_manager.py \
  --jsonl outputs/long-context-reasoning-agents/paper_db.jsonl \
  --output outputs/long-context-reasoning-agents/references.bib
```

Recommended environment:

- Python 3.10+
- Optional environment variable: `S2_API_KEY`
- Optional dependency: `PyMuPDF` for PDF extraction in `self-review` and `systematic-review`

## Curation Rules

- A skill must directly improve paper planning, writing, citation integrity, review quality, or LaTeX submission readiness
- Skills for experiment execution, generic code generation, GitHub repo mining, or presentation-only workflows do not belong in this curated set
- Prefer scriptable and auditable skills over opaque prompt bundles when the task is repetitive or fragile

## Provenance

The current curated skill set was extracted from the `agent-research-skills/` source snapshot already present in this repository and normalized into the authoritative `skills/` layout.

Additional paper-writing skills were also extracted from the `AI-research-SKILLs/20-ml-paper-writing/` source snapshot and normalized into the same catalog.

Additional workflow-specific skills were extracted from `ai-scientist/`, especially its LaTeX writeup and ensemble review loops.

Additional verification-oriented skills were extracted from `AutoResearchClaw/`, especially its evidence-grounding and citation-audit gates.

Additional submission-oriented skills were extracted from `claude-scientific-skills/`, especially its venue strategy, reporting-compliance, and manuscript-schematic guidance.

Additional writing-tooling skills were extracted from `claude-scientific-writer/`, especially document ingestion, quantitative manuscript scoring, and claim-rigor audit workflows.

Additional session-oriented writing skills were extracted from `EvoScientist/`, especially its artifact-grounded writing agent, context-compaction flow, and persistent project memory conventions.

Additional LaTeX-adjacent paper-writing skills were extracted from `latex-document-skill/`, especially its revision redline workflow, long-form manuscript anti-pattern guidance, and pre-submission QA checks.

Additional reviewer-facing writing skills were extracted from `Research-Paper-Writing-Skills/`, especially its reverse-outlining workflow, claim-support alignment checks, and experiments-writing guidance.

Notable curation decisions:

- `deep-research` was renamed and simplified as `systematic-review`
- Hard-coded user-local paths were replaced with repository-relative references
- Only paper-writing-related skills were retained; experiment, coding, and general research-automation skills were excluded
