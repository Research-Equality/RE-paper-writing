---
name: study-manuscript
description: Draft, structure, and refine pedagogical study manuscripts, textbook chapters, and interactive foundational course modules. Unlike compressed conference papers, this skill prioritizes axiomatic clarity, formal definitions, fully worked step-by-step matrix/numerical examples, geometric intuition, pathology analyses, and interactive artifact bridges. Use when writing monographs, study guides, interactive HTML/LaTeX lecture notes, or expanding paper background sections into comprehensive didactic textbooks.
argument-hint: [module-or-chapter-title]
---

# Study Manuscript & Textbook Chapter Writer

Transform dense mathematical and topological deep learning topics into authoritative, publication-grade study manuscripts and interactive textbook chapters.

## Positioning & Philosophy

Standard academic writing skills (`paper-writing-section`, `ml-paper-writing`) are optimized for space-constrained conference submissions (ICLR, NeurIPS, ICML), where derivations are routinely omitted, background is compressed into passing citations, and readers are assumed to know standard conventions.

**`study-manuscript`** operates under the textbook paradigm:
1. **Axiomatic Foundation Before Dynamic Action**: Never introduce an operator without first formally establishing the carrier space, the topology, and the discrete differential structure.
2. **Exhaustive Numeric & Algebraic Transparency**: Never say *"it is trivial to verify that $L = D - A$"*. Write out concrete toy graphs, display the exact matrices entry by entry, and compute products and energies with real numbers.
3. **Pedagogical Rhythm (The 7-Pillar Architecture)**:
   - **Motivation & Intuition**: Real-world/geometric dilemma that standard tools fail to solve.
   - **Formal Definition Boxes**: Axiomatic, mathematically rigorous definitions with typed signatures.
   - **Concrete Worked Examples (Walkthrough)**: Small, non-trivial toy graphs ($n \in \{4, 5, 6\}$) calculated step by step.
   - **Proposition & Spectral Properties**: Invariants, conservation laws, spectral bounds (e.g. $\mathrm{spec}(\Delta) \subset [0, 2]$).
   - **Pathology & Failure Modes**: Where the formulation breaks down (e.g., Dirichlet collapse, heterophilic cancellation, exponential volume bottleneck).
   - **The Advanced Bridge**: How this foundation leads directly to modern frontiers (e.g., Cellular Sheaves, Bisheaves, NBD).
   - **Interactive / Simulation Anchor**: Verification via computational or visual artifacts (HTML5 Canvas, PyTorch verification snippet).

---

## Workflow

### Step 1: Establish Scope, Prerequisites & Pedagogical Contract
- Identify the target chapter or module topic (e.g., *Spectral Graph Theory, Message Passing, Cellular Sheaves, Orthogonal Stalk Transport*).
- Define notation standards (e.g., indices, graph tuples $G = (V, E)$, degrees, normalizations).
- Choose the canonical toy example to accompany the chapter throughout all derivations.

### Step 2: Draft the 7-Pillar Manuscript
Consult `references/pedagogical-framing.md` and `references/worked-examples-guide.md`.
- **Definition Blocks**: Enclose all definitions in clean formal blocks (LaTeX environments `\begin{definition}` or HTML `<div class="math-box formal-def">`).
- **Matrix Calculations**: Lay out matrices in full grid form:
  $$\mathbf{A} \in \mathbb{R}^{n \times n}, \quad \mathbf{D} \in \mathbb{R}^{n \times n}, \quad \mathbf{L} = \mathbf{D} - \mathbf{A}, \quad \mathbf{\Delta}_{\mathrm{sym}} = \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2}$$
  Show intermediate roots and inverses explicitly (e.g., $1/\sqrt{2}, 1/\sqrt{3}$).
- **Energy Derivations**: Show the quadratic form expansion:
  $$E(x) = \frac{1}{2} x^\top L x = \frac{1}{2} \sum_{(u, v) \in E} (x_u - x_v)^2$$
  Substitute concrete vector coordinates and show sum term by term.

### Step 3: Implement Visual & Interactive Anchors
- If authoring HTML: integrate responsive interactive widgets (Canvas/SVG), sliders for diffusion step sizes $\tau$, and live metrics.
- If authoring LaTeX: specify standalone TikZ/pgfplots graph figures with numbered vertices and highlighted edge weights.

### Step 4: Refinement & Didactic Audit
Run the quality checklist:
- [ ] Are all matrix dimensions explicitly stated?
- [ ] Is there at least one fully computed numerical example with non-binary values?
- [ ] Is the connection to physical/geometric processes (heat equation, random walk) clearly derived?
- [ ] Are limitations and open questions (homophily vs. heterophily, oversmoothing) rigorously motivated?

---

## References

- Pedagogical Structure & Didactic Patterns: `references/pedagogical-framing.md`
- Step-by-Step Worked Examples & Matrix Calculation Guide: `references/worked-examples-guide.md`

## Related Skills
- Upstream: [research-planning](../research-planning/), [literature-review](../literature-review/)
- Downstream: [ml-paper-writing](../ml-paper-writing/), [latex-writeup-loop](../latex-writeup-loop/), [academic-plotting](../academic-plotting/)
- Complements: [long-form-manuscript-polish](../long-form-manuscript-polish/), [paper-writing-section](../paper-writing-section/)
