# API and Script Reference

This skill ships with repository-local scripts for the most common literature-review tasks.

## Semantic Scholar

Base URL:

```text
https://api.semanticscholar.org/graph/v1
```

Recommended script:

```bash
python skills/systematic-review/scripts/search_semantic_scholar.py \
  --query "reasoning agents" \
  --max-results 50 \
  --year-range 2022-2026 \
  --api-key "$S2_API_KEY" \
  -o outputs/reasoning-agents/search_results/s2.jsonl
```

Notes:
- `S2_API_KEY` is optional but recommended for better rate limits.
- The script supports citation filtering, venue filtering, and peer-reviewed-only retrieval.

## arXiv

Base URL:

```text
http://export.arxiv.org/api/query
```

Recommended script:

```bash
python skills/systematic-review/scripts/search_arxiv.py \
  --query "reasoning agents" \
  --max-results 30 \
  --categories cs.AI cs.CL cs.LG \
  --sort-by submittedDate \
  -o outputs/reasoning-agents/search_results/arxiv.jsonl
```

Notes:
- Use arXiv to capture very recent work and missing preprints.
- Treat arXiv papers as preprints unless a peer-reviewed venue is confirmed separately.

## Corpus Utilities

Merge and deduplicate:

```bash
python skills/systematic-review/scripts/paper_db.py merge \
  --inputs outputs/reasoning-agents/search_results/*.jsonl \
  --output outputs/reasoning-agents/paper_db.jsonl
```

Download PDFs:

```bash
python skills/systematic-review/scripts/download_papers.py \
  --jsonl outputs/reasoning-agents/paper_db.jsonl \
  --output-dir outputs/reasoning-agents/papers/
```

Extract PDF text:

```bash
python skills/systematic-review/scripts/extract_pdf.py \
  --pdf-dir outputs/reasoning-agents/papers/ \
  --output-dir outputs/reasoning-agents/text/
```

Generate BibTeX:

```bash
python skills/systematic-review/scripts/bibtex_manager.py \
  --jsonl outputs/reasoning-agents/paper_db.jsonl \
  --output outputs/reasoning-agents/references.bib
```

Compile a Markdown review package:

```bash
python skills/systematic-review/scripts/compile_report.py \
  --topic-dir outputs/reasoning-agents/
```

## Reading Options

- For local PDFs, use the repository scripts or native PDF reading tools.
- For arXiv HTML access, use `https://ar5iv.labs.arxiv.org/html/<arxiv_id>` when available.
- When a paper is only available as a preprint, record that status in your notes and citations.
