# Verification Rules

These rules are distilled from AutoResearchClaw's deterministic anti-fabrication pipeline.

## Strict Zones

Unsupported numbers in these areas should be treated as hard failures:

- Results
- Experiments
- Evaluation
- Ablation and ablation studies
- Main result tables
- Experimental setup when it states concrete run counts or training settings

## Lenient Zones

Unsupported numbers in these areas are still problematic, but usually require warnings and revision rather than immediate rejection:

- Introduction
- Related Work
- Discussion
- Conclusion
- Background

## Skip Zones

Do not try to verify numbers inside:

- `\cite{}`, `\ref{}`, `\label{}`
- URLs and file paths
- comments
- verbatim and code blocks
- equations and algorithm blocks when they are symbolic rather than empirical
- package declarations or document setup

## Matching Logic

- Common constants and tiny structural integers may be auto-allowed
- All other numbers should match a verified value registry within a small tolerance
- Percentage and decimal forms should cross-match when they represent the same value
- Condition names should also be checked, not just raw numbers

## Failure Patterns to Catch

- Paper claims more trials than were actually run
- Reported metric is absent from experiment outputs
- Table contains tuned-looking numbers not present in the registry
- Method or baseline names appear in the paper but not in the run summary
