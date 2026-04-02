# Anti-Patterns

This skill is for manuscripts that compile successfully but still look under-edited.

## 1. Wall of Bullets

Problem:

- Section after section is written as bullets instead of argument-driven prose.

Fix:

- Convert explanatory content into paragraphs.
- Keep bullets only for genuinely parallel items, short inventories, or compact reference material.

## 2. `\newpage` Abuse

Problem:

- Every section starts on a fresh page, leaving large blank regions.

Fix:

- Let LaTeX handle routine page breaks.
- Reserve `\newpage` for major transitions such as front matter, appendices, or unusual layout constraints.

## 3. Oversized Figures and Rigid Floats

Problem:

- Figures occupy nearly full page width and force whitespace around them.

Fix:

- Default to about `0.75\textwidth` to `0.85\textwidth`.
- Prefer `[htbp]` over `[H]`.

## 4. No List Compaction

Problem:

- Even short lists consume too much vertical space in long manuscripts.

Fix:

- Add `enumitem` compaction in the preamble for long papers.

## 5. Monotonous Section Structure

Problem:

- Every subsection uses the same presentation pattern, making the paper feel generated.

Fix:

- Alternate among prose, tables, bold-label paragraphs, figures, and callout boxes when appropriate.

## 6. Silent Text-Mode Encoding Errors

Problem:

- The PDF renders broken symbols even though the manuscript compiles.

Fix:

- Escape or rewrite raw `<`, `>`, `~`, `|`, `\`, `{`, and `}` when they are meant as text.

## 7. False Paragraph Starts After Display Math

Problem:

- Text after an equation is indented as if it starts a new paragraph.

Fix:

- Use `\noindent` when the sentence after the display math is a continuation.
