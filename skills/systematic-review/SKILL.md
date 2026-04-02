---
name: systematic-review
description: Conduct a systematic academic literature review for paper writing. Build a shared paper corpus, read core papers in depth, synthesize themes and gaps, and export structured notes plus BibTeX. Use when the user needs a rigorous literature foundation before writing related work or a survey.
argument-hint: [topic]
---

# Systematic Review

Run a reproducible literature-review workflow that produces reusable artifacts for paper writing.

## Input

- `$0` — Topic, research question, or review scope
- Optional: venue range, year range, seed papers, or inclusion criteria

## Shared Artifacts

Write outputs under `outputs/<topic-slug>/`:

```text
outputs/<topic-slug>/
├── search_results/
├── paper_db.jsonl
├── reading_notes.md
├── synthesis.md
├── gaps.md
└── references.bib
```

## Scripts

### Search Semantic Scholar
```bash
python skills/systematic-review/scripts/search_semantic_scholar.py \
  --query "long-context reasoning agents" \
  --max-results 50 \
  --year-range 2022-2026 \
  --api-key "$S2_API_KEY" \
  -o outputs/long-context-reasoning-agents/search_results/s2.jsonl
```

### Search arXiv
```bash
python skills/systematic-review/scripts/search_arxiv.py \
  --query "long-context reasoning agents" \
  --max-results 30 \
  --categories cs.AI cs.CL cs.LG \
  -o outputs/long-context-reasoning-agents/search_results/arxiv.jsonl
```

### Merge, filter, and inspect the corpus
```bash
python skills/systematic-review/scripts/paper_db.py merge \
  --inputs outputs/long-context-reasoning-agents/search_results/*.jsonl \
  --output outputs/long-context-reasoning-agents/paper_db.jsonl
```

### Download papers and export BibTeX
```bash
python skills/systematic-review/scripts/download_papers.py \
  --jsonl outputs/long-context-reasoning-agents/paper_db.jsonl \
  --output-dir outputs/long-context-reasoning-agents/papers/

python skills/systematic-review/scripts/bibtex_manager.py \
  --jsonl outputs/long-context-reasoning-agents/paper_db.jsonl \
  --output outputs/long-context-reasoning-agents/references.bib
```

## Workflow

### Step 1: Define Scope
- Write down the research question, target venues, date range, and inclusion or exclusion rules.
- Prefer peer-reviewed conference and journal papers; keep recent preprints as supplemental evidence.

### Step 2: Collect a Broad Paper Set
- Search Semantic Scholar first, then arXiv for the most recent work.
- Save raw results under `search_results/`.
- Merge and deduplicate into `paper_db.jsonl`.

### Step 3: Prioritize the Reading List
- Rank papers by relevance, venue quality, citation impact, and recency.
- Select 8-15 papers for close reading.
- Track why each selected paper matters.

### Step 4: Read and Annotate
- Extract problem setting, method, datasets, baselines, main results, limitations, and code links.
- Use `references/note-format.md` for note structure.
- Keep citations grounded in the source text; do not infer unsupported claims.

### Step 5: Synthesize
- Build a taxonomy of approaches.
- Identify agreements, contradictions, missing evaluations, and open problems.
- Produce reusable artifacts for downstream writing: `reading_notes.md`, `synthesis.md`, and `gaps.md`.

### Step 6: Export Writing Inputs
- Generate `references.bib`.
- Use the resulting corpus with `literature-review`, `related-work-writing`, `survey-generation`, and `citation-management`.

## Rules

- Keep search results, notes, and synthesized outputs in `outputs/<topic-slug>/`, not inside the skill directory.
- Prefer peer-reviewed sources when claims conflict; mark arXiv work as preprints when cited.
- Every factual claim in synthesized notes must be traceable to at least one paper in `paper_db.jsonl`.
- Do not fabricate citation keys, venues, metrics, or benchmark results.
- If the evidence base is thin, say so explicitly and record the gap.

## References

- Workflow detail: `references/workflow-phases.md`
- Note templates: `references/note-format.md`
- API and script guide: `references/api-reference.md`

## Related Skills

- Downstream: [literature-review](../literature-review/), [citation-management](../citation-management/), [related-work-writing](../related-work-writing/), [survey-generation](../survey-generation/)
- See also: [literature-search](../literature-search/), [research-planning](../research-planning/), [reporting-guidelines-check](../reporting-guidelines-check/), [source-material-ingestion](../source-material-ingestion/), [claim-rigor-audit](../claim-rigor-audit/)
