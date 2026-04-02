# Format Routing

## PDF

- Best for: published papers, reviewer PDFs, supplementary documents
- Watch for: broken columns, headers, footers, equations, OCR failures

## DOCX

- Best for: collaborator drafts, reviewer responses, proposal text
- Watch for: comments, tracked changes, tables with merged cells

## PPTX

- Best for: talk decks that explain system architecture or experiment narrative
- Watch for: speaker notes, text split across shapes, image-only slides

## XLSX

- Best for: result tables, study logs, metadata sheets
- Watch for: hidden sheets, formulas vs rendered values, merged cells

## Images and Scans

- Best for: diagrams or scanned notes only when no source text exists
- Watch for: OCR hallucinations, lost symbols, poor small-text recovery

## Routing Rule

- If the source will be used as factual evidence, prefer the cleanest textual original available.
- If both PDF and DOCX exist, prefer DOCX for text and PDF for layout verification.
- If spreadsheets hold official numbers, later cross-check them with `paper-evidence-verifier` before those numbers enter the manuscript.
