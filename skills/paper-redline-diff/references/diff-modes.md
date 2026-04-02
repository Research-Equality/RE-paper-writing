# Diff Modes

Use `paper-redline-diff` to create change-tracked LaTeX outputs from either:

- two explicit `.tex` versions
- the current working tree versus a git revision
- a multi-file manuscript flattened through `\input{}` or `\include{}`

## Comparison Modes

### File-to-file

Use when old and new drafts live in different folders:

```bash
bash skills/paper-redline-diff/scripts/latex_diff.sh \
  old/main.tex new/main.tex --flatten --compile
```

### Git baseline

Use when the baseline is a prior commit, tag, or branch:

```bash
bash skills/paper-redline-diff/scripts/latex_diff.sh \
  paper/main.tex --git-rev HEAD~1 --compile
```

Good baseline examples:

- `HEAD~1`: previous local revision
- `submission-v1`: prior official submission tag
- `camera-ready-base`: pre-revision branch

## Markup Types

- `UNDERLINE`: balanced default; readable inline additions and deletions
- `CTRADITIONAL`: traditional colored text changes
- `CHANGEBAR`: margin bars with less inline clutter
- `CULINECHBAR`: strongest audit mode for revision packages
- `INVISIBLE`: debug mode only

## Practical Guidance

- Use `--flatten` for multi-file papers so section moves and inserted paragraphs show up correctly.
- Use `--compile` whenever the diff will be shared with someone else.
- Use `--color-add` and `--color-del` only if the receiving reviewer has specific print or accessibility constraints.
- If the diff becomes unreadable around equations or floats, keep the redline for audit and explain the change in prose alongside it.
