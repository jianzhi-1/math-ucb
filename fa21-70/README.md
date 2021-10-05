# COMPSCI 70
### Discrete Mathematics and Probability Theory
UC Berkeley Fall 2021, taught by Prof Satish Rao

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

##### Theorems and Lemmas
- (Euler's Theorem) An undirected graph *G* has an Eulerian tour iff all vertices have even degrees.
- (Euler's Formula) V + F = E + 2
- (Kuratowski) A graph is non-planar iff it contains *K<sub>5</sub>* or *K<sub>3,3</sub>*
- \[Four-Color Theorem] Every planar graph can be colored with 4 colors
  - Weaker version: Every planar graph can be colored with 5 colors. (Key idea: exists node of degree ≤ 5; color-switching 2-color components remains feasible)
- For a planar graph with at least *2* edges, *E ≤ 3V - 6* (double count face-edge pairs; proves *K<sub>5</sub>*)
- For a planar graph with at least *2* edges and no triangles, *E ≤ 2V - 4* (double count face-edge pairs; proves *K<sub>3,3</sub>*)
- A graph is bipartite iff it does not contain an odd cycle (equivalently, iff it is two-colorable)

#### RSA
- Key *(N, e, d)*. Only *d* is secret; *N* and *e* are public.
- *N = pq* where *p, q* are primes.
- *(e, (p - 1)(q - 1)) = 1*
- *d = e<sup>-1</sup> (mod (p - 1)(q - 1))*
- *E(x) = x<sup>e</sup> (mod N)*
- *D(y) = y<sup>d</sup> (mod N)*
- Only requires *d* to decode.
- \[Prime Number Theorem] *π(n) ≥ n/ln(n)*

#### Error Correcting Codes
- Erasure Errors: given *k* errors, require *n + k* packets
- General Errors: given *k* errors, require *n + 2k* packets
- *Q(x) = P(x)E(x)*
  - *Q(x)* has degree *n + k - 1* with *n - k* unknown coefficient
  - *E(x)* has degree *k* with *k* unknown coefficient (since *E(x)* is monic)
  - *E(x) = (x - e<sub>1</sub>)...(x - e<sub>k</sub>)
  - For non-errors, *Q(x<sub>i</sub>) = r<sub>i</sub>E(x<sub>i</sub>)*
  - For errors, *Q(x<sub>i</sub>) = 0* since *E(x<sub>i</sub>) = 0*

#### Hamming Distance
- The **Hamming distance** between two strings *s*, *r* is the number of positions in which they differ: *d(s, r) = Σ(r<sub>i</sub> ≠ s<sub>i</sub>)*
- The **minimum distance** of a code is the minimum distance between two distinct codewords: *min<sub>m ≠ m'</sub>d(c(m), c(m'))*
- Theorem: The Reed Solomon code that takes *n* message characters to a codeword of size *n + 2k* has minimum distance *2k + 1*

#### Countability and Computability
- Surjective implies *|A| ≥ |B|*
- Injectivity implies *|A| ≤ |B|*
- Cantor's Diagonalization
- Cantor Set
- |P(ℕ)| > |ℕ|
- Schröder–Bernstein Theorem: If there exists injective functions *f: A → B* and *g: B → A* between sets *A* and *B*, then there exists a bijective function *h: A → B*
- Halting Problem
- Godel's Incompleteness Theorem

#### Probability

##### Misc

##### Random Variables and Functions

##### Toolbox
(Credits: the last three tools are from Evan Chen's [Expected Use of Probability](https://web.evanchen.cc/handouts/ProbabilisticMethod/ProbabilisticMethod.pdf))
- Markov's Inequality
- Chebyshev's Inequality
- Law of Large Numbers
- Alteration
- Union Bound
- Lovasz Local Lemma

##### Distributions
- Geometric Distribution
- Poisson Distribution
- Normal Distribution

##### Applications
- Hashing
- Regression/Least Squares

#### Markov Chains


### Exam Area

#### Midterm 1 Prep 😤
- [ ] Fall 20
- [ ] Spring 19 Midterm 1
- [ ] Spring 18 Midterm 1
- [ ] Spring 19 Midterm 2
- [ ] Spring 18 Midterm 2
