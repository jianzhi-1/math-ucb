# COMPSCI 70
### Discrete Mathematics and Probability Theory
UC Berkeley Fall 2021, taught by Prof Satish Rao and Prof Babak Ayazifar

- [x] Week 10: Random Variables (lec19), Expectation (lec20)
- [x] Week 11: Variance (lec21), Veteran's Day
- [x] Week 12: Joint and Conditional PMF (lec22), Concentration Bounds (lec23)
- [x] Week 13: Continuous Distribution (lec24), Thanksgiving
- [x] Week 14: Normal Distribution (lec25), Estimation (lec26)

### Notes

#### Propositional Logic
- *P ⇒ Q*
  - Contrapositive: *¬Q ⇒ ¬P*
  - Converse: *Q ⇒ P*
  - Equivalent to *¬P ∨ Q*

#### Stable Matching
Suppose *A* is bijected to *B*.

##### Definitions
- Matching: a matching is a disjoint set of *n* *A-B* pairs.
- Rogue couple: a rogue couple *(a, b)* for a matching *S* is when *a* and *b* prefers each other to their current partners.
- Unstable Matching: If there exists *a ∈ A* and *b ∈ B* such that both prefers each other over their current matching.
- Stable matching: a matching with no rogue couples.
- Optimality: For a given *a ∈ A*, the optimal *B* is the best *b ∈ B* on *a*'s preference list that *a* could be paired with in any stable matching.
- Pessimality: For a given *a ∈ A*, the pessimal *B* is the worst *b ∈ B* on *a*'s preference list that *a* could be paired with in any stable matching.

##### Theorems and Lemmas
- Propose-and-Reject algorithm always halts, and must terminate in at most *n<sup>2</sup>* days.
- For every *a ∈ A*, *a*'s matching can only worsen. (exchange argument)
- (Improvement Lemma) For every *b ∈ B*, *b*'s matching can only improve.
- Propose-and-Reject always terminate with a matching. (monotonicity)
- Propose-and-Reject always terminate with a **stable** matching. (monotonicity)
- Propose-and-Reject always outputs a matching that is *A*-optimal.
- A matching that is *A*-optimal is *B*-pessimal.

##### Lines of Attack
- Exploit monotonicity
- Consider the first day/last day that ...

#### Graphs

##### Definitions

- *K<sub>n</sub>*: complete graph of *n* vertices
- *K<sub>m,n</sub>*: complete, bipartite graph of *m* and *n* nodes
- Hypercubes: *2<sup>n</sup>* vertices, each vertex having *n* edges, total edges *n2<sup>n-1</sup>*
- A **path** between *v<sub>1</sub>* and *v<sub>n</sub>* is a sequence of edges *{(v<sub>1</sub>, v<sub>2</sub>), ..., (v<sub>n - 1</sub>, v<sub>n</sub>)}* where *v<sub>i</sub>* are **distinct**.
- A **cycle** is a path with *v<sub>1</sub> = v<sub>n</sub>* (**distinct** vertices).
- A **walk** is a path without the condition that *v<sub>i</sub>* are distinct.
- A **tour** is a walk that starts and ends at the same vertex.
- An **Eulerian walk** is a walk that uses each edge in *G* exactly once.
- An **Eulerian tour** is an Eulerian walk that is closed.
- A graph is **planar** if it can be drawn on a plane without edges crossing.
- A **connected component** is a *maximal* set of connected vertices
- A **Hamiltonian tour** is a path that visits each vertex exactly once.
- A **tournament** is a directed graph such that for distinct vertices *u*, *v*, exactly one of *(u, v)* and *(v, u)* is an edge.
- An edge is a **bridge** if its removal disconnects the whole graph.
- A dual graph *G<sup>\*</sup>* of a planar graph is the graph formed by transforming faces into vertices and adjacent faces into edges.
  - *(G<sup>\*</sup>)<sup>\*</sup> = G*
  - *G<sup>\*</sup>* is connected
- A ***n*-dimensional hypercube** has *n* vertices, *n2<sup>n-1</sup>* edges
  - Equivalent to two *(n - 1)*-dimensional hypercube with each corresponding vertices connected to each other.
  - Equivalent to assigning each vertex a length *n* bit string, where an edge joins two vertices if their bit string differs by only *1* position.
  - If *S* is a subset of *V* (a *n*-dimensional hypercube) such that *|S| ≤ |V - S|* and *E<sub>S</sub>* denote the edges connecting *S* to *V - S*, then *|E<sub>S</sub>| ≥ |S|*. (prove by induction on *n*)

##### Theorems and Lemmas
- (Euler's Theorem) An undirected graph *G* has an Eulerian tour iff all vertices have even degrees.
- (Euler's Formula) *V + F = E + 2*
- (Kuratowski) A graph is non-planar iff it contains *K<sub>5</sub>* or *K<sub>3,3</sub>*
- \[Four-Color Theorem] Every planar graph can be colored with *4* colors
  - Weaker version: Every planar graph can be colored with *5* colors. (Key idea: exists node of degree *≤ 5*; color-switching *2*-color components remains feasible)
- For a planar graph with at least *2* edges, *E ≤ 3V - 6* (double count face-edge pairs; proves *K<sub>5</sub>*)
- For a planar graph with at least *2* edges and no triangles, *E ≤ 2V - 4* (double count face-edge pairs; proves *K<sub>3,3</sub>*)
- A graph is bipartite iff it does not contain an odd cycle (equivalently, iff it is two-colorable)

#### RSA
- Key *(N, e, d)*. 
  - Only *d* is secret; 
  - *(N, e)* is the public key and are public. 
  - *p, q* are not public
- *N = pq* where *p, q* are primes (usually large, around 512 bits).
- *(e, (p - 1)(q - 1)) = 1*
- *d = e<sup>-1</sup> (mod (p - 1)(q - 1))*
- *E(x) = x<sup>e</sup> (mod N)*
- *D(y) = y<sup>d</sup> (mod N)*
- Only requires *d* to decode.
- \[Prime Number Theorem] *π(n) ≥ n/ln(n)*

#### Error Correcting Codes
- Erasure Errors: given *k* errors, require *n + k* packets; *q > n + k*
- General Errors: given *k* errors, require *n + 2k* packets; *q > n + 2k*
- *Q(x) = P(x)E(x)*, where *E(x)* is the error-locator polynomial.
  - *Q(x)* has degree *n + k - 1* with *n - k* unknown coefficient
  - *E(x)* has degree *k* with *k* unknown coefficient (since *E(x)* is monic)
  - *E(x) = (x - e<sub>1</sub>)...(x - e<sub>k</sub>)*
  - For non-errors, *Q(x<sub>i</sub>) = r<sub>i</sub>E(x<sub>i</sub>)*
  - For errors, *Q(x<sub>i</sub>) = 0* since *E(x<sub>i</sub>) = 0*

#### Hamming Distance
- Represent a string of codewords as vector ***s*** of length *|**s**| = L*.
  - For erasure errors, *L ≥ n + k*.
  - For general errors, *L ≥ n + 2k*.
- The **Hamming distance** between two strings ***s***, ***r*** is the number of positions in which they differ: *d(**s**, **r**) = Σ(r<sub>i</sub> ≠ s<sub>i</sub>)*
- The **minimum distance** of a code is the minimum distance between two distinct codewords: *min<sub>**m** ≠ **m'**</sub>d(**m**, **m'**)*
  - Corollary: If the minimum distance is 1, then there is no protection against errors and erasures.
  - Corollary: If the minimum distance is *k + 1* or better, then the code can recover from *k* erasure errors.
  - Corollary: If the minimum distance is *k* or less, then there is a codeword pair for which erasing *k* positions would make the pair ambiguous.
  - Corollary: If the minimum distance is *2d*, then an attacker can corrupt *d* characters to make it ambiguous for the decoder.
- Theorem: The Reed Solomon code that takes *n* message characters to a codeword of size *n + 2k* has minimum distance *2k + 1*. (prove by showing *2k + 1* ≥ minimum distance and *2k + 1* ≤ minimum distance)

#### Countability and Computability

- Derangement Theorem: For *n ≥ 3*, *D<sub>n</sub> = (n - 1)(D<sub>n-1</sub> + D<sub>n-2</sub>)*. (prove by recursion)
  - *D<sub>n</sub> = n! Σ (-1)<sup>k</sup>/k!* (prove by PIE)
  - *Q<sub>n</sub> := D<sub>n</sub> - n·D<sub>n-1</sub> ⇒ Q<sub>n</sub> = (-1)<sup>n</sup>*
- Surjective implies *|A| ≥ |B|*
- Injectivity implies *|A| ≤ |B|*
- Cantor's Diagonalization
- Cantor Set
- |P(ℕ)| > |ℕ|
- Schröder–Bernstein Theorem: If there exists injective functions *f: A → B* and *g: B → A* between sets *A* and *B*, then there exists a bijective function *h: A → B*
- Halting Problem
- Godel's Incompleteness Theorem: Any set of axioms is either inconsistent or incomplete.
- Generalized Continuum Hypothesis: If an infinite set's cardinality lies between that of an infinite set *S* and its power set, then it has the same cardinality as either *S* or the power set of *S*.
- Kolmogorov Complexity: minimum program that prints string *s*.

#### Probability (10/19)
- Definitions
  - Sample Space *Ω*
    - Collection of sample points
    - Mutually exclusive (disjoint)
    - Finest-grain (can't make it more granular)
    - Collectively exhaustive (all outcome lies in *Ω*)
    - Set of all possible outcomes in a random experiment
  - Event: a collection of sample points (i.e. a subset of *Ω*)
    - Complement of the event is the complement of the event set in *Ω* (disc 8A)
  - Event Space *Σ*
    - If *Ω* is finite, the *Σ* is the power set of *Ω*.
    - Set of all possible events

Example: I flip a coin until H is obtained.
*Ω = \{H, TH, TTH, ... }* (countably infinite sample space)
An event can be: \{H, TH}
*Σ = \{ \{H}, \{TH}, \{H, TH}, \{TTH}, \{TTH, H}, \{TTH, TH}, \{TTH, TH, H} ... }*

- *P: Σ → ℝ*

Axioms of Probability:
- I. Nonnegativity: for any event *A*, *P(A) ≥ 0*
- II. Normalization: *P(Ω) = 1*
- III. (Finite) Additivity: If *A<sub>1</sub> ∩ A<sub>2</sub> = Φ*, then *P(A<sub>1</sub> ∪ A<sub>2</sub>) = P(A<sub>1</sub>) + P(A<sub>2</sub>)* (valid for finite sample space)

Consequences of the Axioms:
- *P(A) + P(A<sup>C</sup>) = P(Ω) = 1* (by III, then II)
- *0 ≤ P(A) = 1 - P(A<sup>C</sup>) ≤ 1*
- If *A ⊆ B*, *P(A) ≤ P(B)* \[Monotonicity]
  - Since *A ∩ (B - A) = Φ*, *P(B) = P(A) + P(B - A)*. Hence *P(A) = P(B) - P(B - A) ≤ P(B)*.
- *P(B) = Σ<sub>i</sub>P(B ∩ A<sub>i</sub>)* for disjoint *A<sub>i</sub>* s.t. *Σ<sub>i</sub>P(A<sub>i</sub>) = 1*

### (10/21)
Finite Uniform Probability Law
- The probability of an event *E* = *|E|/|Ω|*
  - Example: *P(R) = |{R<sub>1</sub>, R<sub>2</sub>}|/|Ω|*
*P(A|B) = P(A ∩ B)/P(B)*
Independence: *A* and *B* are independent events implies *P(A|B) = P(A)*
Baye's Rule: *P(A|B) = P(B|A) (P(A)/P(B))*

##### Misc

##### Random Variables and Functions

##### Toolbox
(Credits: the last three tools are from Evan Chen's [Expected Use of Probability](https://web.evanchen.cc/handouts/ProbabilisticMethod/ProbabilisticMethod.pdf))
###### Common
1. *𝐄\[X + Y] = 𝐄\[X] + 𝐄\[Y]*
2. *Var\[cX] = c<sup>2</sup>Var\[X]*
3. For **independent** random variables *X, Y*, *𝐄\[XY] = 𝐄\[X]𝐄\[Y]*
4. For **independent** random variables *X, Y*, *Var\[X + Y] = Var\[X] + Var\[Y]*
5. *Var\[X + Y] = Var\[X] + Var\[Y] + 2 Cov\[X, Y]*

- Markov's Inequality
- Chebyshev's Inequality
- Law of Large Numbers
- Alteration
- Union Bound
- Lovasz Local Lemma

##### Distributions
1. Bernoulli Distribution
- Special case of binomial distribution in which a single trial is conducted (i.e. *n = 1*).
- *X ~ Bernoulli(p)*
- *𝐏\[X = 0] = (1 - p)*
- *𝐏\[X = 1] = p*
- *𝐄\[X] = p*
- *Var\[X] = p(1 - p)*

2. Binomial Distribution
- Equivalent to a random variable that counts the number of heads that a single coin with bias *p* and flipped *n* times will yield.
- *X ~ Binom(n, p)*
- *𝐏\[X = i] = <sup>n</sup>C<sub>i</sub>p<sup>i</sup>(1 - p)<sup>n - i</sup>* for *i = 0, 1, ..., n*
- *𝐄\[X] = np*
- *Var\[X] = np(1 - p)*
- Prove by reduction to Binomial experiments + linearity of expectations OR algebra.

3. Geometric Distribution
- Equivalent to a random variable that counts the number of heads that a single coin with bias *p* takes to return a head (including the final toss).
- *X ~ Geometric(p)*
- *𝐏\[X = i] = (1 - p)<sup>i - 1</sup>p* for *i = 1, 2, ...*
- *𝐄\[X] = 1/p*
- *Var\[X] = (1 - p)/p<sup>2</sup>*
- *f(x) = px/(1 - (1 - p)x)*
- Prove by Tail Sum Formula OR state analysis OR conditional expectation OR algebra.

4. Poisson Distribution
- Used for experiments for the number of occurrences in a region of unit size.
- *X ~ Poisson(λ)*
- *𝐏\[X = i] = (λ<sup>i</sup>/i!)e<sup>-λ</sup>* for *i = 0, 1, 2, ...*
- *𝐄\[X] = λ*
- *Var\[X] = λ*
- If *X ~ Poisson(λ)* and *Y ~ Poisson(μ)*, then *X + Y ~ Poisson(λ + μ)* (which can be generalized to *n* Poisson distributions).
- \[Approximation to Binomial] If *X ~ Binom(n, λ/n)*, then *𝐏\[X = i] → (λ<sup>i</sup>/i!)e<sup>-λ</sup>* as *n → ∞*

5. Normal Distribution
- *X ~ N(μ, σ<sup>2</sup>)*

6. Hypergeometric Distribution
- Equivalent to the distribution of the number of red balls from choosing *n < N* balls from *N* balls of which *B* are red and the rest are yellow.
- *X ~ Hypergeometric(N, B, n)*
- *𝐏\[X = k] = <sup>B</sup>C<sub>k</sub><sup>N - B</sup>C<sub>n - k</sub>/<sup>N</sup>C<sub>n</sub>*

7. Uniform Distribution
- *X ~ Uniform(S)* where *S* is a set of values
- Honestly, I just put this in for fun.

##### Covariance
- *Cov\[X, Y] = 𝐄\[(X - μ<sub>X</sub>)(Y - μ<sub>Y</sub>)] = 𝐄\[XY] - 𝐄\[X]𝐄\[Y]*
- *Cov\[X, X] = Var\[X]*
- *Var\[X + Y] = Var\[X] + Var\[Y] + 2 Cov\[X, Y]*
- For independent *X, Y*, *Cov\[X, Y] = 0* (converse not true).
- *Cov\[X, Y]* is bilinear, i.e *Cov\[aX<sub>1</sub> + bX<sub>2</sub>, cY<sub>1</sub> + dY<sub>2</sub>] = ac·Cov\[X<sub>1</sub>, Y<sub>1</sub>] + ad·Cov\[X<sub>1</sub>, Y<sub>2</sub>] + bc·Cov\[X<sub>2</sub>, Y<sub>1</sub>] + bd·Cov\[X<sub>2</sub>, Y<sub>2</sub>]*. (I love Linear Algebra!)
- *Corr\[X, Y] = Cov\[X, Y]/σ<sub>X</sub>σ<sub>Y</sub>*
- *-1 ≤ Corr\[X, Y] = Cov\[X', Y'] ≤ 1* (prove by setting *X' = (X - μ<sub>X</sub>)/σ<sub>X</sub>* and *Y' = (Y - μ<sub>Y</sub>)/σ<sub>Y</sub>*
- *Corr\[X, Y] = 1* ⇒ *Y = AX + B* for *A > 0* (*Y' = X'*)
- *Corr\[X, Y] = -1* ⇒ *Y = AX + B* for *A < 0* (*Y' = -X'*)

##### Probabilistic Bounding
- (Markov's Inequality) For a nonnegative random variable *X*, *𝐏\[X ≥ c] ≤ 𝐄\[X]/c*.
- (Generalized Markov's Inequality) For random variable *Y* with finite mean and positive constants *c* and *r*, *𝐏\[|Y| ≥ c] ≤ 𝐄\[|Y|<sup>r</sup>]/c<sup>r</sup>*.
- (Extended Markov's Inequality) For a random variable *X* not necessarily nonnegative, let *Φ(X)* be a non-negative function which is monotonically increasing for *x > 0* and *α* be a positive constant. Then *𝐏\[X ≥ α] ≤ 𝐄\[Φ(X)]/Φ(α)*.
- (Cantelli's Inequality) *𝐏\[X ≥ α] ≤ σ<sup>2</sup>/(α<sup>2</sup> + σ<sup>2</sup>)*
- (Chebyshev's Inequality) For a random variable *X* with finite expectation *μ* and any positive constant *c*, *𝐏\[|X - μ| ≥ c] ≤ Var\[X]/c<sup>2</sup>*. (prove by generalized Markov's when *r = 2*)
- (Corollary) *𝐏\[|X - μ| ≥ kσ] ≤ 1/k<sup>2</sup>*
- (Law of Large Numbers) Let *X<sub>1</sub>*, *X<sub>2</sub>*, ... be a sequence of random variables and denote *(S<sub>i</sub>)* as its partial sum sequence. Then *𝐏\[|S<sub>n</sub>/n - μ| < ε] → 0* as *n → ∞* for all *ε > 0*. (prove by generalized Markov's)

##### Tricks (up my sleeves)
- Algebra / Calculus / Probability Generating Function (see below)
- Tail Sum Formula: For *X* taking on values *0, 1, 2, ...*, *𝐄\[X] = Σ<sub>i</sub><sup>∞</sup>𝐏\[X ≥ i]*
- *𝐄\[X(X - 1)]*: equivalent to differentiation actually

##### Applications
- Hashing
- Regression/Least Squares

#### Markov Chains
- Transition Probability Matrix: *P<sub>ij</sub> = 𝐏\[X<sub>n+1</sub> = j | X<sub>n</sub> = i]* (due to *amnesic* nature). Equivalently, *P<sub>ij</sub>* denotes the probability that the system transits from state *i* to state *j*.
- ***μ<sup>(k)</sup>*** is a row vector denoting the distribution at step *k*.
- *𝐏\[X<sub>0</sub> = i] = **μ**<sup>(0)</sup><sub>i</sub>*, i.e. ***μ<sup>(k)</sup><sub>j</sub>*** is the probability of being in state enumerated *j* at step *k*; sum over all *j* = 1.
- ***μ**<sup>(n)</sup> = μ<sup>(0)</sup>·P<sup>n</sup>* (incrementing step)
- *𝐏\[X<sub>n</sub> = i] = \[**μ**<sup>(n)</sup>]<sub>i</sub> = \[**μ**<sup>(0)</sup>·P<sup>n</sup>]<sub>i</sub>*

#### Probability Generating Functions


### Exam Area

#### Midterm Prep 😤
See my [Midterm Sheet](https://github.com/jianzhi-1/math-ucb/blob/main/fa21-70/mid-term1sheet.pdf)
- [x] Spring 21 Midterm
- [x] Fall 20 Midterm
- [x] Spring 19 Midterm 1
- [x] Spring 18 Midterm 1

#### Finals Prep 😤
See my [Finals Sheet](https://github.com/jianzhi-1/math-ucb/blob/main/fa21-70/mid-term1sheet.pdf)
- [x] Spring 19
- [x] Fall 20
- [x] Spring 20
- [ ] Spring/Fall/Summer YY Finals
