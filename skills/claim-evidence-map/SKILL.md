---
name: claim-evidence-map
description: Map the paper's headline claims, especially in the abstract and introduction, to concrete supporting evidence and flag claims that need downgrading, relocation, or new experiments. Use when the draft may be overclaiming or when reviewer trust depends on tight claim-support alignment.
argument-hint: [draft-or-claim-list]
---

# Claim Evidence Map

Use this skill when the writing sounds confident but the support structure may be weak or opaque.

## When to Use

- The abstract or introduction makes strong novelty or performance claims
- Reviewers are likely to ask "where is the evidence for this sentence?"
- A paper has been revised many times and claims may have drifted away from the results
- You need a structured map before `claim-rigor-audit`, `paper-revision`, or final submission

## Workflow

### Step 1: Extract Headline Claims
- Pull the major claims from title, abstract, introduction, conclusion, and contribution bullets.
- Focus first on novelty, performance, robustness, generalization, and practical-value claims.
- Split multi-part claims into separate items so each can be checked independently.

### Step 2: Anchor Each Claim
- For each claim, identify the exact supporting evidence:
  - result table
  - ablation
  - qualitative figure
  - error analysis
  - stress test
  - methodological argument only
- Record exact anchors such as `Table 2`, `Fig. 3`, or `Sec. 4.2`.

### Step 3: Assign Support Status
Use one of these labels:

- `supported`
- `partially-supported`
- `needs-evidence`
- `not-testable-from-paper`

Claims without a clear anchor should never remain implicitly "supported."

### Step 4: Repair the Draft
- Weaken or narrow claims that exceed the evidence.
- Move speculative interpretation out of Abstract/Introduction if it belongs later in Discussion.
- Add missing evidence references when the support exists but is not visible to the reader.

### Step 5: Return the Map
Return a compact table:

```text
Claim | Evidence anchor | Status | Required action
```

See `references/claim-map-template.md`.

## Rules

- Treat Abstract and Introduction as high-risk zones.
- A claim is not supported merely because the authors believe it is true.
- If evidence is indirect or partial, label it as such.
- Prefer narrowing the claim over stretching the interpretation.

## References

- `references/claim-map-template.md`: output structure and status labels
- `references/high-risk-zones.md`: where unsupported claims cause the most reviewer damage

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [paper-writing-section](../paper-writing-section/), [experiment-report-bridge](../experiment-report-bridge/)
- Downstream: [claim-rigor-audit](../claim-rigor-audit/), [paper-evidence-verifier](../paper-evidence-verifier/), [paper-revision](../paper-revision/)
- See also: [self-review](../self-review/), [experiment-section-audit](../experiment-section-audit/)
