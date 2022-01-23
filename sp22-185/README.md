# MATH 185
### Introduction to Complex Analysis
UC Berkeley Spring 2022, taught by Prof Ryan Hass

### Symbols
ℂ, ℝ, Ω, ∞, ∀, ≥, ≤, ∈, ∉, ⊆, ⊂, Ø, →, ∃, ε, ∩, ≠, ∪, ⊄

### Topology in ℂ
- \[Open disk] The open disk of radius *r > 0* about *z<sub>0</sub>* is given by *B<sub>r</sub>(z<sub>0</sub>) = {z ∈ ℂ | |z - z<sub>0</sub> < r}*
- \[Open] Say *Ω ⊂ ℂ* is **open** if for every *z ∈ Ω*, *∃r > 0* s.t. *B<sub>r</sub>(z) ⊂ Ω*.
- \[Closed] Say *Ω ⊂ ℂ* is **closed** if *Ω<sup>c</sup>* is open.
- \[Boundary] Define the **boundary** of *Ω ⊂ ℂ* as *∂Ω = {z ∈ ℂ | B<sub>r</sub>(z) ∩ Ω ≠ Ø, B<sub>r</sub>(z) ∩ Ω<sup>c</sup> ≠ Ø}*
- \[Closure] Define the **closure** of *Ω ⊂ ℂ* as *Ω ∪ ∂Ω*.
- \[Bounded] Say *Ω ⊂ ℂ* is **bounded** if *∃M > 0* s.t. *Ω ⊂ B<sub>M</sub>(0)*.
- \[Compact] Say *Ω ⊂ ℂ* is **compact** if *Ω* is closed and bounded.
- \[Connected] Say *Ω ⊂ ℂ* is **connected** if *∃* two disjoint **open** sets *A, B* s.t. *Ω ⊂ A∪B* but *Ω ⊄ A* and *Ω ⊄ B*.
- \[Region] Say *Ω ⊂ ℂ* is a **region** if *Ω* is open and connected.
- \[Complete] A metric space *(S, d)* is **complete** if every Cauchy sequence converges.

##### Theorems and Lemmas
- Let *Ω ⊂ ℂ*. Then the following are equivalent:
  - *Ω* is closed
  - For any sequence *(z<sub>n</sub>) ∈ Ω*, if *(z<sub>n</sub>) → z)*, then *z ∈ Ω* (i.e. *Ω* contains all limit points)
  - *∂Ω ⊂ Ω*
  - *Ω* is equal to its own closure
- The complex plane ℂ is complete.
- Every compact metric space is complete (i.e. every Cauchy sequence has to converge).

### Branches
- Let *Ω ⊂ ℂ* be open, *f: Ω → ℂ* be multivalued. Then *z<sub>0</sub> ∈ ℂ* is a **branch point** of *f* if *f* is continuous around a small circle about *z<sub>0</sub>* but *f(z)* does not return to its original value.
- A **branch** of *f* is a choice of range s.t. the function *f* becomes well-defined (i.e. *f* is restricted to become single-valued*)
- A **branch cut** of *f* are points removed from *f*'s domain to ensure the function is continuous and well-defined on a particular branch.

ℂ, ℝ, Ω, ∞, ∀, ≥, ≤, ∈, ∉, ⊆, ⊂, Ø, →, ∃, ε, ∩, ≠, ∪, ⊄

### Polynomial, Differentiation, Power Series
- A polynomial *P(x, y)* is **analytic** if it is a polynomial in *P(x + iy)*
- A function *f* is **complex differentiable** if *lim<sub>h → 0</sub>(f(z+h) - f(z))/h* exists
- \[Cauchy Riemann Equations]
  - A polynomial is analytic if and only if *iP<sub>x</sub> = P<sub>y</sub>*
  - If a function *f* is differentiable at *z<sub>0</sub>*, then it must satisfy *if<sub>x</sub> = f<sub>y</sub>* (i.e. *u<sub>x</sub> = v<sub>y</sub>* and *u<sub>y</sub> = -v<sub>x</sub>* at *z<sub>0</sub>*
- A function *f* is differentiable at *a* if and only if *∃φ(z)* continuous at *a* and satisfies *f(z) - f(a) = φ(z)(z - a)* for *z ∈ Ω*. Say *f'(a) = φ(a)*.
- A complex differentiable function is geometrically equivalent to the scaling, rotation and translation of a small ball about every single point.

### Holomorphic and Entire Functions

### Line Integrals in ℂ, Path Independence

### Cauchy Integral Formula

### Properties of Holomorphic Functions

### Open Mapping Theorem

### Uniform Convergence and Extensions

### Singularities

### Laurent Series

### Residue Theory

### Counting Zeros

### Improper Integrals

### Conformal Mapping

### Bilinear Transformations

### Exam Area

#### Midterm 1 Prep 😤

#### Midterm 2 Prep 😤

#### Final Exam Prep 😤
