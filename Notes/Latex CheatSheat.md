# Obsidian LaTeX Cheatsheet

This note covers the essentials of writing mathematics in Obsidian using MathJax.

## 1. The Basics (The Containers)

- **Inline Math:** Surround with single `$` to write math in a sentence.  
  Example: `Let $f(x)$ be continuous.` → Let $f(x)$ be continuous.

- **Block Math:** Surround with double `$$` to center equations.  
  Example:→
$$\int e^x \, dx$$

## 2. Fundamental Syntax

| Type              | LaTeX Code     | Rendered              |
|-------------------|----------------|-----------------------|
| **Superscript**   | `x^{2y}`       | $x^{2y}$              |
| **Subscript**     | `a_{i,j}`      | $a_{i,j}$             |
| **Grouping**      | `{...}`        | Used to group characters (e.g., inside exponents) |
| **Fractions**     | `\frac{a}{b}`  | $\frac{a}{b}$         |
| **Multiplication**| `\cdot` or `\times` | $x \cdot y$ or $x \times y$ |
| **Roots**         | `\sqrt{x}` or `\sqrt[3]{x}` | $\sqrt{x}$ or $\sqrt[3]{x}$ |

## 3. Set Theory & Logic (Analysis/Discrete)

- **Sets:** `\mathbb{R}` → $\mathbb{R}$, `\mathbb{Z}` → $\mathbb{Z}$, `\mathbb{Q}` → $\mathbb{Q}$, `\mathbb{N}` → $\mathbb{N}$, `\emptyset` → $\emptyset$
- **Relations:** `\in` → $\in$, `\subset` → $\subset$, `\subseteq` → $\subseteq$, `\neq` → $\neq$
- **Logic:** `\implies` → $\implies$, `\iff` → $\iff$, `\forall` → $\forall$, `\exists` → $\exists$
- **Negation:** `\neg` → $\neg$ or `\not\exists` → $\not\exists$

## 4. Linear Algebra (Matrices & Vectors)

**Standard Matrix:**

→ `A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}`
$$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$

**Determinant (Vertical Bars):**

→`|A| = \begin{vmatrix} a & b \\ c & d \end{vmatrix}`
$$|A| = \begin{vmatrix} a & b \\ c & d \end{vmatrix}$$

**Inner Products & Norms:**

- Inner Product: `\langle u, v \rangle` → $\langle u, v \rangle$
- Norm: `\| x \|` → $\| x \|$
- Orthogonal: `u \perp v` → $u \perp v$

## 5. Calculus & Analysis

- Limits: `\lim_{x \to \infty}` → $\lim_{x \to \infty}$
- Integrals: `\int_{a}^{b}` → $\int_{a}^{b}$
- Summation: `\sum_{i=1}^{n}` → $\sum_{i=1}^{n}$
- Partials: `\frac{\partial f}{\partial x}` → $\frac{\partial f}{\partial x}$
- Gradient: `\nabla f` → $\nabla f$

## 6. Advanced Structures

### A. Piecewise Functions (Cases)

Essential for defining functions based on conditions.
```latex
f(x) = \begin{cases} 
x^2 & \text{if } x \ge 0 \\
-x & \text{if } x < 0 
\end{cases}
```
$$
f(x) = \begin{cases} 
x^2 & \text{if } x \ge 0 \\
-x & \text{if } x < 0 
\end{cases}
$$ 
### B. Multi-line Alignment (`aligned`)

For proofs or simplifications.
```latex
\begin{aligned}
x &= 2(a + b) \\
  &= 2a + 2b
\end{aligned}
```
$$
\begin{aligned}
x &= 2(a + b) \\
  &= 2a + 2b
\end{aligned}
$$
### C. Parentheses Sizing

When wrapping tall fractions, `( )` are too small. Use `\left(` and `\right)`.

- **Bad:** `(\frac{1}{2})` → $(\frac{1}{2})$
    
- **Good:** `\left( \frac{1}{2} \right)` → $\left( \frac{1}{2} \right)$
    
- _Also works for brackets `[]`, braces `\{\}`, and bars `||`._
### D. Advanced Typography

- **Calligraphy:** `\mathcal{L}` (Laplace), `\mathcal{P}` (Power set) → $\mathcal{L}, \mathcal{P}$
    
- **Fraktur:** `\mathfrak{g}` (Lie Algebras) → $\mathfrak{g}$
    
- **Blackboard Bold:** `\mathbb{R}`
    
- **Spacing:**
    
    - `\,` (Tiny space)
        
    - `\quad` (Medium space)
        
    - `\qquad` (Large space)
        

### E. Combinatorics & Discrete Math

- **Binomial Coeff:** `\binom{n}{k}` → $\binom{n}{k}$
    
- **Modular:** `a \equiv b \pmod{n}` → $a \equiv b \pmod{n}$
    
- **Floor/Ceil:** `\lfloor x \rfloor`, `\lceil x \rceil` → $\lfloor x \rfloor, \lceil x \rceil$
    

## 7. Obsidian-Specific Tips

- **Tagging:** You can tag equations like `$$E=mc^2 \tag{1}$$`.
    
- **Callouts for Theorems:**
    

> [!info] Theorem (Spectral Theorem)
> 
> If $A$ is symmetric, then there exists an orthogonal matrix $Q$ such that $A = Q \Lambda Q^T$.

# Advanced Obsidian LaTeX

This guide covers advanced formatting for proofs, Linear Algebra, and annotating your thoughts directly in the equations.

## 1. Advanced Linear Algebra

### Augmented Matrices (Gaussian Elimination)
Standard matrices don't have the vertical separator line. Use `array` for this.
* `c`: center aligned column
* `|`: vertical line separator
```latex
\left[
\begin{array}{cc|c}
1 & 2 & 5 \\
0 & 1 & 3
\end{array}
\right]
```
$$
\left[
\begin{array}{cc|c}
1 & 2 & 5 \\
0 & 1 & 3
\end{array}
\right]
$$

### Block Matrices

Useful for partitioning matrices.
```latex
M = \left[
\begin{array}{c|c}
A & B \\
\hline
C & D
\end{array}
\right]
```
$$
M = \left[
\begin{array}{c|c}
A & B \\
\hline
C & D
\end{array}
\right]
$$
### Bold Vectors (Rigorous Notation)

In advanced texts (like Hoffman/Kunze), vectors are often bold lowercase, not arrows.

- **Code:** `\mathbf{v}` or `\boldsymbol{\alpha}`
    
- **Render:** $\mathbf{v}, \boldsymbol{\alpha}$
    

---

## 2. Annotating Equations (The "Teacher" Mode)

These are crucial for self-study. They let you explain _why_ a step happened right inside the math.

### Underbrace & Overbrace

Explain specific terms.
```latex
\overbrace{1+2+\dots+n}^{n(n+1)/2}
```
$$
\overbrace{1+2+\dots+n}^{n(n+1)/2}
$$
### Crossing Out Terms (Cancellation)

_Note: This requires the `cancel` package. Add `\require{cancel}` at the top of your math block once._

- **Strike:** `\cancel{x}`
    
- **Strike with value:** `\cancelto{0}{x}` (My favorite for limits)
```latex
\require{cancel}
\lim_{x \to \infty} \frac{\cancel{x}^2 + 1}{\cancel{x}^2 - 3} = \cancelto{1}{\frac{1}{1}}
```
$$
\require{cancel}
\lim_{x \to \infty} \frac{\cancel{x}^2 + 1}{\cancel{x}^2 - 3} = \cancelto{1}{\frac{1}{1}}
$$
### Color Coding

Highlight changes between steps.

- **Code:** `\color{red}{x^2}`
    
- **Render:** $x + \color{red}{y} = z$
## 4. Accents & Decorations

Essential for Physics and Vector Calculus.

- **Hats:** `\hat{i}` ($\hat{i}$), `\widehat{AB}` ($\widehat{AB}$)
    
- **Vector Arrow:** `\vec{v}` ($\vec{v}$), `\overrightarrow{AB}` ($\overrightarrow{AB}$)
    
- **Mean/Conjugate:** `\bar{x}` ($\bar{x}$), `\overline{z+w}` ($\overline{z+w}$)
    
- **Time Derivative:** `\dot{x}` ($\dot{x}$), `\ddot{x}` ($\ddot{x}$)
    
- **Tilde:** `\tilde{x}` ($\tilde{x}$)
## 5. Custom Shortcuts (Macros)

You can define shortcuts at the top of a note to speed up writing.

Format: \newcommand{\name}{latex_code}

Place this at the very top of your note (invisible in preview):

$\newcommand{\R}{\mathbb{R}}$

$\newcommand{\b}[1]{\mathbf{#1}}$

Now you can just type:

- `$\R$` instead of `\mathbb{R}`
    
- `$\b{x}$` instead of `\mathbf{x}`
    

---

## 6. Big Operators

For advanced sums and products.

- **Product:** `\prod_{i=1}^n` ($\prod_{i=1}^n$)
    
- **Union/Intersect:** `\bigcup`, `\bigcap` ($\bigcup, \bigcap$)
    
- **Double Integral:** `\iint_D` ($\iint_D$)
    
- **Contour Integral:** `\oint_C` ($\oint_C$)
# LaTeX Symbol Reference

## 1. Greek Alphabet
*Note: Capitalize the command for the uppercase letter (e.g., `\Gamma`). Letters not listed usually look like standard Roman letters (e.g., A, B).*

| Name | Lower | Code | Upper | Code |
| :--- | :--- | :--- | :--- | :--- |
| Alpha | $\alpha$ | `\alpha` | $A$ | `A` |
| Beta | $\beta$ | `\beta` | $B$ | `B` |
| Gamma | $\gamma$ | `\gamma` | $\Gamma$ | `\Gamma` |
| Delta | $\delta$ | `\delta` | $\Delta$ | `\Delta` |
| Epsilon | $\epsilon$ | `\epsilon` | $E$ | `E` |
| Var Epsilon | $\varepsilon$ | `\varepsilon` | | |
| Zeta | $\zeta$ | `\zeta` | $Z$ | `Z` |
| Eta | $\eta$ | `\eta` | $H$ | `H` |
| Theta | $\theta$ | `\theta` | $\Theta$ | `\Theta` |
| Kappa | $\kappa$ | `\kappa` | $K$ | `K` |
| Lambda | $\lambda$ | `\lambda` | $\Lambda$ | `\Lambda` |
| Mu | $\mu$ | `\mu` | $M$ | `M` |
| Nu | $\nu$ | `\nu` | $N$ | `N` |
| Xi | $\xi$ | `\xi` | $\Xi$ | `\Xi` |
| Pi | $\pi$ | `\pi` | $\Pi$ | `\Pi` |
| Rho | $\rho$ | `\rho` | $P$ | `P` |
| Sigma | $\sigma$ | `\sigma` | $\Sigma$ | `\Sigma` |
| Tau | $\tau$ | `\tau` | $T$ | `T` |
| Phi | $\phi$ | `\phi` | $\Phi$ | `\Phi` |
| Var Phi | $\varphi$ | `\varphi` | | |
| Chi | $\chi$ | `\chi` | $X$ | `X` |
| Psi | $\psi$ | `\psi` | $\Psi$ | `\Psi` |
| Omega | $\omega$ | `\omega` | $\Omega$ | `\Omega` |

---

## 2. Set Theory & Logic

| Symbol | Code | Meaning |
| :--- | :--- | :--- |
| $\forall$ | `\forall` | For all |
| $\exists$ | `\exists` | There exists |
| $\nexists$ | `\nexists` | There does not exist |
| $\in$ | `\in` | Element of |
| $\notin$ | `\notin` | Not element of |
| $\subset$ | `\subset` | Proper subset |
| $\subseteq$ | `\subseteq` | Subset or equal |
| $\cup$ | `\cup` | Union |
| $\cap$ | `\cap` | Intersection |
| $\setminus$ | `\setminus` | Set difference (A \ B) |
| $\emptyset$ | `\emptyset` | Empty set |
| $\mathbb{R}$ | `\mathbb{R}` | Real Numbers |
| $\mathbb{Z}$ | `\mathbb{Z}` | Integers |
| $\mathbb{N}$ | `\mathbb{N}` | Natural Numbers |
| $\mathbb{Q}$ | `\mathbb{Q}` | Rational Numbers |
| $\mathbb{C}$ | `\mathbb{C}` | Complex Numbers |

---

## 3. Relations & Comparison

| Symbol | Code | Meaning |
| :--- | :--- | :--- |
| $\neq$ | `\neq` | Not equal |
| $\approx$ | `\approx` | Approximately |
| $\sim$ | `\sim` | Similar / Distributed as |
| $\cong$ | `\cong` | Congruent / Isomorphic |
| $\equiv$ | `\equiv` | Equivalent / Modular |
| $\le$ | `\le` | Less or equal |
| $\ge$ | `\ge` | Greater or equal |
| $\ll$ | `\ll` | Much less than |
| $\gg$ | `\gg` | Much greater than |
| $\propto$ | `\propto` | Proportional to |
| $\perp$ | `\perp` | Perpendicular / Orthogonal |
| $\parallel$ | `\parallel` | Parallel |

---

## 4. Operators

| Symbol | Code | Meaning |
| :--- | :--- | :--- |
| $\pm$ | `\pm` | Plus-minus |
| $\mp$ | `\mp` | Minus-plus |
| $\times$ | `\times` | Cross product / Multiply |
| $\cdot$ | `\cdot` | Dot product / Multiply |
| $\star$ | `\star` | Convolution / Special op |
| $\ast$ | `\ast` | Asterisk |
| $\oplus$ | `\oplus` | Direct Sum / XOR |
| $\otimes$ | `\otimes` | Tensor Product |
| $\circ$ | `\circ` | Function Composition |
| $\bullet$ | `\bullet` | Bullet |

---

## 5. Arrows

| Symbol | Code | Context |
| :--- | :--- | :--- |
| $\to$ | `\to` | Function mapping / Limit |
| $\mapsto$ | `\mapsto` | Element mapping (x maps to y) |
| $\implies$ | `\implies` | Implication (Logic) |
| $\iff$ | `\iff` | If and only if |
| $\leftarrow$ | `\leftarrow` | Left arrow |
| $\leftrightarrow$ | `\leftrightarrow` | Bi-directional |
| $\uparrow$ | `\uparrow` | Up (Spins/Basis) |
| $\downarrow$ | `\downarrow` | Down |

---

## 6. Calculus & Big Operators

| Symbol | Code | Meaning |
| :--- | :--- | :--- |
| $\sum$ | `\sum` | Summation |
| $\prod$ | `\prod` | Product |
| $\int$ | `\int` | Integral |
| $\oint$ | `\oint` | Contour Integral |
| $\partial$ | `\partial` | Partial derivative |
| $\nabla$ | `\nabla` | Del / Gradient |
| $\infty$ | `\infty` | Infinity |
| $\lim$ | `\lim` | Limit |

---

## 7. Delimiters (Brackets)
*Tip: Use `\left` and `\right` before these to auto-size them.*

| Symbol | Code | Name |
| :--- | :--- | :--- |
| $\{ \}$ | `\{ \}` | Curly Braces |
| $[ ]$ | `[ ]` | Square Brackets |
| $( )$ | `( )` | Parentheses |
| $\langle \rangle$ | `\langle \rangle` | Angle Brackets (Inner Product) |
| $| |$ | `| |` | Pipes (Abs value / Determinant) |
| $\| \|$ | `\| \|` | Double Pipes (Norm) |

---

## 8. Accents & Diacritics

| Symbol | Code | Meaning |
| :--- | :--- | :--- |
| $\hat{a}$ | `\hat{a}` | Hat (Unit vector/Estimator) |
| $\bar{a}$ | `\bar{a}` | Bar (Mean/Conjugate) |
| $\dot{a}$ | `\dot{a}` | Dot (Time derivative) |
| $\ddot{a}$ | `\ddot{a}` | Double Dot |
| $\vec{a}$ | `\vec{a}` | Vector arrow (small) |
| $\tilde{a}$ | `\tilde{a}` | Tilde |
| $\overline{AB}$ | `\overline{AB}` | Long Bar (Segments) |
| $\underline{AB}$ | `\underline{AB}` | Underline |

---

## 9. Miscellaneous

| Symbol | Code | Meaning |
| :--- | :--- | :--- |
| $\dots$ | `\dots` | Ellipsis (Lower) |
| $\cdots$ | `\cdots` | Ellipsis (Centered) |
| $\vdots$ | `\vdots` | Vertical Dots (Matrices) |
| $\ddots$ | `\ddots` | Diagonal Dots (Matrices) |
| $\angle$ | `\angle` | Angle |
| $\triangle$ | `\triangle` | Triangle |
| $\dagger$ | `\dagger` | Dagger (Hermitian adjoint) |