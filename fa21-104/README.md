# MATH 104
### Introduction to Analysis
UC Berkeley Fall 2021, taught by Prof Koji Shimizu

- [x] Week 0: Proofs, Real numbers (lec1)
- [x] Week 1: Completeness Axiom, *max*, *min*, *sup*, *inf* (lec2), Convergence, ε-δ, "Smart" Estimates (lec3)
- [ ] Week 2:
- [ ] Week 3:
- [ ] Week 4:
- [ ] Week 5:

### Notes
- Completeness Axiom for reals: Any **nonempty** subset of R that is bounded above (i.e. admits at least 1 upper bound) admits suprenum (as a real).
- Archimedean property: For any *a*, *b* *>0*, exists a natural number n s.t. *na > b*.
- Denseness of Q: for every *a < b*, exists a rational *r* s.t. *a < r < b*.

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
- There is a subsequence of *(s<sub>n</sub>)* converging to a real *t* iff the set *{n ∈ N: |s<sub>n</sub> - t| < ε}* is infinite for all *ε > 0*.
- If *(s<sub>n</sub>)* is unbounded, it contains a subsequence with limit ±∞.
- If subsequence *(s<sub>n</sub>)* converges, then every subsequence converges to the same limit.
- Every sequence *(s<sub>n</sub>)* has a monotonic subsequence.
- (Bolzano-Weierstrass) Every bounded sequence has a convergent subsequence. (bounded ⇒ contains monotonic, bounded + monotonic ⇒ convergent)
- For any sequence *(s<sub>n</sub>)*, exists a monotonic subsequence whose limit is *lim sup (s<sub>n</sub>)*. Similarly for *lim inf (s<sub>n</sub>)*.
- If S denotes the set of subsequential limits, *sup S = lim sup (s<sub>n</sub>)*, *inf S = lim inf (s<sub>n</sub>)*.
- *lim (s<sub>n</sub>)* exists iff *S* has exactly one element, namely *s<sub>n</sub>*.
- one more 

#### Series

#### Metric Space

#### Darboux Integral
