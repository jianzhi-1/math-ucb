# CS70

### Notes

#### Stable Matching
Suppose *A* is bijected to *B*.
##### Definitions
- Unstable Matching: If there exists *a ∈ A* and *b ∈ B* such that both prefers each other over their current matching.
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

#### RSA and Polynomials

#### Error Correcting Codes
