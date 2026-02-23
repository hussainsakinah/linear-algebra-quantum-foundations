# Mathematics for Quantum Computing

A clean, structured, GitHub-ready LaTeX reference compiled from personal
lecture notes.  It covers the algebraic and functional-analytic foundations
that underpin quantum computing and quantum mechanics, progressing from basic
algebraic structures all the way to Fourier analysis and the outer product.

---

## Contents

| # | Chapter | Topics |
|---|---------|--------|
| 1 | **Algebraic Structures** | Groupoid → Semigroup → Monoid → Group → Abelian Group → Ring → Field · Field Extensions |
| 2 | **Linear Transformations** | Systems of equations · Matrix notation · Composition as matrix multiplication |
| 3 | **Complex Numbers** | Argand plane · Polar form · Euler's formula · Complex conjugate · Phase factor |
| 4 | **Vector Spaces** | Axioms (VS1–VS9) · Examples · Subspaces · Metric spaces · Uniqueness theorems |
| 5 | **Normed & Inner Product Spaces** | Norms · Inner product axioms · Orthogonality · Topological properties · Unit vectors |
| 6 | **Hilbert Spaces** | Cauchy sequences · Completeness · $L^2$ space · Quantum interpretation |
| 7 | **Bra-Ket Notation** | Ket/bra axioms · Dual space · Inner product · Basis expansion · Probability amplitudes |
| 8 | **Matrices** | Types: square, row, column, identity, transpose · Symmetric · Hermitian · Orthogonal · Unitary |
| 9 | **Linear Operators & Eigenvalues** | Axioms · Matrix representation · Eigensystem · Hermitian conjugate · Proof that Hermitian eigenvalues are real · Cauchy–Schwarz |
| 10 | **Fourier Analysis** | Fourier series · Complex exponential form · Derivation of coefficients · Fourier transform · Uncertainty principle |
| 11 | **Outer Product & Completeness** | Outer product vs inner product · Completeness relation · Operator outer-product representation |

---

## Repository Layout

```
math-qc-notes/
├── main.tex                          # Root document — compile this
├── Makefile                          # Build helper (pdflatex)
├── .gitignore                        # LaTeX build artefacts
├── README.md                         # This file
└── chapters/
    ├── 01_algebraic_structures.tex
    ├── 02_linear_transformations.tex
    ├── 03_complex_numbers.tex
    ├── 04_vector_spaces.tex
    ├── 05_normed_and_inner_product_spaces.tex
    ├── 06_hilbert_spaces.tex
    ├── 07_bra_ket_notation.tex
    ├── 08_matrices.tex
    ├── 09_linear_operators_eigenvalues.tex
    ├── 10_fourier_analysis.tex
    └── 11_outer_product_completeness.tex
```

---

## Building

### Prerequisites

- A LaTeX distribution: [TeX Live](https://tug.org/texlive/) (Linux/macOS)
  or [MiKTeX](https://miktex.org/) (Windows)
- Required packages (included in most distributions):
  `amsmath`, `amssymb`, `amsthm`, `mathtools`, `physics`, `tcolorbox`,
  `hyperref`, `geometry`, `booktabs`, `enumitem`, `lmodern`

### Compile

```bash
# Using Make
make

# Or manually (run twice to resolve cross-references)
pdflatex main.tex
pdflatex main.tex
```

The output is `main.pdf`.

---

## LaTeX Conventions Used

| Environment | Purpose |
|-------------|---------|
| `definition` | Formal mathematical definition |
| `theorem` | Major result with proof |
| `proposition` | Minor result with proof |
| `lemma` | Auxiliary result |
| `corollary` | Direct consequence of a theorem |
| `example` | Worked example |
| `remark` | Clarifying comment |
| `notation` | Symbol or notational convention |

### Custom Commands

| Command | Output |
|---------|--------|
| `\ket{\psi}` | $\|\psi\rangle$ (from `physics` package) |
| `\bra{\psi}` | $\langle\psi\|$ |
| `\braket{a}{b}` | $\langle a\|b\rangle$ |
| `\norm{v}` | $\|v\|$ |
| `\abs{z}` | $|z|$ |
| `\R`, `\C`, `\Q`, `\Z` | $\mathbb{R}, \mathbb{C}, \mathbb{Q}, \mathbb{Z}$ |
| `\Tr` | $\mathrm{Tr}$ |
| `\outerp{a}{b}` | $|a\rangle\langle b|$ |

---

## Topics at a Glance

```
Algebraic Hierarchy
  Groupoid ⊂ Semigroup ⊂ Monoid ⊂ Group ⊂ Abelian Group
                                        ↓
                                  Ring ⊂ Field

Space Hierarchy
  Set → Topological Space → Metric Space
                                ↓
  Vector Space → Normed Space → Inner Product Space → Hilbert Space
```

---

## License

Released under the [MIT License](LICENSE).  Feel free to fork, extend, and
share.
