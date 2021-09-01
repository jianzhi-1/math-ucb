# MATH 104
### Introduction to Analysis
UC Berkeley Fall 2021, taught by Prof Koji

- [x] Week 0: Proofs, Real numbers (lec1)
- [x] Week 1: Completeness Axiom, max, min, sup, inf (lec2)

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

#### Series
