---
name: long-form-manuscript-polish
description: Polish long-form LaTeX manuscripts by removing slide-like bullet walls, float and page-break anti-patterns, silent text-mode encoding issues, and monotonous section structure. Use when a 5+ page draft compiles but still reads like notes, slides, or an LLM dump.
argument-hint: [draft-or-main-tex]
---

# Long-Form Manuscript Polish

Turn a technically complete draft into a professional long-form manuscript.

## When to Use

- The draft is 5 or more pages and feels outline-like rather than paper-like
- Section after section falls back to bullets instead of prose
- Figures, tables, or page breaks create whitespace and visual instability
- The manuscript compiles, but the result still looks obviously machine-generated or under-edited

## Workflow

### Step 1: Audit the Document Rhythm
- Count how often sections rely on `itemize` or `enumerate`.
- Note repeated section patterns such as intro sentence -> bullet list -> bold takeaway.
- Identify places where prose should carry the argument instead of list structure.

### Step 2: Replace Slide-Like Structure
- Convert bullet walls into prose paragraphs or bold-label paragraphs.
- Use tables for real comparisons, not long bullet lists of structured facts.
- Vary adjacent section formats so the paper does not repeat the same visual rhythm throughout.

### Step 3: Fix Layout Anti-Patterns
- Remove `\newpage` before routine sections and subsections.
- Default figure widths to about `0.75\textwidth` to `0.85\textwidth`.
- Prefer `[htbp]` over `[H]` unless exact placement is truly required.
- Add global list compaction and widow-orphan penalties for longer manuscripts.

### Step 4: Catch Silent Text-Mode Issues
- Search for `<`, `>`, `~`, `|`, `\`, `{`, and `}` used as plain text.
- Check text immediately after display math; add `\noindent` when the paragraph is continuing rather than restarting.
- Watch for long manuscripts that compile successfully but still render broken symbols or awkward paragraph breaks.

### Step 5: Run Final Polish Checks
- Confirm that prose is the default and lists are the exception.
- Confirm that neighboring sections do not all use the same presentation pattern.
- After polish, run `submission-qa-gate` and then venue-facing LaTeX checks.

## Rules

- In a paper, prose is the default. Lists are exceptions.
- Do not keep bullets just because they are easy to generate.
- Do not use oversized figures or rigid float placement to force layout.
- A long manuscript should feel authored, not assembled from repeated templates.

## References

- High-impact anti-patterns for 5+ page drafts: `references/anti-patterns.md`
- Final polish checklist before submission QA: `references/polish-checklist.md`

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [survey-generation](../survey-generation/), [paper-writing-section](../paper-writing-section/)
- Downstream: [submission-qa-gate](../submission-qa-gate/), [latex-formatting](../latex-formatting/), [paper-compilation](../paper-compilation/)
- See also: [paper-schematics](../paper-schematics/), [paper-revision](../paper-revision/), [reverse-outline-flow-check](../reverse-outline-flow-check/)
