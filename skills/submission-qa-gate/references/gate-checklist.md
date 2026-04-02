# Gate Checklist

Use this sequence right before internal sign-off, arXiv upload, or venue submission.

## 1. Budget

- Does the manuscript still fit the page or word budget?
- Are appendix pages being counted correctly for the target venue?
- Did a recent revision add a figure or table that changed the layout materially?

## 2. Structural Hygiene

- No `TODO`, `FIXME`, `TBD`, `XXX`, or placeholder citations
- Figures and tables have captions and labels
- Key labels are referenced from the body text
- Required sections are present and not obviously skeletal

## 3. Citation Integrity

- Every `\cite{}` resolves
- `.bib` file matches the current manuscript
- No hallucinated or irrelevant bibliography entries remain
- Figure files referenced in LaTeX exist on disk

## 4. Environment Readiness

- Required document class and packages are available
- Venue-specific formatting checks pass
- Anonymous submission requirements are satisfied when relevant

## 5. Compile State

- Clean compile or only understood, acceptable warnings
- Bibliography and cross-references fully resolved
- Final PDF reviewed visually, not just compiled

## Output Format

Keep a short gate note:

```text
QA Gate: PASS / WARN / FAIL
Budget:
Citation integrity:
Labels and refs:
Compile:
Manual follow-up:
```
