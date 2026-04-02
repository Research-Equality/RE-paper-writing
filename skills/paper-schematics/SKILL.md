---
name: paper-schematics
description: Design manuscript visuals that are not primarily numeric plots, including graphical abstracts, method flowcharts, PRISMA or CONSORT diagrams, system overviews, mechanism figures, and caption packages. Use when a paper needs a first-impression visual or a conceptual figure that clarifies the story.
argument-hint: [figure-intent]
---

# Paper Schematics

Use this skill for the paper figures that explain structure, workflow, or mechanism rather than measured values on axes.

## When to Use

- The paper needs a graphical abstract, Figure 1 overview, or conceptual diagram
- Methods are complex enough that a flowchart or pipeline figure will explain them faster than prose
- The manuscript needs PRISMA, CONSORT, system, architecture, or mechanism diagrams
- A figure exists, but its caption, labels, or panel logic are not publication-ready

For numeric charts, use `academic-plotting`.
For venue layout and figure-count tradeoffs, use `venue-submission-strategy`.

## Workflow

### Step 1: Define the Figure's Job
- Decide whether the figure should summarize the whole paper, explain methods, show study flow, or clarify a mechanism.
- Keep one figure responsible for one main message.

### Step 2: Choose the Figure Type
- Graphical abstract: one-image paper summary
- Method or system overview: boxes, arrows, and stage boundaries
- Reporting flow diagram: PRISMA, CONSORT, screening, or cohort construction
- Mechanism or concept figure: qualitative causal or structural explanation
- Multi-panel explanatory figure: combine overview, detail, and legend deliberately

### Step 3: Plan Layout Before Rendering
- Write the panel order, label vocabulary, and visual hierarchy first.
- Keep text minimal and let the caption do the explanatory work.
- Align colors, icons, and terminology with the rest of the manuscript.

### Step 4: Generate and Refine
- Use a diagram workflow or structured prompt for the visual draft.
- Review for scientific fidelity, not just aesthetics.
- Fix ambiguous arrows, overloaded legends, and decorative clutter aggressively.

### Step 5: Package with Caption and Export
- Write a caption that explains what is shown, what each symbol means, and how to read the flow.
- Export a manuscript-ready asset with stable dimensions and readable labels.
- Keep the editable source or prompt record for later revision.

## References

- `references/figure-types.md`: which paper figure type to choose for which communication goal
- `references/layout-and-style.md`: layout, typography, accessibility, and consistency rules
- `references/caption-workflow.md`: how to write figure captions that actually help the paper

## Rules

- Do not use a schematic to imply measurements that were never made.
- Distinguish conceptual explanation from empirical result.
- Minimize text inside the figure; push detail into the caption.
- A graphical abstract or Figure 1 should still make sense when viewed before the reader reaches Methods.

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [paper-writing-section](../paper-writing-section/)
- Downstream: [academic-plotting](../academic-plotting/), [latex-formatting](../latex-formatting/), [paper-compilation](../paper-compilation/)
- See also: [reporting-guidelines-check](../reporting-guidelines-check/), [table-generation](../table-generation/)
