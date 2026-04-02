# Review Workflow

This workflow is distilled from `ai_scientist/perform_review.py`.

## 1. Independent Reviews

- Generate multiple reviews from the same manuscript.
- Keep the schema fixed so the outputs can be aggregated cleanly.
- Use a skeptical reviewer stance by default.

## 2. Meta-Review

- Aggregate the independent reviews into a single review object.
- Preserve consensus strengths and consensus weaknesses.
- If the meta-review step fails, fall back to the strongest valid individual review rather than returning nothing.

## 3. Score Aggregation

- Average numerical fields such as originality, quality, clarity, significance, soundness, presentation, contribution, overall, and confidence.
- Round scores only after validating they fall within the allowed range.

## 4. Reflection

- Revisit the review 1-3 times.
- Ask whether the review is accurate, sound, and clear.
- If nothing changes, stop; repeated stylistic edits do not improve the review.

## 5. Improvement Hook

Once the final review is stable:

- Convert weaknesses into concrete manuscript edits
- Convert questions into rebuttal targets
- Convert low-score dimensions into prioritized revision buckets

This is the bridge from review generation to `paper-revision` and `rebuttal-writing`.
