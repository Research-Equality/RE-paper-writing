---
name: source-material-ingestion
description: Convert PDFs, DOCX, PPTX, XLSX, and other source documents into Markdown so papers, reviews, supplementary files, and reviewer materials become searchable writing inputs. Use when manuscript evidence lives in documents instead of clean text files.
argument-hint: [input-files-or-directory]
---

# Source Material Ingestion

Use this skill when the writing bottleneck is not prose generation but getting source documents into a format that can be searched, quoted carefully, and fed into downstream paper-writing workflows.

## When to Use

- The project includes PDFs, Word docs, slide decks, spreadsheets, scanned images, or mixed source files
- You need to mine reviewer comments, prior drafts, notes, or appendices before rewriting the paper
- Literature or project artifacts need to become Markdown so later skills can work on them reliably

For bibliography repair, use `citation-management`.
For manuscript drafting, use `ml-paper-writing` or `paper-writing-section`.

## Workflow

### Step 1: Inventory the Inputs
- Separate papers, drafts, reviewer files, tables, and slide decks.
- Decide which files are evidence sources and which are just presentation artifacts.
- Keep the original files unchanged.

### Step 2: Route by Format
- Use the converter workflow for PDFs, DOCX, PPTX, and XLSX first.
- Treat scanned or OCR-heavy files as low-trust until manually checked.
- Preserve provenance: source filename, conversion time, and any guessed metadata.

### Step 3: Convert to Markdown
- Write converted outputs outside the skill directory, usually under a project-local folder such as `sources/converted/` or `outputs/<topic-slug>/source_materials/`.
- Normalize headings, tables, and front matter so later search and note-taking stay predictable.
- Generate an index or catalog if the file set is large.

### Step 4: Clean for Downstream Use
- Remove boilerplate, broken page headers, or OCR noise that would mislead later writing.
- Check that tables and equations survived conversion in a usable form.
- Split very large converted files only after preserving a master copy.

### Step 5: Hand Off
- Feed converted Markdown into `literature-review`, `systematic-review`, `self-review`, `paper-revision`, or `ml-paper-writing`.
- Keep a clear mapping from converted Markdown back to the original source file.

## Scripts

### Batch-convert literature and project documents
```bash
python skills/source-material-ingestion/scripts/convert_literature.py \
  papers/ outputs/topic/source_materials/ --recursive --create-index
```

Key flags: `--organize-by-year`, `--recursive`, `--create-index`

## References

- `references/ingestion-workflow.md`: routing, provenance, cleanup, and storage conventions
- `references/format-routing.md`: what to expect from each source file type

## Rules

- Never treat OCR output or table extraction as trustworthy until spot-checked.
- Preserve the original file and the converted Markdown together.
- Record provenance in the converted file front matter.
- Do not write converted artifacts into the skill directory.

## Related Skills

- Upstream: [literature-search](../literature-search/), [systematic-review](../systematic-review/)
- Downstream: [literature-review](../literature-review/), [citation-management](../citation-management/), [ml-paper-writing](../ml-paper-writing/), [self-review](../self-review/)
- See also: [paper-revision](../paper-revision/), [experiment-report-bridge](../experiment-report-bridge/)
