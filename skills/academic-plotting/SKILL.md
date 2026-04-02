---
name: academic-plotting
description: Create publication-quality numeric or data-driven figures for research papers, including result plots, ablation charts, benchmark comparisons, and data-backed visual summaries. Use when the user needs reviewer-readable figures whose content is anchored in measured values or structured chart data.
argument-hint: [figure-request]
---

# Academic Plotting

Generate paper-ready figures from verified result data or structured chart specifications.

## When to Use

- The figure has numeric axes, measured values, or category-level comparisons
- The manuscript needs benchmark plots, ablation charts, error breakdowns, or training curves
- Exact visual fidelity to verified data matters more than conceptual storytelling

For conceptual, non-numeric overview figures, use `paper-schematics`.

## Figure Routing

- If the figure has numeric axes, use a code-first plotting workflow.
- If the figure is a conceptual boxes-and-arrows overview, route to `paper-schematics` instead of this skill.
- If the figure is undecided, inspect the surrounding paper text and infer the intended message before choosing the format.

## Workflow

### Step 1: Extract the Message
- Read the relevant section, result table, or experiment note.
- Identify what the figure must prove or explain.
- Keep the figure focused on one story.

### Step 2: Choose the Figure Type
- Training curves or performance over steps: line plots
- Method comparison across benchmarks: grouped bars or dot plots
- Correlations: scatter plots
- Square metric grids: heatmaps
- Error or category breakdowns: grouped bars, dot plots, or compact heatmaps

### Step 3: Build the Specification
- Extract exact labels from the paper text.
- Decide the layout, highlight color, and what should be visually dominant.
- Mark "ours" or the key contribution clearly but not aggressively.

### Step 4: Generate and Review
- Prefer deterministic code for all figures with numeric data.
- For conceptual diagrams, use the structured prompt or diagram workflow in `references/diagram-generation.md`.
- Save both the editable source and the final exported asset.

### Step 5: Verify Readability
- Ensure labels are legible at paper scale.
- Confirm no chart implies unsupported numerical precision.
- Keep colors venue-safe and readable in grayscale where possible.

## References

- `references/data-visualization.md`: chart selection, matplotlib patterns, chart hygiene
- `references/diagram-generation.md`: diagram prompting and layout workflow
- `references/style-guide.md`: palettes, typography, visual consistency

## Rules

- Never plot invented or rounded-up numbers that do not match the source data.
- Use consistent color semantics across all paper figures.
- Optimize for interpretation speed, not decoration.
- If the figure is primarily conceptual rather than data-backed, move it to `paper-schematics`.

## Related Skills

- Upstream: [ml-paper-writing](../ml-paper-writing/), [paper-writing-section](../paper-writing-section/)
- Downstream: [latex-formatting](../latex-formatting/), [paper-compilation](../paper-compilation/)
- See also: [table-generation](../table-generation/), [paper-schematics](../paper-schematics/)
