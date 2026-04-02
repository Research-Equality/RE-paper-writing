---
name: claim-rigor-audit
description: Stress-test manuscript claims for methodological validity, bias, confounding, evidence strength, and statistical interpretation. Use when a paper risks overclaiming or weak causal reasoning even if the prose looks polished.
argument-hint: [draft-or-claim-list]
---

# Claim Rigor Audit

Use this skill when the main danger is not formatting or wording, but claims that are too strong for the underlying evidence.

## When to Use

- A draft makes causal, clinical, or broad-generalization claims that may outrun the study design
- Reviewers are likely to question bias, confounding, sample quality, or statistical validity
- The team needs a claim-by-claim downgrade or rewrite plan before submission

For numerical consistency against experiment artifacts, use `paper-evidence-verifier`.
For checklist compliance, use `reporting-guidelines-check`.

## Workflow

### Step 1: Extract the Headline Claims
- List the paper's strongest claims from title, abstract, introduction, results, and conclusion.
- Classify each one as descriptive, comparative, predictive, causal, mechanistic, or generalization claim.

### Step 2: Map Evidence Strength
- Identify the study design or evidence type behind each claim.
- Use evidence hierarchy rather than author confidence to judge strength.
- Note when the paper is asking observational evidence to carry causal weight.

### Step 3: Audit Design, Bias, and Confounding
- Check selection bias, measurement bias, attrition, publication bias, and reporting bias.
- Identify confounders that could plausibly explain the finding.
- Ask whether controls, randomization, blinding, or adjustment strategies are actually adequate.

### Step 4: Audit the Statistics
- Check whether significance is being mistaken for importance.
- Look for underpowered claims, multiple-comparison risk, subgroup fishing, or outcome switching.
- Require effect sizes, intervals, and honest uncertainty language where appropriate.

### Step 5: Rewrite to Match the Evidence
- Downgrade causal language when the design is only correlational.
- Separate what the data show from what the authors infer.
- Produce a revision table: `claim -> risk -> required rewrite or added evidence`.

## References

- `references/evidence-hierarchy.md`: how to judge claim strength by study design and evidence tier
- `references/bias-and-confounding.md`: common bias patterns and mitigation questions
- `references/statistical-pitfalls.md`: frequent statistical overclaim patterns

## Rules

- Do not let polished prose hide weak inference.
- Correlation is not causation unless the design justifies it.
- Non-significance does not automatically mean no effect.
- When the evidence is mixed or weak, weaken the claim before submission.

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [paper-writing-section](../paper-writing-section/), [systematic-review](../systematic-review/)
- Downstream: [reporting-guidelines-check](../reporting-guidelines-check/), [self-review](../self-review/), [review-ensemble](../review-ensemble/), [paper-revision](../paper-revision/)
- See also: [paper-evidence-verifier](../paper-evidence-verifier/), [manuscript-scorecard](../manuscript-scorecard/), [claim-evidence-map](../claim-evidence-map/)
