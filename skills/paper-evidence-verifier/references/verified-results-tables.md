# Verified Results Tables

AutoResearchClaw avoids LLM number drift by generating LaTeX result tables directly from verified experiment summaries.

## Core Idea

- Build a registry from experiment data
- Select only reportable conditions
- Generate manuscript-ready LaTeX tables from those conditions
- Tell the drafting workflow not to edit the numeric cells manually

## What the Table Builder Preserves

- condition names
- means and standard deviations
- per-seed values when available
- seed counts
- metric direction for bolding the best result

## Why This Matters

- The LLM is removed from the number-generation loop
- Result tables become deterministic artifacts instead of prose-generated content
- Downstream verifiers can treat these tables as trusted inputs

## Practical Guidance

- If a project has a stable `experiment_summary.json` or equivalent aggregate result file, build the results table from that file first
- Use prose to explain the table, not to re-invent its numbers
