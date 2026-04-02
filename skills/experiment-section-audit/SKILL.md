---
name: experiment-section-audit
description: Audit and redesign the Experiments section around reviewer-facing evidence needs: strong baselines, contribution-linked validation, ablations, hard settings, and readable tables or captions. Use when a paper's experiments feel incomplete, unconvincing, or weakly tied to the claimed contributions.
argument-hint: [experiment-section-or-draft]
---

# Experiment Section Audit

Use this skill when the paper may have enough experiments to run, but not enough evidence packaging to persuade reviewers.

## When to Use

- The Experiments section exists but feels scattered or weakly argued
- Reviewers would likely ask for stronger baselines, clearer ablations, or tougher settings
- Tables and captions communicate numbers but not the message
- The paper's claimed contributions are not mapped to explicit validation experiments

## Workflow

### Step 1: Start from the Claimed Contributions
- List the core contributions from Abstract, Introduction, and Method.
- For each contribution, ask what experiment would directly validate it.
- Build a coverage map from `contribution -> required validation experiment`.

### Step 2: Audit Baseline Strength
- Check whether recent and strong baselines are included.
- Confirm that comparisons use fair settings, not favorable mismatches.
- Flag any result section that relies mainly on weak or outdated baselines.

### Step 3: Audit the Ablation Package
- For each major design choice, require at least one ablation or replacement test.
- Add component-interaction ablations when modules are coupled.
- Keep one core ablation table for the main contributions and smaller focused ablations for local design choices.

### Step 4: Audit Generalization and Limits
- Ask whether the paper includes harder settings, stress tests, or failure modes.
- Check whether the draft reports boundaries of effectiveness rather than only best-case outcomes.
- If the scope is narrow, make that explicit instead of overclaiming.

### Step 5: Audit Communication Quality
- Ensure each table has one message and readable metric headers.
- Keep captions short but sufficient for protocol and notation.
- Make figures and tables part of the argument, not detached decoration.

See `references/table-and-caption-rules.md`.

## Output

Return:

1. `claim -> experiment` coverage map
2. Missing baselines or ablations
3. Table/caption rewrite recommendations
4. A revised Experiments section structure

## Rules

- The Experiments section must answer why the method should be trusted.
- Every key design claim needs explicit validation.
- Do not hide weak scope or failure modes if they define the real limits of the method.
- A clean table is not enough; the evidence package must match the contributions.

## References

- `references/experiment-coverage-template.md`: claim-to-experiment mapping
- `references/table-and-caption-rules.md`: reviewer-facing table and caption guidance

## Related Skills

- Upstream: [experiment-report-bridge](../experiment-report-bridge/), [table-generation](../table-generation/), [paper-writing-section](../paper-writing-section/)
- Downstream: [paper-evidence-verifier](../paper-evidence-verifier/), [self-review](../self-review/), [paper-revision](../paper-revision/)
- See also: [claim-evidence-map](../claim-evidence-map/), [academic-plotting](../academic-plotting/)
