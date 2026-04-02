# Ingestion Workflow

## Recommended Output Layout

Use project-local output folders rather than writing into the skill directory.

Examples:

```text
sources/
  converted/
    INDEX.md
    catalog.json
    smith_2024_paper.md
```

or

```text
outputs/<topic-slug>/
  source_materials/
    INDEX.md
    paper_a.md
    notes_b.md
```

## Minimal Provenance

Every converted Markdown file should preserve:

- original filename
- conversion timestamp
- guessed or extracted title
- guessed author and year when available
- path or folder context if multiple source bundles are mixed

## Cleanup Priorities

1. Remove repeated headers and footers
2. Check that section headings are still recognizable
3. Fix broken tables that will later be cited or summarized
4. Mark OCR-heavy regions as low confidence
5. Keep a master converted file before chunking

## Best Uses

- prior paper drafts
- reviewer PDFs or response letters
- supplementary methods
- slide decks that contain figure explanations
- spreadsheets that need table-to-text conversion before synthesis
