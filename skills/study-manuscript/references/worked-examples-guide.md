# Worked Examples & Matrix Calculation Guide

A hallmark of high-quality didactic textbooks is the concrete, numerical walkthrough that leaves no room for algebraic ambiguity.

## 1. Choosing the Canonical Toy Graph
Select a graph with at least 4 nodes that breaks trivial symmetries:
- Not a simple complete graph $K_n$ (too symmetric; all degrees equal).
- Not a simple path $P_n$ (too trivial).
- Recommended: A 4-node diamond or kite graph with heterogeneous degrees:
  $$V = \{v_1, v_2, v_3, v_4\}$$
  $$E = \{(v_1, v_2), (v_1, v_3), (v_2, v_3), (v_3, v_4)\}$$
  - $v_1$ has degree 2
  - $v_2$ has degree 2
  - $v_3$ has degree 3 (hub/central node)
  - $v_4$ has degree 1 (pendant/leaf node)

## 2. Explicit Matrix Presentation
Never compress matrices with ellipses when $n \le 6$. Show every row and column:

### Adjacency Matrix $\mathbf{A}$:
$$\mathbf{A} = \begin{bmatrix}
0 & 1 & 1 & 0 \\
1 & 0 & 1 & 0 \\
1 & 1 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}$$

### Degree Matrix $\mathbf{D}$:
$$\mathbf{D} = \begin{bmatrix}
2 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 3 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}, \quad
\mathbf{D}^{-1/2} = \begin{bmatrix}
\frac{1}{\sqrt{2}} & 0 & 0 & 0 \\
0 & \frac{1}{\sqrt{2}} & 0 & 0 \\
0 & 0 & \frac{1}{\sqrt{3}} & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$$

### Combinatorial Laplacian $\mathbf{L} = \mathbf{D} - \mathbf{A}$:
$$\mathbf{L} = \begin{bmatrix}
2 & -1 & -1 & 0 \\
-1 & 2 & -1 & 0 \\
-1 & -1 & 3 & -1 \\
0 & 0 & -1 & 1
\end{bmatrix}$$
Point out:
1. Diagonal entries equal vertex degrees: $L_{ii} = d_i$.
2. Off-diagonal entries equal negative adjacency: $L_{ij} = -1$ if $(i,j) \in E$, else $0$.
3. Row sum: $\sum_j L_{ij} = d_i - d_i = 0$, proving $L \mathbf{1} = \mathbf{0}$.

### Symmetric Normalized Laplacian $\mathbf{\Delta}_{\mathrm{sym}} = \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2} \mathbf{A} \mathbf{D}^{-1/2}$:
$$\mathbf{\Delta}_{\mathrm{sym}} = \begin{bmatrix}
1 & -\frac{1}{2} & -\frac{1}{\sqrt{6}} & 0 \\
-\frac{1}{2} & 1 & -\frac{1}{\sqrt{6}} & 0 \\
-\frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{6}} & 1 & -\frac{1}{\sqrt{3}} \\
0 & 0 & -\frac{1}{\sqrt{3}} & 1
\end{bmatrix}$$

## 3. Concrete Signal & Energy Walkthrough
Assign a concrete non-trivial signal vector $x = [x_1, x_2, x_3, x_4]^\top \in \mathbb{R}^4$, for example:
$$x = \begin{bmatrix} 1.0 \\ 0.8 \\ -0.5 \\ -1.0 \end{bmatrix}$$

Compute the quadratic Dirichlet Energy $E(x) = \frac{1}{2} x^\top L x$:
$$E(x) = \frac{1}{2} \left[ (x_1 - x_2)^2 + (x_1 - x_3)^2 + (x_2 - x_3)^2 + (x_3 - x_4)^2 \right]$$
Substitute numeric values step by step:
$$= \frac{1}{2} \left[ (1.0 - 0.8)^2 + (1.0 - (-0.5))^2 + (0.8 - (-0.5))^2 + (-0.5 - (-1.0))^2 \right]$$
$$= \frac{1}{2} \left[ 0.04 + 2.25 + 1.69 + 0.25 \right] = \frac{1}{2} [4.23] = 2.115$$

Explain the interpretation:
- Edges with similar values ($(v_1, v_2)$) contribute negligibly ($0.04$).
- Edges crossing between positive and negative signals ($(v_1, v_3)$ and $(v_2, v_3)$) dominate the energy penalty ($2.25 + 1.69 = 3.94$).
This directly builds the reader's intuition for homophily vs. heterophily!
