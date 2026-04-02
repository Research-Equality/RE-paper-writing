# Systematic Review Workflow

Use this guide when you need a disciplined, artifact-first review process for paper writing.

## Workspace Rule

All generated outputs belong under `outputs/<topic-slug>/`. Keep the skill directory read-only.

Recommended layout:

```text
outputs/<topic-slug>/
├── search_results/
│   ├── s2.jsonl
│   └── arxiv.jsonl
├── paper_db.jsonl
├── selected_papers.md
├── papers/
├── reading_notes.md
├── synthesis.md
├── gaps.md
└── references.bib
```

## Phase 1: Scope the Review

- Write one paragraph defining the review question.
- Record time window, venues, source databases, and exclusion rules.
- Decide whether the goal is related-work support, survey drafting, or general topic orientation.

Deliverable:
- `outputs/<topic-slug>/selected_papers.md` can start as a short scoping note.

## Phase 2: Search and Collect

- Use `scripts/search_semantic_scholar.py` for broad discovery.
- Use `scripts/search_arxiv.py` to capture recent preprints and uncited work.
- Save each raw query result separately under `search_results/`.

Typical commands:

```bash
python skills/systematic-review/scripts/search_semantic_scholar.py \
  --query "topic" \
  --max-results 50 \
  --api-key "$S2_API_KEY" \
  -o outputs/<topic-slug>/search_results/s2.jsonl

python skills/systematic-review/scripts/search_arxiv.py \
  --query "topic" \
  --max-results 30 \
  -o outputs/<topic-slug>/search_results/arxiv.jsonl
```

## Phase 3: Merge and Prioritize

- Merge raw results into one corpus with `scripts/paper_db.py merge`.
- Remove duplicates and weak hits.
- Rank by relevance, venue quality, citations, and recency.
- Select 8-15 papers for close reading.

Deliverables:
- `outputs/<topic-slug>/paper_db.jsonl`
- `outputs/<topic-slug>/selected_papers.md`

## Phase 4: Read in Depth

- Download PDFs with `scripts/download_papers.py` if needed.
- For each core paper, capture:
  - problem and setting
  - method or taxonomy slot
  - datasets, baselines, metrics
  - main results
  - limitations
  - code and benchmark links
- Use `note-format.md` so downstream writing stays consistent.

Deliverable:
- `outputs/<topic-slug>/reading_notes.md`

## Phase 5: Synthesize

- Group papers into themes rather than by publication date alone.
- Build comparison tables, trend summaries, and contradiction notes.
- Separate confirmed findings from open questions.

Deliverables:
- `outputs/<topic-slug>/synthesis.md`
- `outputs/<topic-slug>/gaps.md`

## Phase 6: Export Writing Inputs

- Generate BibTeX from the curated corpus.
- Pass the artifacts to `literature-review`, `related-work-writing`, `survey-generation`, or `citation-management`.

Typical command:

```bash
python skills/systematic-review/scripts/bibtex_manager.py \
  --jsonl outputs/<topic-slug>/paper_db.jsonl \
  --output outputs/<topic-slug>/references.bib
```

## Quality Gates

- The corpus should include both foundational and recent papers.
- Preprints must be explicitly marked as such when they influence the writing.
- Every synthesized claim should be traceable to at least one item in `paper_db.jsonl`.
- If the corpus is sparse or contradictory, record that explicitly in `gaps.md`.
