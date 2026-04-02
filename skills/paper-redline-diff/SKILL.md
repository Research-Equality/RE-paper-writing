---
name: paper-redline-diff
description: Generate change-tracked LaTeX manuscript diffs between two files or between the working draft and a git revision. Use when the user needs a redline PDF for advisor review, revision verification, or rebuttal support.
argument-hint: [main-tex-or-old/new]
---

# Paper Redline Diff

Create reviewer-readable redline artifacts for manuscript revisions.

## When to Use

- The paper has gone through a revision and you need to show exactly what changed
- An advisor, collaborator, or reviewer needs a change-tracked PDF rather than a prose summary
- You want to compare the current draft against a tagged submission, prior commit, or alternate branch

## Scripts

### Generate a diff between two `.tex` files
```bash
bash skills/paper-redline-diff/scripts/latex_diff.sh \
  old/main.tex new/main.tex --flatten --compile
```

### Diff the current draft against a git revision
```bash
bash skills/paper-redline-diff/scripts/latex_diff.sh \
  paper/main.tex --git-rev HEAD~1 --compile
```

### Use a more review-friendly markup mode
```bash
bash skills/paper-redline-diff/scripts/latex_diff.sh \
  paper/main.tex --git-rev v1.0 --type CULINECHBAR --compile
```

## Workflow

### Step 1: Choose the Baseline
- Use file-to-file mode when the old and new drafts live in separate directories.
- Use `--git-rev` when the authoritative baseline is a commit, tag, or branch.
- Use `--flatten` for multi-file projects with `\input{}` or `\include{}` so the diff reflects the real manuscript, not only the top-level file.

### Step 2: Pick the Markup Style
- `UNDERLINE`: good default for advisor review
- `CHANGEBAR`: useful when inline markup becomes too noisy
- `CULINECHBAR`: strongest option for revision audits and rebuttal support

See `references/diff-modes.md` before choosing a mode for external circulation.

### Step 3: Compile and Inspect
- Generate `diff_*.tex`, then compile to PDF.
- Verify that section headings, equations, tables, and citations are still readable in the diff output.
- If the manuscript changed structurally, scan for places where `latexdiff` produced awkward markup around floats or math.

### Step 4: Use the Diff as Evidence
- Pair the redline with the prose change summary from `paper-revision`.
- Use exact section, table, or figure references from the diff when writing `rebuttal-writing`.
- Keep the redline artifact separate from the clean submission PDF.

## Rules

- Diff against a real prior draft, commit, or tagged submission, not an imagined baseline.
- Do not treat the redline as the paper itself; it is a review artifact.
- If `latexdiff` makes a region unreadable, note that explicitly and fall back to a concise prose explanation for that change.
- Prefer git-tag or commit baselines for official revision rounds so the comparison is reproducible.

## References

- Diff modes and command patterns: `references/diff-modes.md`
- How to use redlines in revision and rebuttal loops: `references/review-uses.md`

## Related Skills

- Upstream: [paper-revision](../paper-revision/), [latex-writeup-loop](../latex-writeup-loop/)
- Downstream: [rebuttal-writing](../rebuttal-writing/)
- See also: [submission-qa-gate](../submission-qa-gate/), [paper-compilation](../paper-compilation/), [latex-formatting](../latex-formatting/)
