---
name: reporting-guidelines-check
description: Audit whether a manuscript satisfies the right study-type reporting standard such as CONSORT, STROBE, PRISMA, TRIPOD, ARRIVE, or MINSEQE, then turn missing checklist items into concrete edits. Use before submission, during revision, or when reviewers question reporting completeness.
argument-hint: [draft-and-study-type]
---

# Reporting Guidelines Check

Use this skill when the paper may be scientifically sound but still incomplete against the formal reporting standard expected by reviewers or journals.

## When to Use

- The manuscript is a trial, observational study, systematic review, benchmark, prediction study, sequencing study, or other study type with a known checklist
- A journal or reviewer explicitly asks for CONSORT, STROBE, PRISMA, TRIPOD, ARRIVE, or similar compliance
- The draft feels under-specified in Methods, participant flow, data availability, or statistical reporting

For venue fit and template choice, use `venue-submission-strategy`.
For reviewer-style critique, use `self-review` or `review-ensemble`.

## Workflow

### Step 1: Identify the Primary Guideline
- Infer the study type from the draft, not from the paper title alone.
- Choose one primary reporting standard and add extensions only when the design truly requires them.
- Record any mandatory companion artifacts such as flow diagrams, registrations, or supplementary checklists.

### Step 2: Build a Compliance Matrix
- Create a checklist table with columns for `item`, `status`, `evidence`, `location`, and `required action`.
- Map every required item to the current manuscript, appendix, supplement, or external repository.
- Mark unsupported items explicitly as `missing`, not `implicitly covered`.

### Step 3: Audit the Draft Section by Section
- Check title and abstract for study-type signaling.
- Check Methods for sample definition, intervention or measurement details, exclusions, randomization, statistics, and reproducibility.
- Check Results for participant or sample flow, denominators, confidence intervals, harms, and negative findings where applicable.
- Check Discussion and declarations for limitations, registration, ethics, funding, and data or code access.

### Step 4: Patch the Gaps
- Convert missing checklist items into concrete manuscript edits or supplemental artifacts.
- If an item truly does not apply, state why instead of leaving ambiguity.
- Add flow diagrams, baseline tables, or data-availability statements before polishing prose.

### Step 5: Prepare Submission Evidence
- Produce a final compliance summary that can be reused for journal submission forms or rebuttal.
- Keep a short list of unresolved items that still require author confirmation.

## References

- `references/guideline-selector.md`: map study types to the right reporting standard
- `references/compliance-matrix.md`: how to audit section coverage and common omissions
- `references/submission-attachments.md`: supporting artifacts often required with the manuscript

## Rules

- Do not claim compliance with a guideline unless the required evidence is actually present.
- Prefer one primary guideline plus justified extensions over a vague mix of many standards.
- Treat missing sample flow, registration, and statistical detail as structural issues, not copyediting issues.
- If the draft cannot satisfy an item from the available evidence, report the gap explicitly.

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [paper-writing-section](../paper-writing-section/), [systematic-review](../systematic-review/)
- Downstream: [latex-formatting](../latex-formatting/), [self-review](../self-review/), [review-ensemble](../review-ensemble/), [paper-revision](../paper-revision/)
- See also: [venue-submission-strategy](../venue-submission-strategy/), [paper-evidence-verifier](../paper-evidence-verifier/), [claim-rigor-audit](../claim-rigor-audit/)
