---
name: review-ensemble
description: Generate strict conference-style paper reviews using multiple independent reviews, meta-review aggregation, score averaging, and optional review-guided improvement. Use when the user wants a committee-like review signal rather than a single-pass critique.
argument-hint: [pdf-or-draft]
---

# Review Ensemble

Use this skill when one review is not enough and the goal is a more stable, committee-like assessment.

## When to Use

- The user wants a harsher or more reliable pre-submission review
- A draft needs multiple independent review perspectives before revision
- The task includes turning review output into a meta-review or revision brief

For a lighter single-skill pre-submission check, use `self-review`.

## Workflow

### Step 1: Load the Paper
- Read the LaTeX source directly when available.
- If the draft is a PDF, extract enough text to review the manuscript reliably.

### Step 2: Generate Independent Reviews
- Produce 3-5 reviews independently using the same review schema.
- Encourage diversity in reasoning, not randomness in formatting.
- Keep the reviewer standard skeptical rather than generous.

### Step 3: Aggregate
- Build a meta-review that finds consensus and major disagreements.
- Average valid numerical scores across reviewers.
- Keep the final decision binary if the downstream workflow requires that.

### Step 4: Reflect
- Run 1-3 reflection passes on the aggregated review.
- Stop when the review stabilizes; do not keep editing for style alone.

### Step 5: Hand Off to Revision
- Convert the final weaknesses and questions into a revision plan.
- Use `paper-revision` for manuscript changes and `rebuttal-writing` for author response.

## References

- `references/review-schema.md`: the structured review fields and score scales
- `references/review-workflow.md`: ensemble, meta-review, and improvement loop

## Rules

- Be critical and explicit about limited evidence, weak baselines, and missing reproducibility details.
- Separate summary from criticism cleanly.
- If reviewers disagree, preserve the disagreement rather than smoothing it away.
- Confidence should reflect actual certainty, not presentation quality.

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [paper-compilation](../paper-compilation/)
- Downstream: [paper-revision](../paper-revision/), [rebuttal-writing](../rebuttal-writing/)
- See also: [self-review](../self-review/), [paper-evidence-verifier](../paper-evidence-verifier/), [reporting-guidelines-check](../reporting-guidelines-check/), [venue-submission-strategy](../venue-submission-strategy/), [claim-rigor-audit](../claim-rigor-audit/), [manuscript-scorecard](../manuscript-scorecard/)
