# Guideline Selector

Choose the reporting standard from the study design, not from the venue alone.

## Core Mapping

- Randomized controlled trial: `CONSORT`
- Trial protocol: `SPIRIT`
- Observational cohort, case-control, or cross-sectional study: `STROBE`
- Systematic review or meta-analysis: `PRISMA`
- Scoping review: `PRISMA-ScR`
- Diagnostic accuracy study: `STARD`
- Prediction model development or validation: `TRIPOD`
- Animal study: `ARRIVE`
- Case report: `CARE`
- Microarray study: `MIAME`
- High-throughput sequencing study: `MINSEQE`
- Proteomics study: `MIAPE`
- Flow cytometry study: `MIFlowCyt`

## Selection Rules

- Pick one primary guideline first.
- Add an extension only when the design explicitly matches it.
- If the paper combines multiple study components, match the main claim path:
  - systematic review with meta-analysis: `PRISMA`
  - benchmark plus predictive model: usually `TRIPOD` if the main claim is prediction
  - trial plus biomarker subgroup analysis: `CONSORT` first, then note biomarker-specific additions

## Mandatory Companion Artifacts

- `CONSORT`: participant flow diagram, baseline table, registration details
- `STROBE`: participant flow or source description, bias discussion, missing-data handling
- `PRISMA`: search strategy, study-selection flow diagram, inclusion criteria, bias assessment
- `TRIPOD`: predictor definition, handling of missing data, validation procedure, performance metrics
- `ARRIVE`: ethics, animal details, randomization, blinding, sample-size rationale
- `MINSEQE`: sequencing protocol, QC metrics, deposited raw data, processing pipeline

## Failure Modes

- Using a venue checklist instead of a study-design checklist
- Treating "mentioned somewhere" as compliant
- Ignoring supplements, repositories, or registration numbers in the audit
- Claiming `not applicable` without justification
