# EECS 127
### Optimization Models in Engineering
UC Berkeley Spring 2022, taught by Prof Thomas Courtade

- [x] Week 1: Introduction (lec1); Linear algebra review (lec2)
- [ ] Week 2:
- [ ] Week 3:


ℂ, ℝ, Ω, ∞, ∀, ≥, ≤, ∈, ∉, ⊆, ⊂, Ø, →, ×, ‖, Σ, ·, ∀, ∇, ⇒, ⟨, ⟩, ∂

### Multivariable Calculus
- Gradient of *f:ℝ<sup>n</sup> → ℝ* at *x<sub>0</sub>* is a *n*-vector given by: *∇f = \[∂f/∂x<sub>i</sub>]
- *g(x) = f(Ax + b) ⇒ ∇g = A<sup>T</sup>∇f(Ax + b)* 
- Gradient is perpendicular to level sets, and points in the direction of steepest increase.
- First order approximation of *f(x)*: *f(x<sub>0</sub>) + ∇f(x<sub>0</sub>)<sup>T</sup>(x - x<sub>0</sub>)*
- First order approximation of *f(x)*: *f(x) = f(x<sub>0</sub>) + J(x - x<sub>0</sub>)* where *J* is the **Jacobian matrix** of *f* at *x<sub>0</sub>*. (so *J<sub>ij</sub> = ∂f<sub>i</sub>/∂x<sub>j</sub>*.

### Linear Algebra

##### First Principles
- Hyperplane *H = {x | a<sup>T</sup>x = b}*
- Equivalently, if *x<sub>0</sub> ∈ H*, then a hyperplane is the set of vectors *x* s.t. *x - x<sub>0</sub>* is orthogonal to *a*.
- Projection of *0* to the hyperplane: point *ba* (assuming *a* normalized)
- Geometrically, *|b|* is the length of closest point *x* on the hyperplane from the origin.
- Halfspace *H = {x | a<sup>T</sup>x ≥ b}*
- For any two matrices *A ∈ ℝ<sup>m × n</sup>, B ∈ ℝ<sup>n × m</sup>*, *tr(AB) = tr(BA)*
- The scalar product of two same type matrices is symmetric and is the sum of product of respective components: *⟨A, B⟩ = tr(A<sup>T</sup>B)*

##### Properties of Special Matrices

###### Full Column Rank Matrices
- A matrix *A ∈ ℝ<sup>m × n</sup>* has full column rank if all columns are linearly independent. (implies *m ≥ n*)
- A matrix *A* has full column rank if and only if *∃B ∈ ℝ<sup>n × m</sup>* s.t. *BA = I<sub>n</sub>*
- *A = Q\[R<sub>1</sub> 0]<sup>T</sup>*
- *B = \[R<sub>1</sub><sup>-1</sup> 0]Q<sup>T</sup>*
- *B = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>*
- In general, left inverses are not unique.


###### Full Row Rank Matrices
- A matrix *A ∈ ℝ<sup>m × n</sup>* has full row rank if all rows are linearly independent. (implies *n ≥ m*)
- A matrix *A* has full row rank if and only if *∃B ∈ ℝ<sup>n × m</sup>* s.t. *AB = I<sub>m</sub>*
- *A<sup>T</sup> = Q\[R<sub>1</sub><sup>T</sup> 0]<sup>T</sup>*
- *A = \[R<sub>1</sub><sup>T</sup> 0]Q<sup>T</sup>*
- *B = A<sup>T</sup>(AA<sup>T</sup>)<sup>-1</sup>*
- In general, right inverses are not unique.


###### Symmetric Matrices

###### Orthogonal Matrices
- *U<sup>T</sup>U = UU<sup>T</sup> = I<sub>n</sub>*
- Preserves length and angles: *⟨Ux, Uy⟩ = ⟨x, y⟩*

###### Dyads
- *A = uv<sup>T</sup>* for some *u, v*
- *Ax = uv<sup>T</sup>x = (v<sup>T</sup>x)u ∈ Span(u) ∀x*

ℂ, ℝ, Ω, ∞, ∀, ≥, ≤, ∈, ∉, ⊆, ⊂, Ø, →, ×, ‖, Σ, ·, ∀, ∇, ⇒, ⟨, ⟩

##### QR Decomposition
- Factorizes a matrix *A = QR* where *Q* is orthogonal (i.e. *Q<sup>T</sup>Q = I*) and *R* is upper-triangular.
- *A ∈ ℝ<sup>m × n</sup>* is full rank (*rank(A) = n =* number of columns of *A*)
  - *Q = \[q<sub>1</sub> ... q<sub>n</sub>]* where *q<sub>i</sub>* are the vectors from Gram-Schmidt process on *a<sub>i</sub>*
  - *R ∈ ℝ<sup>n × n</sup>* is equal to the coefficients obtained during Gram-Schmidt (either a projection or a scaling factor)
  - *R* is invertible implies *A* is full rank.
- *A ∈ ℝ<sup>m × n</sup>* is **not** full rank
  - Key idea is to permutate the matrix *A* such that all the linearly independent column vectors come first.
  - *AP = Q\[R<sub>1</sub> R<sub>2</sub>]*
  - *Q ∈ ℝ<sup>m × r</sup> = \[q<sub>1</sub> ... q<sub>r</sub>]* where *q<sub>i</sub>* are the vectors from Gram-Schmidt process
  - *R<sub>1</sub> ∈ ℝ<sup>r × r</sup>* is a square, invertible, upper-triangular matrix and equal to the coefficients obtained during Gram-Schmidt
  - *R<sub>2</sub> ∈ ℝ<sup>r × (n-r)</sup>* is the equal to the coefficients obtained during Gram-Schmidt of the dependent column vectors of *A*
  - *P* is a permutation (therefore orthogonal) matrix that moves all independent column vectors to the left
- Full QR Decomposition
  - Key idea: append *I<sub>m</sub>* to the matrix *A*
  - *AP = QR*
  - *Q ∈ ℝ<sup>m × m</sup>* is always orthogonal (since we can always find *m* independent vectors)
  - *R ∈ ℝ<sup>m × (n+m)</sup> = \[\[R<sub>1</sub> R<sub>2</sub>] \[0 0]]* where *R<sub>1</sub>* is invertible and gives *rank(A)*.
  - *P* is a permutation (therefore orthogonal) matrix

##### Norms
###### *l<sub>p</sub>* Norm
- *‖x‖<sub>p</sub> = (Σ<sub>i</sub>x<sub>i</sub><sup>p</sup>)<sup>1/p</sup>*, *p ∈ ℝ*
- *‖x‖<sub>∞</sub> = max<sub>i</sub>|x<sub>i</sub>|*

###### Dual Norm
- For a given norm *‖·‖*, define the **dual norm** *‖·‖<sub>\*</sub>* s.t. *‖y‖<sub>\*</sub> = max<sub>x</sub> x<sup>T</sup>y* with *‖x‖ ≤ 1*.
  - Intuitively, the dual norm of a vector is the maximum value achieved after applying a linear function with norm *1* to it.
  - On Wikipedia, dual norm is the measure of size for a continuous linear function defined on vector space.
- *x<sup>T</sup>y ≤ ‖x‖‖y‖<sub>\*</sub>*
- Norm dual to the Euclidean norm is itself.
- Norm dual to the *l<sub>∞</sub>* norm is the *l<sub>1</sub>* norm

###### Operator Norm
- Given two normed vector spaces *V, W*, a linear map *A:V → W* is **continuous** iff *∃c* s.t. *‖Av‖ ≤ c‖v‖ ∀v ∈ V*
- Intuitively, a continuous operator *A* never increases a vector by more than a factor of *c*.
- Consequence: image of a bounded set is bounded, so all continuous operators are bounded operators.
- *‖A‖<sub>op</sub> := inf\{c ≥ 0 | ‖Av‖ ≤ c‖v‖ ∀v ∈ V}*
- TODO: there are multiple other equivalent definitions

###### Frobenius Norm
- *‖A‖<sub>F</sub> = sqrt(Tr(A<sup>T</sup>A))*
- Equivalent to the Euclidean norm of treating *A* as a vector of length *nm*
- Invariant under orthonormal transformation of basis
- Intuitively, captures the *average effect of noise*.

###### Largest Singular Value (LSV) Norm
- *‖A‖<sub>LSV</sub> = max<sub>v | ‖v‖<sub>2</sub> &lt; 1</sub> ‖Av‖<sub>2</sub>*
- Intuitively, captures the *worst case effect of noise*.

ℂ, ℝ, Ω, ∞, ∀, ≥, ≤, ∈, ∉, ⊆, ⊂, Ø, →, ×, ‖, Σ, ·, ∀, ∇, ⇒, ⟨, ⟩
###### Variant of LSV Norm
- *‖A‖<sub>∞, 1</sub> = max<sub>v | ‖v‖<sub>∞</sub> &lt; 1</sub> ‖Av‖<sub>1</sub>*
- Intuitively, captures the *worst case effect of noise*, but considers all vectors *v* with largest component less than *1*.

##### Projection
- Line *x<sub>0</sub> + tu*, *u* not necessarily normalized; point *x*.
- Optimal *t*: *t<sup>\*</sup> = (u<sup>T</sup>(x - x<sub>0</sub>)/(u<sup>T</sup>u)*
- Projected vector: *z<sup>\*</sup> = x<sub>0</sub> + (u<sup>T</sup>(x - x<sub>0</sub>))/(u<sup>T</sup>u) u*

##### Singular Value Decomposition

##### Principal Component Analysis

##### Linear Programming
- Farkas' Lemma: Let *A ∈ ℝ<sup>m×n</sup>* and *b ∈ ℝ<sup>n</sup>*, then **exactly one** of the following assertions is true.
  - There exists *x ∈ ℝ<sup>n</sup>* such that *Ax = b* and *x ≥ 0*.
  - There exists *y ∈ ℝ<sup>m</sup>* such that *A<sup>T</sup>y ≥ 0* and *b<sup>T</sup>y < 0*.

### Duality

###### Conjugate (Fenchel) Duality

###### Weak Duality

###### Strong Duality Theorem

##### Convex Duality

### Optimization

##### Conic Optimization

##### Convex Optimization



### Applications

### Bag of Tricks
- Inequalities (AM-GM, CS, Holder, Muirhead, Jensen, Power)
- Geometric interpretation
- Smoothing

### Matlab
```Matlab
>> x = [1; 2; -3];
>> r2 = norm(x,2); % l2-norm
>> r1 = norm(x,1); % l1 norm
>> rinf = norm(x,inf); % l-infty norm
```

```Matlab
>> [Q,R] = qr(A,0); % A is a mxn matrix, Q is mxn orthogonal, R is nxn upper triangular
```

```Matlab
>> Ainv = inv(A); % produces the inverse of a square, invertible matrix
```

```Matlab
>> frob_norm = norm(A,'fro');
>> lsv_norm = norm(A);
```


### Exam Area

#### Midterm Prep 😤
- [ ] YY Spring/Fall

#### Final Exam Prep 😤
- [ ] YY Spring/Fall
