# CS70
### Discrete Mathematics and Probability Theory
UC Berkeley Fall 2021, taught by Prof Satish Rao

### Notes

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


#### Graphs

##### Definitions

- *K<sub>n</sub>*: complete graph of *n* vertices
- *K<sub>m,n</sub>*: complete, bipartite graph of *m* and *n* nodes
- Hypercubes: *2<sup>n</sup>* vertices, each vertex having *n* edges, total edges *n2<sup>n-1</sup>*
- A **path** between *v<sub>1</sub>* and *v<sub>n</sub>* is a sequence of edges *{(v<sub>1</sub>, v<sub>2</sub>), ..., (v<sub>n - 1</sub>, v<sub>n</sub>)}* where *v<sub>i</sub>* are distinct.
- A **cycle** is a path with *v<sub>1</sub> = v<sub>n</sub>*
- A **walk** is a path without the condition that *v<sub>i</sub>* are distinct
- A **tour** is a walk that starts and ends at the same vertex.
- An **Eulerian walk** is a walk that uses each edge in *G* exactly once.
- An **Eulerian tour** is an Eulerian walk that is closed.
- A graph is **planar** if it can be drawn on a plane without edges crossing.
- A **connected component** is a *maximal* set of connected vertices
- A **Hamiltonian tour** is a path that visits each vertex exactly once.
- A **tournament** is a directed graph such that for distinct vertices *u*, *v*, exactly one of *(u, v)* and *(v, u)* is an edge.

##### Theorems and Lemmas
- (Euler's Theorem) An undirected graph *G* has an Eulerian tour iff all vertices have even degrees.
- (Euler's Formula) V + F = E + 2
- (Kuratowski) A graph is non-planar iff it contains *K<sub>5</sub>* or *K<sub>3,3</sub>*
- Every planar graph can be colored with 5 colors
- For a planar graph, *E ≤ 3V - 6* (double count face-edge pairs)
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

#### Polynomials

#### Error Correcting Codes
