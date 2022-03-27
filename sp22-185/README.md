# MATH 185
### Introduction to Complex Analysis
UC Berkeley Spring 2022, taught by Prof Ryan Hass

- [x] Week 1: 
- [x] Week 2: 
- [x] Week 3:
- [x] Week 4: Holomorphic, Entire (lec10), Cauchy Riemann + Smoothness (lec11); Line integral (lec12)
- [x] Week 5: Line integral (lec13); Path independence (lec14); 
- [x] Week 6: President's Day; Midterm 1; (lec15);
- [ ] Week 7: Cauchy Integral Formula (lec16)

### Topology in ℂ
- \[Open disk] The open disk of radius *r > 0* about *z<sub>0</sub>* is given by *B<sub>r</sub>(z<sub>0</sub>) = {z ∈ ℂ | |z - z<sub>0</sub>| < r}*
- \[Open] Say *Ω ⊂ ℂ* is **open** if for every *z ∈ Ω*, *∃r > 0* s.t. *B<sub>r</sub>(z) ⊂ Ω*.
- \[Closed] Say *Ω ⊂ ℂ* is **closed** if *Ω<sup>c</sup>* is open.
- \[Boundary] Define the **boundary** of *Ω ⊂ ℂ* as *∂Ω = {z ∈ ℂ | B<sub>r</sub>(z) ∩ Ω ≠ Ø, B<sub>r</sub>(z) ∩ Ω<sup>c</sup> ≠ Ø}*
- \[Closure] Define the **closure** of *Ω ⊂ ℂ* as *Ω ∪ ∂Ω*.
- \[Bounded] Say *Ω ⊂ ℂ* is **bounded** if *∃M > 0* s.t. *Ω ⊂ B<sub>M</sub>(0)*.
- \[Compact] Say *Ω ⊂ ℂ* is **compact** if *Ω* is closed and bounded.
- \[Connected] Say *Ω ⊂ ℂ* is **disconnected** if *∃* two disjoint **open** sets *A, B* s.t. *Ω ⊂ A∪B* but *Ω ⊄ A* and *Ω ⊄ B*. Say *Ω ⊂ ℂ* is **connected** otherwise.
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
  - Equivalent definition *∂/∂z* and *∂/∂z̄* (???)
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
###### Divergence Test

###### Dirichlet Test
If *(a<sub>n</sub>)<sub>n</sub>* is a sequence of real numbers and *(b<sub>n</sub>)<sub>n</sub>* is a sequence of complex numbers satisfying:
- *(a<sub>n</sub>)<sub>n</sub>* is monotonic
- *lim<sub>n → ∞</sub> a<sub>n</sub> = 0*
- The absolute value of all partial sums of *(b<sub>n</sub>)<sub>n</sub>* is less than *M ∈ ℝ*. 

Then the series *Σa<sub>n</sub>b<sub>n</sub>* converges.

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
- \[Theorem] If *f:Ω → ℂ* is continuous and *g<sup>N</sup>* is holomorphic for some positive integer *N*, then *g* itself is holomorphic.

⚠️ Possible to have function that is ℂ-differentiable at infinitely many points, but nowhere holomorphic

⚠️ Possible to have function that is continuous everywhere, but ℂ-differentiable only at a point

### Line Integrals in ℂ, Path Independence
- \[Lemma (Triangle Inequality)] Let *g:\[a, b] → ℂ* be piecewise continuous, then *|∫g(x) dx| ≤ ∫|g(x)|dx* over *\[a, b]*
- \[Smooth] Let *\[a, b] ⊂ ℝ* and *γ:\[a, b] → ℂ* define a piecewise differentiable curve *C*. Say *C* is **smooth** if *γ(t) ≠ 0* for all but finite points *t ∈ \[a, b]*. (intuitively, cannot halt for a prolonged period of time while travelling the curve)
- \[Complex Differential] Define the **complex differential** as *dz = dx + i·dy*
- \[Line Integral] Define the **line integral** of *f* over *C* as *∫<sub>C</sub> f(x) dz = ∫<sub>C</sub>f(x + iy)(dx + i·dy) = ∫γ(t) γ'(t) dt*
- \[Smoothly Equivalent] If ∃ one-to-one function *λ:\[c,d] → \[a,b]* s.t. *λ(c) = a*, *λ(d) = b* (i.e. maps endpoints to endpoints) and *λ'(t) > 0* (i.e. progresses in the same way) with *γ<sub>2</sub> = γ<sub>1</sub> ∘ λ*, then say *γ<sub>2</sub>* and *γ<sub>1</sub> ∘ λ* are **smoothly equivalent**. (intuitively, the curves begin and ends in the same position, and traces the same curve, visits points in the same number of times and in the same order)
- For two smoothly equivalent curves, their line integrals are the same: *∫<sub>C1</sub>f = ∫<sub>C2</sub>f*
- \[Reversed Orientation] Define *-C*  as the **reversal** of *C* (i.e. *C* with reversed direction). Then *∫<sub>-C</sub>f = -∫<sub>C</sub>f*
- \[ML Estimate] Let *Ω ⊂ ℂ* be open and *f: Ω → ℂ* and *C* be a smooth curve in *Ω* with length *L = |C|*. If *|f(z)| ≤ M ∀z ∈ ℂ*, then *|∫<sub>C</sub> f(z) dz| ≤ M|C| = ML*
- \[Fundamental Theorem of Complex Line Integral] Let *Ω ⊂ ℂ* be open and *f ∈ H(Ω)*, then for any smooth curve *C ∈ Ω*, *∫<sub>C</sub> f'(z) dz = f(z<sub>1</sub>) - f(z<sub>0</sub>)*, hence can just consider the value at endpoints (NOTE: *f* must be holomorphic on *Ω*)
- \[Path Independence] Let *Ω ⊂ ℂ* be open and *f : Ω → ℂ*. If for all curves *C1, C2 ∈ Ω* that begins at *z<sub>0</sub>* and end at *z<sub>1</sub>*, *∫<sub>C1</sub> f = ∫<sub>C2</sub> f*, then say the line integral of *f* is **path independent**.
- \[Theorem (Path Independence)] Let *Ω ⊂ ℂ* be open and *f : Ω → ℂ*. If *f* has an anti-derivative in *Ω*, then the line integral *∫<sub>C</sub> f* is path independent for all smooth curves *C ∈ Ω*. 
  - \[Corollary] Lack path independence ⇒ No anti-derivative inside *C*
- \[Closed Curve] Say *C* is a **closed** curve if *C* is given by *γ:\[a, b] → ℂ* and *γ(a) = γ(b)*.
- \[Simple Curve] Say *C* is a **simple** curve if *C* is given by *γ:\[a, b] → ℂ* and *γ(t<sub>1</sub>) ≠ γ(t<sub>2</sub>)* for distinct *t<sub>1</sub>, t<sub>2</sub> ∈ \[a, b]*.
- \[Jordan Closed Curve Theorem] Let *C* be a simple closed curve in *ℂ*. Then *C* partitions *ℂ* into two regions, one of them bounded and defined as the **interior** of the curve.
- \[Theorem (Path Independence II)] Let *Ω ⊂ ℂ* be open and *f : Ω → ℂ*. The line integral of *f* is path in dependent in *Ω* if and only if *∮<sub>C</sub> f(z) dz = 0* for all closed curve *C ∈ Ω*
- \[Singularity] ???
- \[Theorem (Integral of Closed Rectangles)] Suppose *f:ℂ → ℂ* is entire and *R* be a rectangle in *C*, then *∮<sub>∂R</sub> f(z) dz = 0*

### Cauchy Integral Formula
- If *f(z)* is analytic in and on a curve *C*, then *∫<sub>C</sub> f(z) dz = 0*.
- Let *f(z)* be an analytic function inside and on a simple, closed curve *C* that is positively oriented, with *z<sub>0</sub>* inside *C*.
- *f(z<sub>0</sub>) = (1/2πi) ∫<sub>C</sub> f(z)/(z-z<sub>0</sub>) dz*
- If *z<sub>0</sub>* is not in *C*, then *∫<sub>C</sub> f(z)/(z-z<sub>0</sub>) dz = 0* since the function *f(z)/(z-z<sub>0</sub>)* will be analytic everywhere in *C*.
- \[Extended] *f<sup>n</sup>(z<sub>0</sub>) = (n!/2πi) ∫<sub>C</sub> f(z)/(z-z<sub>0</sub>)<sup>n+1</sup> dz*
- \[Cauchy–Kovalevskaya] ???
- Let *f* be entire. Then *f(z) = Σf<sup>(k)</sup>(0)/k! z<sup>k</sup>* for all *z ∈ ℂ*, i.e. *f* is equal to its Taylor series centered at *0* for all *z*. In fact, *f* is equal to its Taylor series expansion centered at *a ∈ ℂ* for all *z*.

### Properties of Holomorphic Functions
- Let *f* be entire. Then *f* is infinitely differentiable in *ℂ* and analytic (i.e. *f* can be represented by a power series that converges everywhere in the complex plane).
- Anti-derivative of Caratheodory function exists. In fact, Caratheodory function is also infinitely differentiable.
- Let *f* be entire, and *g* be *f*'s Caratheodory function centered at *a ∈ ℂ*, then *g* is entire and in particular, *g* is infinitely differentiable.
- Let *f* be entire with roots *a<sub>1</sub>, ..., a<sub>k</sub>*. Then *g(x) = f(x)/(x - a<sub>1</sub>)...(x - a<sub>k</sub>)* for *x ≠ a<sub>i</sub>* and *g(a<sub>i</sub>) = lim<sub>z → a<sub>i</sub></sub> g(z)* is entire. (prove by induction)

### Open Mapping Theorem

### Uniform Convergence and Extensions

### Singularities
- *f* has an **isolated singularity** at *z<sub>0</sub>* if *f* is analytic in a deleted neighbourhood of *z<sub>0</sub>* but not at *z<sub>0</sub>* i.e. *f* must be discontinuous at the isolated singularity
- Say *f* has a **removable singularity** at *z<sub>0</sub>* if exists *g* analytic at *z<sub>0</sub>* s.t. *f(z) = g(z)* for all *z* in some neighborhood of *z<sub>0</sub>*.
- If, for *z ≠ z<sub>0</sub>*, *f* can be written in the form *f(z) = A(z)/B(z)* where *A, B* are analytic at *z<sub>0</sub>*, *A(z<sub>0</sub>) ≠ 0*, *B(z<sub>0</sub>) = 0*, then say *f* has a **pole** at *z<sub>0</sub>*. The order of the pole is the same as the order of zero that *B* has at *z<sub>0</sub>*.
- If *f* has neither a removable singularity or pole at *z<sub>0</sub>*, then *f* has an **essential singularity** at *z<sub>0</sub>*.
- \[Riemann's Principle of Removable Singularity] If *f* has an isolated singularity at *z<sub>0</sub>* and if *lim<sub>z → z<sub>0</sub></sub> (z - z<sub>0</sub>)f(z) = 0*, then the singularity is removable.

### Laurent Series

### Residue Theory

### Counting Zeros

### Improper Integrals

### Conformal Mapping

### Bilinear Transformations

### Haunts: Multivariable Calculus
- \[Green's Theorem] can use with Cauchy Riemann to prove the rectangle theorem

### Exam Area

#### Midterm 1 Prep 😤
- [x] 21 Practice 1A
- [x] 21 Practice 1B
- [x] 16 Fall

#### Midterm 2 Prep 😤
- [x] 21 Practice 2A
- [x] 15 Fall

#### Final Exam Prep 😤
