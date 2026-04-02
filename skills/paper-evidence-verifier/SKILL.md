---
name: paper-evidence-verifier
description: Verify that every quantitative claim in a draft is grounded in real experiment artifacts, flag fabricated conditions or unsupported numbers, and sanitize result tables when needed. Use when a paper draft may have drifted away from the actual experiment outputs.
argument-hint: [paper-and-results]
---

# Paper Evidence Verifier

Use this skill when the main risk is not prose quality, but factual drift between the paper and the experiment evidence.

## When to Use

- The draft contains many numbers copied from logs, JSON summaries, or tables
- The paper was generated or heavily revised by an LLM
- You need a deterministic check that Results, Experiments, Ablations, and tables do not contain unsupported values

For bibliography issues, use `citation-verification-gate`.
For reviewer-style critique, use `self-review` or `review-ensemble`.

## Workflow

### Step 1: Build the Ground-Truth Registry
- Read the authoritative experiment summary, not ad hoc notes.
- Prefer the promoted best or final experiment summary over intermediate iterations.
- Collect verified values, verified condition names, and trusted metadata such as seed counts or primary metrics.

### Step 2: Scan the Draft
- Extract numerical values from the paper while skipping citations, labels, URLs, package declarations, code blocks, and similar LaTeX noise.
- Classify where each number appears: strict sections, lenient sections, tables, or prose.

### Step 3: Verify Numbers
- Auto-allow only a narrow set of common constants and tiny structural integers.
- Match all other numbers against the verified registry with a small tolerance.
- Treat strict sections such as Results, Experiments, Evaluation, Ablations, and result tables as hard-fail zones.

### Step 4: Check Condition Names and Config Claims
- Flag condition names or variants mentioned in the paper that do not exist in the experiment outputs.
- Flag unsupported claims about trial counts, baselines, statistical tests, or hardware details.

### Step 5: Sanitize if Needed
- Replace unsupported table cells with placeholders instead of leaving fabricated values in place.
- Remove or weaken unsupported prose claims.
- Prefer pre-built tables from verified data whenever possible.

## References

- `references/verification-rules.md`: strict vs lenient zones, tolerance rules, skip zones
- `references/sanitization-playbook.md`: how to remove or replace unsupported values safely
- `references/verified-results-tables.md`: how to pre-build manuscript tables from verified data

## Rules

- Results and table numbers are evidence claims, not stylistic content.
- Never keep a number in a strict section unless it can be traced to an experiment artifact.
- Treat fabricated condition names as seriously as fabricated metrics.
- When uncertain, remove or annotate the claim instead of preserving a suspicious value.

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [latex-writeup-loop](../latex-writeup-loop/), [table-generation](../table-generation/)
- Downstream: [review-ensemble](../review-ensemble/), [paper-revision](../paper-revision/)
- See also: [paper-compilation](../paper-compilation/), [citation-verification-gate](../citation-verification-gate/), [claim-rigor-audit](../claim-rigor-audit/), [claim-evidence-map](../claim-evidence-map/), [experiment-section-audit](../experiment-section-audit/)
