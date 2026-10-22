# Pedagogical Framing & Didactic Patterns

When writing a textbook chapter, course module, or monograph section, adopt the voice of a master researcher-educator who leaves no algebraic ambiguity.

## 1. The Tone & Voice
- **Rigorous yet Lucid**: Treat the reader as an ambitious scholar who values formal proofs, but needs intuitive geometric grounding before dense calculations.
- **No Mystery Notation**: Every symbol introduced must have an explicit set membership (e.g., $v_i \in V$, $A \in \{0, 1\}^{n \times n}$ or $\mathbb{R}^{n \times n}$).
- **Continuous Narrative**: Do not jump between definitions without transition prose explaining *why* the next mathematical object was invented.

## 2. The 7 Pedagogical Pillars
1. **Pillar I: Intuitive Context & Physical Analogy**
   - Anchor the math in physics or geometry: discrete heat diffusion, vibrating membranes, electrical resistor networks, fluid pressure.
2. **Pillar II: Formal Definition**
   - Provide clean boxed statements. Use numbered definitions (Definition 1.1, Definition 1.2).
3. **Pillar III: The Canonical Toy Graph (Worked Walkthrough)**
   - Always instantiate the concept on an explicit small graph ($n \in \{4, 5, 6\}$).
   - Show vertex coordinates, edge pairs, degrees, and the full matrices without ellipses ($...$).
4. **Pillar IV: Action on Signals (Operators in Motion)**
   - Show how the operator acts on a 1D or multi-channel signal $x \in \mathbb{R}^n$.
   - Compute the output vector $(Lx)$ entry by entry.
5. **Pillar V: Invariants and Conservation Laws**
   - State and prove core invariants: $L \mathbf{1} = \mathbf{0}$, positive semi-definiteness ($x^\top L x \ge 0$), trace, spectrum bounds.
6. **Pillar VI: Structural Pathologies & Dilemmas**
   - Identify where the simple model fails in real-world systems:
     - Isotropic smoothing washing out high-frequency features (Oversmoothing).
     - Heterophilic graphs where neighbors belong to opposite classes.
     - Information bottlenecks in tree-like or negatively curved topologies (Over-squashing).
7. **Pillar VII: Modern Frontiers & Generalizations**
   - Explain how current research overcomes these limits: Sheaf Laplacians ($F \in O(d)$), Bisheaves ($F \neq C^\top$), anisotropic diffusion.
