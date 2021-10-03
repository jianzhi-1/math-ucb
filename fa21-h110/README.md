# MATH H110
### Honors Linear Algebra
UC Berkeley Fall 2021, taught by Prof Alexander Givental

- [x] Week 0: Vectors (lec1)
- [x] Week 1: Conic Sections, Quadratic Forms (lec2), Complex Numbers (lec3)
- [x] Week 2: Classification of Linear Algebra Problems (lec4), Vector Spaces (lec5)
- [x] Week 3: Bases, Dimension (lec6), Matrices (lec7)
- [x] Week 4: Transposition, Bilinear and Quadratic Forms (lec8), Hermitian Forms, Permutation (lec9)
- [x] Week 5: Determinant (lec10), Cofactor Theorem, Adjugate Matrix (lec11)
- [ ] Week 6:
- [ ] Week 7:
- [ ] Week 8:
- [ ] Week 9:
- [ ] Week 10:
- [ ] Week 11:
- [ ] Week 12:
- [ ] Week 13:
- [ ] Week 14:
- [ ] Week 15: RRR Week
- [ ] Week 16: Final Exam

### Notes

#### Quadratic Forms

All conic sections can be characterized by the eccentricity ε, the fixed ratio of distance to a fixed point *focus* and a fixed line *directrix*. ε is also *tan(α)/tan(θ)* where *α* is the angle of the cutting plane and *θ* is the angle of cone.

Every quadratic form in a suitably rotated coordinate system assumes the form *Q = A·X<sup>2</sup> + B·Y<sup>2</sup>*.

Every quadratic form has two perpendicular axes of symmetry (*X = 0* and *Y = 0* in the rotated coordinate system).

Completing squares allow you to see the classification of quadratic forms.

###### Ellipse
- Defined as set of points with the same sum of distance to two points (the foci)
- *(x/α)<sup>2</sup> + (y/β)<sup>2</sup> = 1*
- *α*, *β* refers to semi-major and semi-minor axes respectively
- Can prove geometrically that foci are at *(±f, 0)* where *f<sup>2</sup> = α<sup>2</sup> - β<sup>2</sup>*
- A light ray generated from one focus reflects at the boundary to end up at the other focus 
- *ε < 1*

###### Parabola
- Defined as set of points of equal distance from a point (the focus) and a line (the directrix)
- *y = kx<sup>2</sup>*
- Can prove geometrically that the focus is *(0, f)* where *f = 1/4k* and the line is *y = -f*
- A light ray perpendicular to the directrix, reflected off the concave portion of the parabola will hit the focus
- *ε = 1*

###### Hyperbola
- Defined as set of points with the same difference of distance to two points (the foci)
- *(x/α)<sup>2</sup> - (y/β)<sup>2</sup> = 1*
- Can prove geometrically that the foci are *(±f, 0)* where *f<sup>2</sup> = α<sup>2</sup> + β<sup>2</sup>*
- A light ray emitted from one foci and reflected off the hyperbola is congruent to a light ray emitted from the other foci to the point of reflection
- Equivalently, the tangent of the hyperbola at that point bisects the angle formed with the two foci
- *ε > 1*

#### Vector Spaces

##### Direct Sums

##### Affine Subspaces
An *affine subspace* *v + W* is constructed by adding a fixed vector *v ∈ V* to all vectors of subspace *W ⊆ V*. It is parallel to *W*. When *v ∉ W*, the affine subspace is not linear.

##### Dual Space
The dual space *V<sup>*</sup>* is the set of all *linear functions* from vector space *V* to scalars *𝕂*.
*dim V<sup>*</sup> = dim V*

For a given basis of *V*, say *{b<sub>1</sub>, ... , b<sub>n</sub>}*, the **dual basis** is defined to be *{f<sub>1</sub>, ... , f<sub>n</sub>}* where *f<sub>i</sub>(b<sub>j</sub>) = δ<sub>ij</sub>*.

If *T* maps *V* to *W*, the dual map *T'* maps *W<sup>*</sup>* to *V<sup>*</sup>* such that for *g ∈ W<sup>*</sup>* and *v ∈ V*, *T'(g)(x) = g(T(x))*.

##### Dual Dual Space
The double dual is the set of all *linear functions* from *V<sup>*</sup>* to 𝕂. 
The evaluation map *E: v → E<sub>v</sub>* is a linear map mapping *V* to *V<sup>**</sup>*, and provides an isomorphism between *V* and *V<sup>**</sup>*.
*dim V<sup>**</sup> = dim V<sup>*</sup> = dim V*

##### Quotient Space
The *quotient space* of *V* by a subspace *W* is the set of equivalence classes s.t. all vectors from *V* are partitioned into and *v - v' ∈ W ⇒ v, v'* are equivalent mod *W* (i.e. same equivalence class).

##### Quotient Map
The *quotient map π* maps every vector in *V* to its equivalence class in *V/W*. It is a linear map.
*dim V/W = dim V - dim W*

##### Induced Map

##### Annihilator
The *annihilator* of *W*, *W<sup>⊥</sup>*, is the set of all *linear functions* which vanishes on *W ⊆ V*. *W<sup>⊥</sup>* is a subspace of *V<sup>*</sup>*.
*dim W + dim W<sup>⊥</sup> = dim V*


#### Matrices

- **Linear functions** *a: V → 𝕂* are represented by *\[a<sub>1</sub> a<sub>2</sub> ... <sub>n</sub>]*, where *n* is the dimension of *V*.
- **Linear maps*** *A: V → W* are represented by a *m × n* matrix. The value of A<sub>ij</sub> is the value of the linear function *a<sub>i</sub>* on the *e<sub>j</sub>* basis vector. The *j*th column of *A* is the value of *A(e<sub>j</sub>)*. The *i*th row of *A* is the linear function that determines the *i*th value of the coordinate in *W*.
- **Linear transformations**: linear maps from a vector space *V* to itself.
- If *dim V = n* and *dim W = m*, then *Hom(V, W)* has dimension *mn* (prove by isomorphism to *M<sup>m × n</sup>*).

##### Composition
If *C = AB*, then *C<sub>ij</sub>* is the value of the linear function *a<sub>i</sub>* on the vector *B(e<sub>j</sub>)*.
*C<sub>ij</sub> = \[a<sub>i1</sub> a<sub>i2</sub> ... a<sub>in</sub>]\[b<sub>1j</sub> b<sub>2j</sub> ... b<sub>nj</sub>]<sup>T</sup> = Σa<sub>ik</sub>b<sub>kj</sub>*

##### Change of Coordinates
- Vectors
  - A linear transformation represented by matrix *C* that associates *x* (old) a new vector *x'* (new) in the same coordinate system. This means that *x* and *x'* represents the same object actually, just in different basis.
  - *x = Cx'*
  - The *i*th column of *C* is the new coordinate *e'<sub>i</sub>* represented in old coordinates.
- Linear functions
  - A linear function *a: V → 𝕂* is transformed s.t. *a' = aC*. (derived from *a'x' = ax = aCx'*
- Linear maps
  - A linear map *A: V → W* is transformed s.t. *A' = D<sup>-1</sup>AC*.
- Linear transformation
  - A linear transformation *A: V → V* is transformed s.t. *A' = C<sup>-1</sup>AC*. (Similarity transformation)

##### Transposition (Dual/Transposed/Adjoint)
For a linear map *A: V → W*, the dual of *A* is defined to be *A<sup>T</sup>: W<sup>\*</sup> → V<sup>\*</sup>* s.t. *(A<sup>T</sup>a)(v) = a(Av)*.
*A<sup>T</sup>* is linear. By this definition, *(AB)<sup>T</sup> = B<sup>T</sup>A<sup>T</sup>*.

##### Bilinear Forms
Define *B: V × W → 𝕂* such that *B* is linear on *v* and *w*. Then *B* is a bilinear form, and is uniquely determined by the *m × n* matrix of coefficients *B(e<sub>i</sub>, f<sub>j</sub>)*.

- *B(x, y) = x<sup>T</sup>By*
- *B<sub>ij</sub> = B(e<sub>i</sub>, f<sub>j</sub>)*
- For change of coordinates (*x = Dx'*, *y = Cy'*), *B' = D<sup>T</sup>BC*.
- For the special case where *m = n* and *B = I*, *B(x, y) = <x, y> = x<sub>1</sub>y<sub>1</sub> + x<sub>2</sub>y<sub>2</sub> + ... + x<sub>n</sub>y<sub>n</sub>*
- For *B: V × W → 𝕂*, define the **transposed bilinear form** *B<sup>T</sup>: W × V → 𝕂*. *B<sup>T</sup><sub>ij</sub> = B<sub>ji</sub>*
- Each *B: V × W → 𝕂* can be associated to a linear map *B: W → V<sup>*</sup>*. The way I think of it is to suppose one argument of the bilinear form has been fixed (i.e. *B(v, w<sub>o</sub>)* is a linear function on *v* for fixed *w<sub>o</sub>*)

A bilinear form is **positive-definite** if *B(v, v) > 0* for all *v*.
A real *n × n* matrix is positive definite if *x<sup>T</sup>Ax > 0* for all *x ≠ 0*.

- Bilinear form of same vector space
  - Symmetric: *B(u, v) = B(v, u)*
  - Anti-symmetric: *B(u, v) = -B(v, u)*
  - Every bilinear form can be uniquely written as the form of a symmetric and non-symmetric form.
  - Under a change of coordinates, *B' = C<sup>T</sup>BC* remains symmetric/anti-symmetric if *B* is.

##### Quadratic Forms

- A quadratic form in *n* variables is a function with the form *Q(x<sub>1</sub>, ..., x<sub>n</sub>) = Σa<sub>ij</sub>x<sub>i</sub>x<sub>j</sub>*. (i.e. it can be written as *Q(x) = x<sup>T</sup>Ax* for some symmetric matrix *A*)

- A quadratic form can be constructed from bilinear form by *Q<sub>B</sub> = B(v, v) = (A + S)(v, v) = S(v, v)*
- A symmetric bilinear form can be reconstructed from quadratic form *S(u, v) = (S(u + v, u + v) - S(u, u) - S(v, v))/2*
- *Q(λv) =	λ<sup>2</sup>Q(v)*

- Every quadratic form can be transformed under an orthogonal change of variables *x = By* such that:
  - *Q(x) = Σa<sub>ij</sub>x<sub>i</sub>x<sub>j</sub> = Σλ<sub>i</sub>y<sub>i</sub><sup>2</sup>* where *λ<sub>i</sub>* are the eigenvalues of *A*.

- The signature of a quadratic form is defined as *(n<sub>+</sub>, n<sub>-</sub>)*, where *n<sub>+</sub>* is the number of positive eigenvalues and *n<sub>-</sub>* is the number of negative eigenvalues.

- \[Sylvester's Law of Inertia] Two symmetric square matrices of the same size have the same signature iff they are congruent (i.e. *B = SAS<sup>T</sup>* for some non-singular *S*).

##### Hermitian Forms

𝕂 = ℂ
A sesquilinear form is a function *T: V × V → ℂ* that is half-linear in the first argument and linear in the second.
  - *T(λu + μv, w) = λ<sup>\*</sup>T(u, w) + μ<sup>\*</sup>T(v, w)*
  - *T(w, λu + μv) = λT(w, u) + μT(w, v)*
  - *T(v, w) = Σv<sup>\*</sup><sub>i</sub>t<sub>ij</sub>w<sub>j</sub>*
  - The Hermitian adjoint *T<sup>†</sup> = (T(v, u))<sup>\*</sup>* is also sesquilinear
  - *t<sub>ij</sub><sup>†</sup> = T<sup>†</sup>(e<sub>i</sub>, e<sub>j</sub>) = (T(e<sub>i</sub>, e<sub>j</sub>))<sup>\*</sup> = (t<sub>ji</sub>)<sup>\*</sup>*
  - *T<sup>††</sup> = T* (proven by definition)
  - Hermitian-symmetric: *T<sup>†</sup> = T*
    - Hermitian-symmetric matrices must have real diagonals, and diagonally opposite elements are conjugates
    - Corresponding Hermitian quadratic form takes on purely *real* values
  - Hermitian-anti-symmetric: *T<sup>†</sup> = -T*
    - Hermitian-anti-symmetric matrices must have imaginary diagonals, and diagonally opposite elements are negative conjugates
    - Corresponding Hermitian quadratic form takes on purely *imaginary* values
  - Every sesquilinear form can be uniquely written as the sum of Hermitian-symmetric and Hermitian-anti-symmetric ones.
  - *T* is Hermitian symmetric iff *iT* is Hermitian anti-symmetric (prove by definition)

##### Hermitian Quadratic Forms 
- *H(z) = ΣΣz<sup>\*</sup><sub>i</sub>h<sub>ij</sub>z<sub>j</sub>*
- *T(λv, λv) = |λ|<sup>2</sup>T(v, v)*
- *h<sub>ji</sub> = h<sub>ij</sub><sup>*</sup>*
- When *h* is the identity matrix, the corresponding quadratic form is equivalent to *|z<sub>1</sub>|<sup>2</sup> + |z<sub>2</sub>|<sup>2</sup> + ... + |z<sub>n</sub>|<sup>2</sup>*
  
#### Determinants
- *det(A<sup>T</sup>) = det(A)*
- Totally anti-symmetric: *det(\[... a<sub>i</sub> ... a<sub>j</sub> ...]) = -det(\[... a<sub>j</sub> ... a<sub>i</sub> ...])*
- Additive w.r.t columns/rows: *det(\[... a<sub>i</sub>+a'<sub>i</sub> ...]) = det(\[... a<sub></sub> ...]) + det(\[... a'<sub>i</sub> ...])*
- Multiplication of scalar: *det(\[... λa<sub>i</sub> ...]) = λdet(\[... a<sub>i</sub> ...])*
- *det(I) = 1*
- *det(AB) = det(A)det(B)*

- Every totally anti-symmetric function of *n* coordinate vectors of size *n* and is linear in each of them must be proportional to the determinant function.
- *det C* represents the factor of scaling when vectors *v<sub>i</sub>* are replaced by *Cv<sub>i</sub>*

##### Cofactor Theorem
- *M<sub>ij</sub>* denotes the determinant of the *(n - 1)* by *(n - 1)* matrix obtained after crossing out the *i*th row and the *j*th column.
- *A<sub>ij</sub>* denotes the *(ij)*-cofactor, which is just *M<sub>ij</sub>* with a sign.
- Cofactor expansion across *i*th row: *det A = a<sub>i1</sub>A<sub>i1</sub> + a<sub>i2</sub>A<sub>i2</sub> + ... + a<sub>in</sub>A<sub>in</sub>*
- Cofactor expansion across *j*th column: *det A = a<sub>1j</sub>A<sub>1j</sub> + a<sub>2j</sub>A<sub>2j</sub> + ... + a<sub>nj</sub>A<sub>nj</sub>*
- \[Forgery] Applying cofactor theorem to *i*th row and the cofactors of *j*th row: *a<sub>i1</sub>A<sub>j1</sub> + a<sub>i2</sub>A<sub>j2</sub> + ... + a<sub>in</sub>A<sub>jn</sub> = 0* for *i ≠ j*

##### Adjugate Matrix
- Adjugate matrix is the cofactor matrix transposed: *\[adj(A)]<sub>ij</sub> = A<sub>ji</sub>*
- Adjugate matrix summarizes the cofactor theorem and forgery: *A adj(A) = (det A)I = adj(A) A*

##### Cramer's Rule
- For a system of linear equations *Ax = b*, *x<sub>i</sub> = det(\[a<sub>1</sub> ... a<sub>i-1</sub> b a<sub>i+1</sub> ... a<sub>1</sub>])/det(A)* provided that *A* is **invertible**.
- In other words, equivalent to a **forgery** by replacing the *i*th column of *A* with *b*. (prove by expanding out *x = A<sup>-1</sup>b*)

##### Extras
- In a *2 × 2* block matrix assuming *D<sup>-1</sup>* exists, the determinant is *det(A - BD<sup>-1</sup>C)·det(D)*.
- Laplace's Formula: 
  - Say *I* is a multi-index of length *|I| = k* to mean an increasing sequence *i<sub>1</sub> < ... < i<sub>n</sub>*.
  - Define *I'* to be the complement of *I*.
  - Let *A* be a *n × n* matrix and *I, J* be two multi-index of same length.
  - Define *M<sub>IJ</sub> = (IJ)-minor* of *A* as the determinant of the *k × k* matrix formed by the intersection of *I* and *J*.
  - Then, the determinant of *A* is determined over the sum of all possible *J*:
  - *det(A) = Σ<sub>J:|J|=k</sub> (-1)<sup>i<sub>1</sub> + ... + i<sub>k</sub> + j<sub>1</sub> + ... + j<sub>k</sub></sup> M<sub>IJ</sub> M<sub>I'J'</sub>*
- Binet-Cauchy Formula: the determinant of a *k × k* matrix *AB* is given by *det(AB) = Σ<sub>I</sub>(det A<sub>I</sub>)(det B<sub>I</sub>)*

#### Rank

#### Gaussian Elimination

#### Inertia Theorem

#### Minkowski-Hasse Theorem
  
#### Orthogonal and Orthonormal
- Given a *<,>* symmetric bilinear form on a real vector space *V*, two vectors *u, v* are **orthogonal** if *<u, v> = 0*. A basis is **orthonormal** if *<v<sub>i</sub>, v<sub>j</sub>> = 0* for *i ≠ j* and *<v<sub>i</sub>, v<sub>i</sub>> = 1*.
- Given an orthogonal basis, every vector *v ∈ V* can be expressed as *v = Σc<sub>i</sub>v<sub>i</sub>* where *c<sub>i</sub> = <v, v<sub>i</sub>>/<v<sub>i</sub>, v<sub>i</sub>>*. If orthonormal, *c<sub>i</sub> = <v, v<sub>i</sub>>*.

##### Orthogonal Matrix
- A real *n × n* matrix *A* is orthogonal if *A<sup>T</sup>A = I*.
- *A* is orthogonal iff the columns of *A* forms an orthonormal basis.
- If *A*, *B* orthogonal, *AB* is orthogonal. (*(AB)<sup>T</sup>AB = B<sup>T</sup>A<sup>T</sup>AB = I*)
- Left multiplication by *A* preserves dot product. (*<Ax, Ay> = (Ax)<sup>T</sup>Ay = x<sup>T</sup>A<sup>T</sup>Ay = x<sup>T</sup>y = <x, y>*)

##### Gram-Schmidt Process
Given a basis *{v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>n</sub>}*, we can always obtain a set of orthogonal (and thereafter an orthonormal) basis by:
- *w<sub>1</sub> = v<sub>1</sub>*
- *w<sub>2</sub> = v<sub>2</sub> - w<sub>1</sub>(<v<sub>2</sub>, w<sub>1</sub>>/<w<sub>1</sub>, w<sub>1</sub>>)*
- so on

#### Spectral Theorem

- (Symmetric Matrices) Suppose *A* is a *n x n* real symmetric matrix. Then
  - *A* is diagonializable
  - every eigenvalue λ of *A* is a real number and there exists a real eigenvalue *u* s.t. *Au = λu*
  - eigenvectors corresponding to unique eigenvalues are necessarily orthogonal i.e. *u<sub>i</sub> · u<sub>j</sub> = 0*
  - there exists a real diagonal matrix *D* and an orthogonal matrix *U* such that *A = UDU<sup>T</sup>*, where *D = diag(λ<sub>1</sub>, ..., λ<sub>n</sub>)* and *U = [u<sub>1</sub> ... u<sub>n</sub>]*

- (Converse) If *B* is an orthogonal matrix and *B<sup>T</sup>AB* is diagonal, then *A* is symmetric.

#### Euclidean Geometry

#### Jordan Canonical Form

#### Linear Dynamical System

#### Quivers

##### Gabriel's Theorem

#### LPU Decomposition

#### Jordan Canonical Form

#### Nilpotence

#### Cornerstones of Linear Algebra

##### Rank Theorem
Any *m x n* matrix *A* can be row **and** column reduced into the following form, where *k = rank(A)*:

[ I<sub>k</sub> 0 ]

[ 0 0 ]

Row and column operations preserve the rank.

##### Inertia Theorem

Every quadratic form in *n* variables can be transformed by a suitable linear change of variables to exactly one of the normal forms: *X<sub>1</sub><sup>2</sup> + ... X<sub>p</sub><sup>2</sup> - X<sub>p + 1</sub><sup>2</sup> - ... - X<sub>p + q</sub><sup>2</sup>* where *0 ≤ p + q ≤ n*.

##### Orthogonal Diagonalization Theorem

##### Jordan Canonical Form Theorem
