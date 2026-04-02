# Review Uses

Redline PDFs are most useful when the manuscript has already changed and you need evidence of what changed, not just a promise that something changed.

## Best Uses

- Advisor or coauthor review after a substantial revision
- Author response preparation, where each reviewer concern maps to concrete text or figure changes
- Internal release checks before resubmission or camera-ready upload

## Suggested Workflow

1. Revise the clean manuscript in `paper-revision`.
2. Generate a redline against the last stable baseline.
3. Check whether the diff actually shows the intended fix in the relevant section.
4. Cite the changed section, figure, or table in `rebuttal-writing`.

## What to Look For

- Did the intended clarification really land in the right section?
- Did you accidentally change unrelated wording near the targeted fix?
- Did a table, caption, or equation move in a way that needs separate explanation?
- Are all claimed changes in the rebuttal visible in the redline?

## What Not to Do

- Do not send a redline as the only response artifact when reviewers need a clean rebuttal summary.
- Do not assume `latexdiff` perfectly communicates semantic change for every equation or float.
- Do not diff against an unstable working copy if an official revision baseline exists.
