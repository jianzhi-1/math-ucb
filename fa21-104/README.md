# MATH 104
### Introduction to Analysis
UC Berkeley Fall 2021, taught by Prof Koji Shimizu

- [x] Week 0: Proofs, Real numbers (lec1)
- [x] Week 1: Completeness Axiom, *max*, *min*, *sup*, *inf* (lec2), Convergence, ε-N, "Smart" Estimates (lec3)
- [x] Week 2: Oracles, Limit Theorems (lec4), Monotone Sequences (lec5)
- [x] Week 3: *lim sup*, *lim inf*, Cauchy (lec6), Subsequences and Subsequential Limits (lec7)
- [x] Week 4: Series; Cauchy Criterion; Comparison, Ratio, Root Test (lec8), Midterm 1
- [x] Week 5: Integration Test, Alternate Series Test (lec9), Continuity (lec10)
- [ ] Week 6: Properties of Continuous Functions (lec11)
- [ ] Week 7:
- [ ] Week 8:
- [ ] Week 9: , Midterm 2
- [ ] Week 10:
- [ ] Week 11:
- [ ] Week 12:
- [ ] Week 13:
- [ ] Week 14:
- [ ] Week 15: RRR Week
- [ ] Week 16: Final Exam

### Notes
- Completeness Axiom for reals: Any **nonempty** subset of ℝ that is bounded above (i.e. admits at least 1 upper bound) admits suprenum (as a real).
- Archimedean property: For any *a*, *b* *>0*, exists a natural number *n* s.t. *na > b*.
- Denseness of ℚ: for every *a < b*, exists a rational *r* s.t. *a < r < b*.

#### Monotone Sequences 
- All *monotone* sequences converge (to a real number for bounded sequences) or diverges to ±∞.
- *u<sub>N</sub> = inf{s<sub>n</sub>: n > N}*
- *v<sub>N</sub> = sup{s<sub>n</sub>: n > N}*
- *(u<sub>n</sub>)* is increasing, *(v<sub>n</sub>)* is decreasing
- *lim sup s<sub>n</sub> = lim v<sub>N</sub> = lim sup{s<sub>n</sub>: n > N}*
- *lim inf s<sub>n</sub> = lim u<sub>N</sub> = lim inf{s<sub>n</sub>: n > N}*
- *lim inf s<sub>n</sub> = lim sup s<sub>n</sub>* iff *lim s* is defined

#### Cauchy Sequences
- A sequence *(s<sub>n</sub>)* is **Cauchy** if for each ε > 0, exists *N* s.t. for all *m, n > N*, *|s<sub>n</sub> - s<sub>m</sub>| < ε*
- A sequence is convergent iff it is Cauchy. (backward implies proven by *lim inf s<sub>n</sub> = lim sup s<sub>n</sub>*)
- All Cauchy sequences are bounded.

#### Subsequences
- *n<sub>k</sub> ≥ k*
- There is a subsequence of *(s<sub>n</sub>)* converging to a real *t* iff the set *{n ∈ ℕ: |s<sub>n</sub> - t| < ε}* is infinite for all *ε > 0*.
- If *(s<sub>n</sub>)* is unbounded, it contains a subsequence with limit ±∞.
- (11.3) If subsequence *(s<sub>n</sub>)* converges, then every subsequence converges to the same limit.
- (11.4) Every sequence *(s<sub>n</sub>)* has a monotonic subsequence.
- (Bolzano-Weierstrass) Every bounded sequence has a convergent subsequence. (bounded ⇒ contains monotonic, bounded + monotonic ⇒ convergent)
- (11.7) For any sequence *(s<sub>n</sub>)*, there exists a monotonic subsequence whose limit is *lim sup (s<sub>n</sub>)*. Similarly for *lim inf (s<sub>n</sub>)*.
- (11.8) If S denotes the set of subsequential limits, *sup S = lim sup (s<sub>n</sub>)*, *inf S = lim inf (s<sub>n</sub>)*.
- *lim (s<sub>n</sub>)* exists iff *S* has exactly one element, namely *s<sub>n</sub>*.
- If *(t<sub>n</sub>)* is a sequence in *S ∩ ℝ* (*S* is the set of subsequential limit of a sequence *(s<sub>n</sub>)*) and that *lim t<sub>n</sub> = t*, then *t* belongs to *S*.

#### *lim sup s<sub>n</sub>* and *lim inf s<sub>n</sub>*
- (12.1) If *(s<sub>n</sub>)* converges to *s > 0*, then *lim sup s<sub>n</sub>t<sub>n</sub> = s·lim sup t<sub>n</sub>*
- (12.2) If *(s<sub>n</sub>)* is a sequence of nonzero real numbers, then *lim inf |s<sub>n + 1</sub>/s<sub>n</sub>| ≤ lim inf |s<sub>n</sub>| ≤ lim sup |s<sub>n</sub>| ≤ lim sup |s<sub>n + 1</sub>/s<sub>n</sub>|*
- If *lim |s<sub>n + 1</sub>/s<sub>n</sub>| = L*, then *lim |s<sub>n</sub>|<sup>1/n</sup>| = L*.

#### Series
- A series *Σa<sub>n</sub>* is absolutely convergent if *Σ|a<sub>n</sub>|* converges.
- Absolutely convergent series are convergent.
- A series *Σa<sub>n</sub>* satisfies the Cauchy criterion if for each *ε > 0*, *∃N* s.t. *n ≥ m > N* implies *|Σ<sub>k=m</sub><sup>n</sup>a<sub>k</sub>| < ε*.
- If a series *Σa<sub>n</sub>* converges, then *lim a<sub>n</sub> = 0*.
- Comparison Test: Let *Σa<sub>n</sub>* be a series where *a<sub>n</sub> ≥ 0* for all *n*:
  - If *Σa<sub>n</sub>* converges and *a<sub>n</sub> ≥ |b<sub>n</sub>|* for all *n*, then *Σb<sub>n</sub>* converges.
  - If *Σa<sub>n</sub> = ∞* converges and *b<sub>n</sub> ≥ a<sub>n</sub>* for all *n*, then *Σb<sub>n</sub> = ∞*.
- Ratio Test: A series *Σa<sub>n</sub>* of **non-zero** terms:
  - converges absolutely if *lim sup |a<sub>n+1</sub>/a<sub>n</sub>| < 1*
  - diverges if *lim inf |a<sub>n+1</sub>/a<sub>n</sub>| > 1*
  - otherwise the test gives no information (*lim inf |a<sub>n+1</sub>/a<sub>n</sub>| ≤ 1 ≤ lim sup |a<sub>n+1</sub>/a<sub>n</sub>|*)
- Root Test: Let *Σa<sub>n</sub>* be a series and *α = lim sup |a<sub>n</sub>|<sup>1/n</sup>*, then the series *Σa<sub>n</sub>*
  - converges absolutely if *α < 1*
  - diverges if *α > 1*
  - otherwise the test gives no information (*α = 1*)
- Integral Test: Suppose that *f(x)* is a continuous, positive and decreasing function on interval *\[k, ∞)* and *f(n) = a<sub>n</sub>*, then:
  - *∫<sup>∞</sup><sub>k</sub>f(x) dx* is convergent implies *Σa<sub>n</sub>* is convergent
  - *∫<sup>∞</sup><sub>k</sub>f(x) dx* is divergent implies *Σa<sub>n</sub>* is divergent
- Alternating Series Test:
  - If *a<sub>1</sub> ≥ a<sub>2</sub> ≥ ... ≥ a<sub>n</sub> ≥ ... ≥ 0* and *lim a<sub>n</sub> = 0*, then the alternating series *Σ(-1)<sup>n+1</sup>a<sub>n</sub>* converges.
  - The partial sums *s<sub>n</sub> = Σ(-1)<sup>n+1</sup>a<sub>n</sub>* satisfy *|s - s<sub>n</sub>| ≤ a<sub>n</sub>|* for all *n*.

#### Continuity
- Sequence definition: *f* is continuous at *x<sub>0</sub>* if for every sequence *(x<sub>n</sub>* converging to *x<sub>0</sub>*, *lim f(x<sub>n</sub>) = f(x<sub>0</sub>)*. 
- ε-δ definition: *f* is continuous at *x<sub>0</sub>* if for each *ε > 0*, exists *δ > 0* such that *x ∈ dom(f)* and *|x - x<sub>0</sub>| < δ* implies *|f(x) - f(x<sub>0</sub>)| < ε*
- Let *f, g* be real valued functions continuous at *x<sub>0</sub>* (prove by sequence definition and limit theorems)
  - *|f|* is continuous at *x<sub>0</sub>*
  - *kf* is continuous at *x<sub>0</sub>*
  - *f + g* is continuous at *x<sub>0</sub>*
  - *fg* is continuous at *x<sub>0</sub>*
  - *f/g* is continuous at *x<sub>0</sub>* if *g(x<sub>0</sub>) ≠ 0*
  - *g∘f* is continuous at *x<sub>0</sub>*


- If *f* is a continuous real-valued function on a closed interval *\[a, b]*, then *f* is a bounded function and assumes its maximum and minimum values on the closed interval *\[a, b]*.
- \[Intermediate Value Theorem] If *f* is a continuous real-valued function on interval *I*, then if *a, b ∈ I, a < b* and *f(a) < y < f(b)*, then exists *x ∈ I* such that *f(x) = y*.
- If *f* is a continuous real-valued function on interval *I*, the set *f(I) = \{f(x): x ∈ I}* is also an interval or a single point.
- If *f* is a continuous strictly increasing function on interval *I*, then *f(I)* is an interval *J* and *f<sup>-1</sup>* with domain *J* is also a continuous strictly increasing function on *J*.
- Let *g* be a strictly increasing function on an interval *J* such that *g(J)* is an interval *I*, then *g* is continuous on *J*.
- Let *f* be a one-to-one continuous function on an interval *I*, then *f* is either strictly increasing or strictly decreasing.

#### Uniform Continuity
- Let *f* be a real-valued function defined on *S*, a subset of ℝ. *f* is **uniformly continuous** on *S* if for each *ε > 0*, exists *δ > 0* such that *x, y ∈ S* and *|x - y| < δ* implies *|f(x) - f(y)| < ε*.
- If *f* is uniformly continuous on its domain, then it is continuous on its domain. (from definition)
- If *f* is continuous on a **closed interval** *\[a, b]*, then *f* is uniformly continuous on *\[a, b]*. (prove by Bolzano-Weierstrass)
- If *f* is uniformly continuous on a set *S* and *(s<sub>n</sub>)* is a Cauchy sequence in *S*, then *(f(s<sub>n</sub>))* is a Cauchy sequence.
- A real-valued function *f* on *(a, b)* is uniformly continuous on *(a, b)* iff it can be extended to a continuous function ᵮ on *\[a, b]*. (reverse by interweaving trick)
- Let *f* be a continuous function on an interval *I* (may be bounded or unbounded). Let *I<sup>0</sup>* be the interval obtained by removing from *I* any endpoints that happen to be in *I*. If *f* is differentiable on *I<sup>0</sup>* and if *f'* is bounded on *I<sup>0</sup>*, then *f* is uniformly continuous on *I*.
- If *f* is uniformly continuous on a bounded set *S*, then *f* is a bounded function on *S*. (prove by Bolzano-Weierstrass and Cauchy version of uniform continuity)

#### Limits of Functions
- *lim<sub>x → a<sup>S</sup></sub> f(x) = L* iff for each *ε > 0* there exists *δ > 0* such that *x ∈ S* and *|x - a| < δ* implies *|f(x) - L| < ε*.
- If *f* is a function defined on *J \ {a}* for some open interval *J* containing *a*, then *lim<sub>x → a</sub> f(x)* exists iff the limits *lim<sub>x → a<sup>+</sup></sub> f(x)* and *lim<sub>x → a<sup>-</sup></sub> f(x)* both exist and are equal to each other.

#### Power Series
- Let *β = lim sup |a<sub>n</sub>|<sup>1/n</sup>* and *R = 1/β* (radius of convergence):
  - *|x| < R* implies power series converges
  - *|x| > R* implies power series diverges
- The power series converges for exactly one of the following:
  - all *x ∈ ℝ*
  - only *x = 0*
  - a bounded interval centered at *0* (may be open, half-open or closed)

#### Uniform Convergence
- *(f<sub>n</sub>)* converges uniformly on *S* to a function *f* defined on *S* if for each *ε > 0* and all *x ∈ S*, ∃ N s.t. *n > N* implies *|f<sub>n</sub>(x) - f(x)| < ε|*
- A sequence *(f<sub>n</sub>)* of functions on a set *S* converges uniformly to a function *f* on *S* iff *lim sup{|f(x) - f<sub>n</sub>(x)| : x ∈ S} = 0*.
- (24.3) The uniform limit of continuous functions is continuous. (prove by *ε / 3*)

differentiation and integration of power series

#### Differentiation
derivative
Mean Value Theorem
L'Hôpital Rule

#### Integration
Riemann integral
fundamental theorem of calculus

#### Taylor Series

#### Metric Space

##### Definitions
- A metric space *(S, d)* is a set *S* with a metric/distance function *d* on it that satisfies:
  - *d(x, x) = 0 ∀ x ∈ S*
  - *d(x, y) = d(y, x) ∀ x, y ∈ S*
  - *d(x, z) ≤ d(x, y) + d(y, z) ∀ x, y z ∈ S* (triangle inequality)
- *k*-dimensional Euclidean space *ℝ<sup>k</sup>* is the space of all *k*-tuples.
- A sequence *(s<sub>n</sub>)* in metric space *(S, d)* converges to *s* in *S* if *lim d(s<sub>n</sub>, s) = 0*.
- A sequence is **Cauchy** if for each *ε > 0*, there exists *N* such that *m, n > N ⇒ d(s<sub>m</sub>, s<sub>n</sub>) < ε*.
- A sequence is **bounded** if there exists *M > 0* such that *max{|x<sub>j</sub>|} ≤ M* for all *1 ≤ j ≤ k* for all points in the sequence.
- A metric space *(S, d)* is **complete** if every Cauchy sequence in *S* converges to some element in *S*.
- An element *s<sub>0</sub> ∈ E ⊆ S* is **interior** to *E* if for some *r > 0*, *{s ∈ S: d(s, s<sub>0</sub>) < r} ⊆ E*.
- *E* is **open** in *S* if every point in *E* is interior to *E* i.e. *E = E<sup>0</sup>*.
- *E* is **closed** if its complement *S \ E* is open. 
- The **closure** *E<sup>-</sup>* of a set *E* is the intersection of all closed sets containing *E*.
- The **boundary** of *E* is the set *E<sup>-</sup> \ E<sup>0</sup>*, which contains **boundary points**.
- A family *U* of open sets is an **open cover** for *E* if each point of *E* belongs to at least one set in *U* i.e. *E ⊆ ∪{u: u ∈ U}*.
- A set *E* is **compact** if every open cover of *E* has a finite subcover of *E*.

##### Theorems and Lemmas

- (13.3) A sequence *(x<sup>(n)</sup>)* in *ℝ<sup>k</sup>* converges iff *(x<sub>j</sub><sup>(n)</sup>)* converges in *ℝ* for all *1 ≤ j ≤ k*.
- A sequence *(x<sup>(n)</sup>)* in *ℝ<sup>k</sup>* is Cauchy iff *(x<sub>j</sub><sup>(n)</sup>)* converges in *ℝ* for all *1 ≤ j ≤ k*.
- (13.4) Euclidean *k*-space *ℝ<sup>k</sup>* is complete
- \[Bolzano-Weierstrass] Every bounded sequence in *ℝ<sup>k</sup>* has a convergent subsequence.
- Openness / Closedness
  - The union of any collection of open sets is open.
  - The intersection of finitely many open sets is open.
  - The intersection of any collection of closed sets is closed.
- \[Heine-Borel] A subset *E* of *ℝ<sup>k</sup>* is compact iff it is closed and bounded.
- \[Baire Category Theorem]

#### Darboux Integral

### Exam Area

#### Midterm 1 Prep 😤
- [x] 21 Practice 1
- [x] 21 Practice 2

#### Midterm 2 Prep 😤
- [ ] YY Fall/Spring/Summer

#### Final Exam Prep 😤
- [ ] YY Fall/Spring/Summer
