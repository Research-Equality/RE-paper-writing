# Quality Checks

Use these checks during the writeup loop before and after compilation.

## Bibliography Checks

- Every `\cite{}` key must exist in the bibliography block or `.bib` file.
- Do not add a new citation from memory.
- If a citation exists under a different key, normalize the manuscript to that key instead of duplicating entries.

## Figure Checks

- Every referenced figure file must exist.
- Remove duplicate figure insertions unless the duplication is truly intentional.
- Replace placeholder captions and labels with meaningful ones.

## Structural Checks

- No duplicate section headers.
- No broken environment closures like `</end{figure}>`.
- No repeated labels, repeated captions, or repeated prose blocks.
- Escape unsafe characters such as underscores in plain text.

## Evidence Checks

- All numerical claims must come from actual logs, tables, or saved result files.
- Missing evidence means weaken or remove the claim.
- Ensure notes and saved findings are reflected in the manuscript if they matter.

## Compile Loop

Recommended order:

1. Lint or run `chktex`
2. Fix the smallest concrete errors first
3. Run `pdflatex -> bibtex -> pdflatex -> pdflatex`
4. Re-check warnings and unresolved references

Keep the fix minimal. Avoid large rewrites while debugging LaTeX syntax.
