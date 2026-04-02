---
name: manuscript-scorecard
description: Score a paper draft across problem framing, literature grounding, methodology, data, analysis, results, writing, and citations, then track revision progress with a repeatable scorecard. Use when you need a quantitative readiness snapshot rather than only free-form review comments.
argument-hint: [draft-or-scores]
---

# Manuscript Scorecard

Use this skill when the draft needs a structured numeric diagnostic that can be compared across revisions, coauthors, or venue targets.

## When to Use

- The team wants a 1-5 score by dimension instead of only narrative feedback
- You need to compare draft quality before and after revision
- The manuscript already exists, but readiness for submission is still unclear

For conference-style review text, use `self-review` or `review-ensemble`.
For methodological stress testing, use `claim-rigor-audit`.

## Workflow

### Step 1: Choose the Scope
- Decide whether the scorecard covers the full manuscript, one section, or a review package.
- Keep the scoring target stable if you plan to compare versions over time.

### Step 2: Score the Core Dimensions
- Score each dimension from 1 to 5:
  - `problem_formulation`
  - `literature_review`
  - `methodology`
  - `data_collection`
  - `analysis`
  - `results`
  - `writing`
  - `citations`
- Attach short evidence notes for every score instead of rating by intuition alone.

### Step 3: Aggregate
- Use the score calculator for a weighted overall score.
- Identify top strengths and weakest dimensions immediately.
- Keep the raw dimension scores, not only the final average.

### Step 4: Interpret
- Translate weak dimensions into concrete revision priorities.
- Compare the score profile against the target venue and draft stage.
- Treat a high score in one dimension as non-compensation for major weakness in another.

### Step 5: Track Revision Progress
- Save each revision's score JSON and report.
- Re-score after substantial changes, not after minor copyedits.
- Compare deltas per dimension to see whether revisions actually improved the draft.

## Scripts

### Calculate a weighted score report
```bash
python skills/manuscript-scorecard/scripts/calculate_scores.py \
  --scores manuscript_scores.json --output manuscript_scorecard.txt
```

### Interactive scoring
```bash
python skills/manuscript-scorecard/scripts/calculate_scores.py --interactive
```

## References

- `references/dimensions.md`: what each score dimension means and how to judge it
- `references/score-interpretation.md`: thresholds, weighting logic, and progress tracking rules

## Rules

- Every numeric score must be backed by evidence from the draft.
- Do not let polished writing hide weak methodology or weak evidence.
- Preserve dimension-level scores so later revisions can be compared fairly.
- Use the scorecard to prioritize revision, not to replace reasoning.

## Related Skills

- Upstream: [self-review](../self-review/), [review-ensemble](../review-ensemble/), [claim-rigor-audit](../claim-rigor-audit/)
- Downstream: [paper-revision](../paper-revision/), [rebuttal-writing](../rebuttal-writing/)
- See also: [venue-submission-strategy](../venue-submission-strategy/)
