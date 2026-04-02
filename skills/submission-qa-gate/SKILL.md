---
name: submission-qa-gate
description: Run a deterministic pre-submission QA gate on a LaTeX manuscript, covering word and page budget, TODO markers, label hygiene, citation coverage, lint, and compile readiness. Use immediately before internal circulation, arXiv upload, or venue submission.
argument-hint: [main-tex-path]
---

# Submission QA Gate

Run the last mechanical checks before the manuscript leaves the writing loop.

## When to Use

- The draft is content-complete and you want a pass or fail gate before submission
- You need a repeatable checklist for coauthor handoff, advisor sign-off, or camera-ready prep
- The paper compiles, but you still want to catch latent issues such as TODO markers, broken cite keys, or labeling gaps

For build failures themselves, use `paper-compilation`.

## Core Commands

### Citation and figure validation
```bash
python skills/citation-management/scripts/validate_citations.py \
  --tex paper/main.tex --bib paper/references.bib --check-figures
```

### Venue-facing LaTeX checks
```bash
python skills/latex-formatting/scripts/latex_checker.py \
  paper/main.tex --venue neurips --check-anon
```

### Full compile and style pass
```bash
python skills/paper-compilation/scripts/compile_paper.py \
  paper/main.tex --check-style
```

### Fast unresolved-marker scan
```bash
rg -n 'TODO|FIXME|TBD|XXX' paper
```

## Workflow

### Step 1: Budget and Inventory
- Confirm that word count, page count, figures, tables, and appendix usage still fit the target venue.
- Record the manuscript inventory in a short gate report so later revisions can be compared.

### Step 2: Structural Hygiene
- Remove all `TODO`, `FIXME`, `TBD`, and placeholder markers.
- Check that figures and tables have labels and that important labels are referenced.
- Confirm that the essential paper sections are present and not empty.

### Step 3: Citation Integrity
- Run citation validation against the active `.bib`.
- If citations are missing or suspicious, route through `citation-management` and `citation-verification-gate` before continuing.
- Treat unused or placeholder bibliography entries as a cleanup task, not a cosmetic issue.

### Step 4: Environment and Compile Readiness
- Verify that the document class and required packages are available.
- Run lint and then a full compile pass.
- Treat compilation warnings as actionable if they may affect references, floats, or bibliography output.

### Step 5: Gate Decision
Produce a concise decision:

```text
PASS / WARN / FAIL
- budget
- citation integrity
- labels and refs
- unresolved markers
- compile status
- remaining manual checks
```

## Rules

- A clean compile alone is not enough to pass the gate.
- Any unresolved marker, missing cite key, or missing figure file is a gate failure.
- If the target venue matters, check against that venue explicitly rather than using a generic style pass.
- Prefer a short written gate report over a vague statement that the paper is "ready."

## References

- Gate sequence and what each check should answer: `references/gate-checklist.md`
- Common fail patterns and how to classify them: `references/common-failures.md`

## Related Skills

- Upstream: [latex-writeup-loop](../latex-writeup-loop/), [paper-evidence-verifier](../paper-evidence-verifier/), [citation-management](../citation-management/)
- Downstream: [paper-compilation](../paper-compilation/), [self-review](../self-review/)
- See also: [latex-formatting](../latex-formatting/), [citation-verification-gate](../citation-verification-gate/), [paper-redline-diff](../paper-redline-diff/)
