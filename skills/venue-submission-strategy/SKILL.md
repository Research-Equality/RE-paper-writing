---
name: venue-submission-strategy
description: Align a manuscript to the expectations of a target journal or conference, including venue fit, reviewer priorities, page budget, anonymization, and template choice. Use when the target venue materially changes how the paper should be framed or packaged.
argument-hint: [target-venue-or-family]
---

# Venue Submission Strategy

Use this skill when the important question is not only "can the paper compile?" but "is this actually written for the venue that will judge it?"

## When to Use

- The target journal or conference is known, or the user is choosing between candidate venues
- The same results could be framed differently for different reviewer cultures
- Page limits, anonymization, abstract style, or appendix policy affect what belongs in the main paper

For mechanical LaTeX fixes, use `latex-formatting`.
For post-review editing, use `paper-revision` and `rebuttal-writing`.

## Workflow

### Step 1: Identify the Venue Family
- Classify the target as high-impact journal, specialist journal, ML conference, medical journal, HCI venue, survey venue, or other relevant family.
- Determine whether the venue optimizes for broad significance, mechanistic depth, experimental rigor, or application relevance.

### Step 2: Lock Constraints Early
- Record page limits, anonymization rules, supplementary policy, abstract structure, and figure allowances.
- Decide the working template and document structure before heavy drafting begins.
- Separate hard constraints from style preferences.

### Step 3: Reframe the Contribution
- Rewrite the one-sentence contribution in the venue's language.
- Adjust the abstract, title, introduction opening, and Figure 1 so they answer the venue's first-pass question.
- Remove claims that are too broad for the evidence or too narrow for the venue.

### Step 4: Budget the Main Paper
- Decide what stays in the main paper versus appendix or supplement.
- Protect the space needed for the evidence that the venue cares about most.
- If the venue is double-blind, audit all author-identifying text, URLs, acknowledgments, and repository references.

### Step 5: Pre-Submission Risk Check
- List the most likely reviewer objections for this venue.
- Check whether the current draft already answers them in the main paper.
- Hand off to `latex-formatting`, `self-review`, or `review-ensemble` once the submission strategy is stable.

## References

- `references/venue-families.md`: how major venue families differ in scope and document norms
- `references/reviewer-priorities.md`: what reviewers commonly optimize for by venue family
- `references/page-budget.md`: how to allocate scarce main-paper space

## Rules

- Venue fit is a writing decision before it becomes a formatting decision.
- Do not wait until the end to discover that the main paper is solving the wrong reviewer question.
- Keep the strongest evidence in the main paper for the venue's dominant evaluation criteria.
- If the venue is uncertain, state the assumed family and write against that assumption explicitly.

## Related Skills

- Upstream: [research-planning](../research-planning/), [ml-paper-writing](../ml-paper-writing/)
- Downstream: [latex-formatting](../latex-formatting/), [self-review](../self-review/), [review-ensemble](../review-ensemble/), [rebuttal-writing](../rebuttal-writing/)
- See also: [reporting-guidelines-check](../reporting-guidelines-check/), [paper-writing-section](../paper-writing-section/)
