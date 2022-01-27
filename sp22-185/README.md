# MATH 185
### Introduction to Complex Analysis
UC Berkeley Spring 2022, taught by Prof Ryan Hass

### Topology in ℂ
- \[Open disk] The open disk of radius *r > 0* about *z<sub>0</sub>* is given by *B<sub>r</sub>(z<sub>0</sub>) = {z ∈ ℂ | |z - z<sub>0</sub>| < r}*
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
- A **branch** of *f* is a choice of range s.t. the function *f* becomes well-defined (i.e. *f* is restricted to become single-valued)
- A **branch cut** of *f* are points removed from *f*'s domain to ensure the function is continuous and well-defined on a particular branch.

### Polynomial, Differentiation, Power Series
- A polynomial *P(x, y)* is **analytic** if it is a polynomial in *P(x + iy)*
- A function *f* is **complex differentiable** if *lim<sub>h → 0</sub>(f(z+h) - f(z))/h* exists
- \[Cauchy Riemann Equations]
  - A polynomial is analytic if and only if *iP<sub>x</sub> = P<sub>y</sub>*
  - If a function *f* is differentiable at *z<sub>0</sub>*, then it must satisfy *if<sub>x</sub> = f<sub>y</sub>* (i.e. *u<sub>x</sub> = v<sub>y</sub>* and *u<sub>y</sub> = -v<sub>x</sub>* at *z<sub>0</sub>*
- A function *f* is differentiable at *a* if and only if *∃φ(z)* continuous at *a* and satisfies *f(z) - f(a) = φ(z)(z - a)* for *z ∈ Ω*. Say *f'(a) = φ(a)*.
- A complex differentiable function is geometrically equivalent to the scaling, rotation and translation of a small ball about every single point.
- \[Uniform Convergence] *(f<sub>n</sub>) → f)* **uniformly** if *∃N* s.t. *n > N* implies *|f<sub>n</sub>(z) - f(z)| < ε ∀z*
- \[Weierstrass M-Test] Let *(M<sub>k</sub>)* be a sequence with *M<sub>k</sub> ≥ 0* s.t. *ΣM<sub>k</sub> < ∞*. If *|f<sub>k</sub>(z)| < M<sub>k</sub> ∀k*, then *|Σf<sub>k</sub>(z)|* converges **uniformly and absolutely** on *Ω*.
- A **power series** centered at *z<sub>0</sub>* is of the form *S(z) = Σa<sub>n</sub>(z - z<sub>0</sub>)<sup>n</sup>* where *(a<sub>n</sub>)* is a sequence.
- \[Radius of Convergence] Let *β = lim sup |a<sub>n</sub>|<sup>1/n</sup>*. Then the **radius of convergence** is *R = 1/β*.
  - The power series converges absolutely on the open disk *|z - z<sub>0</sub>| < R*
  - The power series converges uniformly on a smaller closed disk *|z - z<sub>0</sub>| ≤ r < R*
  - The power series diverges for *|z - z<sub>0</sub>| > R*
  - The power series is **continuous** on *|z - z<sub>0</sub>| < R* (proof by *ε/3* trick)
- Power series is infinitely differentiable in the complex plane within its radius of convergence. After differentiation, the radius of convergence stays the same.
- \[Theorem (Uniqueness)] Let *f* be be a power series centered at *z<sub>0</sub>* with radius of convergence *R*. Suppose *∃(z<sub>n</sub>) ∈ B<sub>R</sub>(z<sub>0</sub>) \ \{z<sub>0</sub>}* where *(z<sub>n</sub>) → z<sub>0</sub>* (i.e. *(z<sub>n</sub>)* approaches the center of the power series) and *f(z<sub>n</sub>) = 0 ∀n*. Then *f(z) = 0 ∀z ∈ B<sub>R</sub>*.

##### Series Tests
Absolute convergence implies convergence (proof by triangle inequality).
###### Comparison Test (Basic/Limit) ???
###### Ratio Test
###### Root Test
###### Divergence Test ???
###### Dirichlet Test ???
###### Cauchy Condensation Test ???

ℂ, ℝ, Ω, ∞, ∀, ≥, ≤, ∈, ∉, ⊆, ⊂, Ø, →, ∃, ε, ∩, ≠, ∪, ⊄, Σ, ·

### Holomorphic and Entire Functions
- \[Complex Differentiable] Let *Ω ⊂ ℂ* be open and *f: Ω → ℂ*. Say *f* is **complex differentiable** if *lim<sub>h → 0</sub>(f(z+h) - f(z))/h* exists.
- \[Holomorphic] Let *Ω ⊂ ℂ* be a region and *f: Ω → ℂ*. Say *f* is **holomorphic** at *z<sub>0</sub>* if *f* is complex differentiable in a neighbourhood of *z<sub>0</sub> ∈ Ω*
- \[Holomorphic] If *f* is complex differentiable on *Ω*, say *f* is **holomorphic** on *Ω*.
- Define *H(Ω)* to be the set of all holomorphic functions on *Ω*.
- \[Entire] Say *f:ℂ → ℂ* is **entire** if *f* is complex differentiable everywhere on *ℂ*.
- \[Theorem (Cauchy Riemann + Continuity)] Suppose *f<sub>x</sub>* and *f<sub>y</sub>* exist and are continuous in a neighborhood of *z<sub>0</sub>* and *if<sub>x</sub> = f<sub>y</sub>*, then *f* is differentiable at *z<sub>0</sub>*
- \[Theorem (*f' = 0*)] Let *Ω ⊂ ℂ* be a region and *f ∈ H(Ω)*. If *f' = 0* everywhere in *Ω* then *f* is constant on *Ω*.

⚠️ Possible to have function that is ℂ-differentiable at infinitely many points, but nowhere holomorphic

⚠️ Possible to have function that is continuous everywhere, but ℂ-differentiable only at a point

### Line Integrals in ℂ, Path Independence
- \[Lemma (Triangle Inequality)] Let *g:\[a, b] → ℂ* be piecewise continuous, then *|∫g(x) dx| ≤ ∫|g(x)|dx* over *\[a, b]*
- \[Smooth] Let *\[a, b] ⊂ ℝ* and *γ:\[a, b] → ℂ* define a piecewise differentiable curve *C*. Say *C* is **smooth** if *γ(t) ≠ 0* for all but finite points *t ∈ \[a, b]*. (intuitively, cannot halt for a prolonged period of time while travelling the curve)
- \[Complex Differential] Define the **complex differential** as *dz = dx + i·dy*
- \[Line Integral] Define the **line integral** of *f* over *C* as *∫<sub>C</sub> f(x) dz = ∫<sub>C</sub>f(x + iy)(dx + i·dy) = ∫γ(t) γ'(t) dt*

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
