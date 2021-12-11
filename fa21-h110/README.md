# MATH H110
### Honors Linear Algebra
UC Berkeley Fall 2021, taught by Prof Alexander Givental

- [x] Week 0: Vectors (lec1)
- [x] Week 1: Conic Sections, Quadratic Forms (lec2), Complex Numbers (lec3)
- [x] Week 2: Classification of Linear Algebra Problems (lec4), Vector Spaces (lec5)
- [x] Week 3: Bases, Dimension (lec6), Matrices (lec7)
- [x] Week 4: Transposition, Bilinear and Quadratic Forms (lec8), Hermitian Forms, Permutation (lec9)
- [x] Week 5: Determinant (lec10), Cofactor Theorem, Adjugate Matrix (lec11)
- [x] Week 6: Determinant Formulae (lec12), Determinant Exercises (lec13)
- [x] Week 7: Rank Theorem (lec14), Dimension Counting (lec15)
- [x] Week 8: Gaussian Elimination (lec16), LPU Decomposition and Flags (lec17)
- [x] Week 9: Inertia Theorem (lec18), Sylvester's Rule (lec19)
- [x] Week 10:
- [x] Week 11:
- [x] Week 12:
- [x] Week 13:
- [x] Week 14:

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
- The dual space *V<sup>*</sup>* is the set of all *linear functions* from vector space *V* to scalars *𝕂*.
- *dim V<sup>*</sup> = dim V*
- If *dim V < ∞*, then *V* and *V\** are isomorphic.
- For a given basis of *V*, say *{b<sub>1</sub>, ... , b<sub>n</sub>}*, the **dual basis** is defined to be *{f<sub>1</sub>, ... , f<sub>n</sub>}* where *f<sub>i</sub>(b<sub>j</sub>) = δ<sub>ij</sub>*.
- If *T* maps *V* to *W*, the dual map *T'* maps *W<sup>*</sup>* to *V<sup>*</sup>* such that for *g ∈ W<sup>*</sup>* and *v ∈ V*, *T'(g)(x) = g(T(x))*.

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


#### Linear Maps
##### Properties of Linear Maps
- Any linear map on any linear space *V* is uniquely and completely determined by its action on **any basis** of *V*. (prove by contradiction)

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
  - This implies a bijection between symmetric bilinear forms and quadratic forms.
- *Q(λv) =	λ<sup>2</sup>Q(v)*

- Every quadratic form can be transformed under an orthogonal change of variables *x = By* such that:
  - *Q(x) = Σa<sub>ij</sub>x<sub>i</sub>x<sub>j</sub> = Σλ<sub>i</sub>y<sub>i</sub><sup>2</sup>* where *λ<sub>i</sub>* are the eigenvalues of *A*.

- The signature of a quadratic form is defined as *(n<sub>+</sub>, n<sub>-</sub>)*, where *n<sub>+</sub>* is the number of positive eigenvalues and *n<sub>-</sub>* is the number of negative eigenvalues.

- \[Sylvester's Law of Inertia] Two symmetric square matrices of the same size have the same signature iff they are congruent (i.e. *B = SAS<sup>T</sup>* for some non-singular *S*).

##### Sesquilinear Forms (*𝕂 = ℂ*)
A sesquilinear form is a function *T: V × V → ℂ* that is half-linear in the first argument and linear in the second.
- *T(λu + μv, w) = λ<sup>\*</sup>T(u, w) + μ<sup>\*</sup>T(v, w)*
- *T(w, λu + μv) = λT(w, u) + μT(w, v)*
- *T(v, w) = Σv<sup>\*</sup><sub>i</sub>t<sub>ij</sub>w<sub>j</sub>*
- \[Hermitian Adjoint] *T<sup>†</sup> = (T(v, u))<sup>\*</sup>* 
  - *T<sup>†</sup>* is also sesquilinear
- *t<sub>ij</sub><sup>†</sup> = T<sup>†</sup>(e<sub>i</sub>, e<sub>j</sub>) = (T(e<sub>i</sub>, e<sub>j</sub>))<sup>\*</sup> = (t<sub>ji</sub>)<sup>\*</sup>*
- *T<sup>††</sup> = T* (proven by definition)
- Hermitian-symmetric: *T<sup>†</sup> = T*
  - Hermitian-symmetric matrices must have real diagonals, and diagonally opposite elements are conjugates
  - Every Hermitian-symmetric sesquilinear form *S(z, w)* is uniquely determined by the corresponding Hermitian quadratic form *H(z)*:
  - *S(z, w) = (H(z + w) - H(z + iw))/2*.
- Hermitian-anti-symmetric: *T<sup>†</sup> = -T*
  - Hermitian-anti-symmetric matrices must have imaginary diagonals, and diagonally opposite elements are negative conjugates
- Every sesquilinear form can be uniquely written as the sum of Hermitian-symmetric and Hermitian-anti-symmetric ones.
- *T* is Hermitian symmetric iff *iT* is Hermitian anti-symmetric (prove by definition)
  - *(iT)(u, v) = iT(u, v) = i(T(v, u))<sup>\*</sup> = -(iT(v, u))<sup>\*</sup> = -(iT<sup>†</sup>)(v, u)*
- For matrix form of *T*:
  - *(AB)<sup>†</sup> = B<sup>†</sup>A<sup>†</sup>* (prove by algebra)

##### Hermitian Forms
- **IMPORTANT**: equivalent to Hermitian quadratic form; 
  - **ALL** Hermitian forms are Hermitian symmetric.
  - All Hermitian quadratic forms take on purely *real* value
- Similarly, **anti-Hermitian form** is equivalent to anti-Hermitian quadratic form.
  - **ALL** anti-Hermitian forms are anti-Hermitian symmetric.
  - All anti-Hermitian quadratic forms take on purely *imaginary* value
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
- Adjugate matrix of upper (lower) triangular matrix is upper (lower) triangular.

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
- Binet-Cauchy Formula
  - Let *A* be a *k × n* matrix and *B* be a *n × k* matrix.
  - The determinant of a *k × k* matrix *AB* is given by *det(AB) = Σ<sub>I:|I|=k</sub>(det A<sub>I</sub>)(det B<sub>I</sub>)*
  - When *k = n*, Binet-Cauchy reduces to *det(AB) = det(A)·det(B)*
  - If *k > n*, *det(AB) = 0*.
  - *det(AA<sup>T</sup>) = Σ<sub>I</sub>(det(A<sub>I</sub>)<sup>2</sup>*

#### Tensors
Tensor Products
Einstein's summation convention
Tensor, symmetric, exterior algebras
Exterior forms
Exterior products
Vector Calculus

#### Rank
- *rank(A) = dim A(V)* (rank of a linear map := dimension of its range)
- \[Rank Theorem] A linear map *A : V → W* of rank *r* between *V* (of dimension *n*) and *W* (of dimension *m*) is given by the matrix *E<sub>r</sub>* in suitable bases of *V* and *W*. (prove by constructing a basis in *range(A)*, extend to *W*; take images of those bases, then extend with the basis of *null(A)*)
- \[Rank-Nullity Theorem] *rank(A) + dim null(A) = dim V*
- \[Corollary] For every *m × n* matrix *A* of rank *r* there exist invertible matrices *D* and *C* of sizes *m × m* and *n × n* respectively s.t. *D<sup>-1</sup>AC = E<sub>r</sub>*.
  - *C*: change of coordinate matrix *x = Cx'*
  - *D*: change of coordinate matrix *y = Dy'*
  - *y = Ax ⇔ Dy' = ACx' ⇔ y' = D<sup>-1</sup>ACx'*
- Linear maps between finite dimensional spaces are equivalent (*A' = D<sup>-1</sup>AC*) iff they have the same rank.
- Matrices of adjoint maps with respect to the dual bases are transposed to each other.
  - Adjoint linear maps have the same rank.
  - Maximal number of linearly independent rows of a matrix is equal to the maximal number of linearly independent columns.
  - Rank of a matrix is equal to the maximal *k* for which there is a *k × k* sub-matrix with nonzero determinant.
- For a system of linear equations:
  - The solution set to *Ax = 0* is a linear subspace of dimension *n - r*.
  - The system *Ax = b* is consistent only when *b* lies in the *range(A)* (of dimension *r*)
  - The solution set to *Ax = b* if it exists is an affine subspace in *V* of dimension *n - r* parallel to the kernel of *A*.
  - When *det A ≠ 0*, a system of *n* unknowns and *n* linear equations have a unique solution. Otherwise, the solutions are not unique for some *b* and do not exist for the others.
- If linear subspaces of dimension *k* and *l* together spans a space of dimension *n*, then the intersection is a linear subspace of dimension *k + l - n*.
- *rank(A + B) ≤ rank(A) + rank(B)* (prove by basis)

#### Gaussian Elimination
- *\[A|I<sub>n</sub>] = \[I<sub>n</sub>|A<sup>-1</sup>]*
- \[LPU Decomposition] Every **invertible** matrix *M* can be factored as the product *M = LPU* where *L* is a lower-triangular matrix, *P* is a permutation matrix (an identity matrix with some permutation of the columns) and *U* is an upper-triangular matrix. (prove by extracting out *L* via Gaussian Elimination)
- A sequence of nested subspaces *V<sub>1</sub> ⊂ V<sub>2</sub> ⊂ ...  ⊂ V<sub>n</sub>* forms a **flag** in the space *V = V<sub>n</sub>*
- A **complete flag** obtained when *dim V<sub>i</sub> = i*.
- An invertible linear transformation preserves the standard coordinate flag iff its matrix is upper-triangular.
- Every complete flag can be obtained from any other via an invertible linear transformation. (prove by mapping bases)
- Every complete flag can be transformed into exactly one of the *n!* coordinate flags by invertible linear transformations preserving one of them.
- **Bruhat cells**: set of equivalence classes determined by the intersections of spaces of the flags with the spaces of the fixed flag.
- **LPU Decomposition**: mark out pivot columns first, split elementary row operations which linearly adds one row to a multiple of others to form *L*, then apply *P* to transpose the matrix into the form *U*. Obtain *LPU* as a result.

#### Inertia Theorem
- For a quadratic form *Q*, a basis is *Q*-orthogonal if *Q(e<sub>i</sub>, e<sub>j</sub>) = 0* for all *i ≠ j*.
- Every quadratic form *Q* in a finite dimensional vector space has a *Q*-orthogonal basis. (prove by induction on *dim*)
- Every *Q* can be transformed into exactly one **normal form** *Q = X<sub>1</sub><sup>2</sup> + ... +  X<sub>p</sub><sup>2</sup> - X<sub>p+1</sub><sup>2</sup> - ... -  X<sub>p+q</sub><sup>2</sup>*, *p + q ≤ n* by scaling.
- Normal forms with different *(p, q)* pair are non-equivalent to each other.
- \[Positive Inertia Index] *p* (the number of positive squares in the normal form) is equal to the maximal dimension of the subspace where the quadratic form *Q* is positive. (prove by intersecting subspace)
- \[Negative Inertia Index] *q* (the number of negative squares in the normal form) is equal to the maximal dimension of the subspace where the quadratic form *Q* is negative.
- *p, q* do not depend on the choice of coordinate system.
- For every symmetric *n × n* matrix *Q*, exists an invertible *C* s.t. *C<sup>T</sup>QC* is diagonal. (corollary)
  - In particular, each *Q* can be uniquely transformed into exactly one diagonal matrix of the form *\[I<sub>p</sub> 0 0]\[0 -I<sub>q</sub> 0]\[0 0 0]*.
- Every quadratic form in *ℂ<sup>n</sup>* can be linearly transformed to exactly one of the forms *z<sub>1</sub><sup>2</sup> + ... + z<sub>1</sub><sup>r</sup>* where *0 ≤ r ≤ n*.
  - In particular, each complex symmetric matrix *Q* can be transformed into exactly one of the form *\[I<sub>r</sub> 0]\[0 0]* by the transformation *C → C<sup>T</sup>QC* and *r = rank(Q)*.
- Every Hermitian quadratic form *H* in *ℂ<sup>n</sup>* can be transformed by a linear change of coordinates to exactly one of the normal forms: *|z<sub>1</sub>|<sup>2</sup> + ... + |z<sub>p</sub>|<sup>2</sup> - |z<sub>p+1</sub>|<sup>2</sup> - ... |z<sub>p+q</sub>|<sup>2</sup>*, *0 ≤ p + q ≤ n*. (prove by intersecting subspace, same as for quadratic forms)
- Every anti-Hermitian quadratic form *Q* in *ℂ<sup>n</sup>* can be transformed by a linear change of coordinates to exactly one of the normal forms *i|z<sub>1</sub>|<sup>2</sup> + ... + i|z<sub>p</sub>|<sup>2</sup> - i|z<sub>p+1</sub>|<sup>2</sup> - ... i|z<sub>p+q</sub>|<sup>2</sup>*, *0 ≤ p + q ≤ n*.
- Any Hermitian (anti-Hermitian) matrix can be transformed into exactly one of the normal forms *\[I<sub>p</sub> 0 0]\[0 -I<sub>q</sub> 0]\[0 0 0]* (*\[iI<sub>p</sub> 0 0]\[0 -iI<sub>q</sub> 0]\[0 0 0]*) by transformation of the form *T → C<sup>†</sup>TC* where *C* is an invertible complex matrix.
- \[Sylvester's Rule] Suppose that a Hermitian *n × n* matrix *H* has non-zero leading minors (i.e. *det H ≠ 0*, then the negative inertia index of the corresponding Hermitian form is equal to the number of sign changes in *Δ<sub>0</sub>, ... , Δ<sub>n</sub>*.
  - Any positive definite Hermitian form in *ℂ<sup>n</sup>* can be transformed into *|z<sub>1</sub>|<sup>2</sup> + ... + |z<sub>n</sub>|<sup>2</sup>* by a linear change of coordinates preserving a given complete flag.
  - A Hermitian form in *ℂ<sup>n</sup>* is positive definite iff all its leading minors are positive.
  - Every positive definite Hermitian form in *Cn* has an orthonormal basis *{f<sub>1</sub>, ..., f<sub>n</sub>}* s.t. *f<sub>i</sub> ∈ Span(e<sub>1</sub>, ..., e<sub>k</sub>)*

#### Eigenvalues and Eigenvectors
- \[Cayley Hamilton] Let *A* be a matrix with characteristic polynomial *P*. Then *P(A) = 0*.
  - *A<sup>n</sup>* where *n > rank(A)* can be expressed in smaller powers of *A*.
- The minimal polynomial shares the same roots as the characteristic polynomial.
  - \[Corollary] The minimal polynomial divides the characteristic polynomial (since *P(A) = 0* for characteristic polynomial)

#### Jordan Canonical Form
- The algebraic multiplicity of each eigenvalues give the size of the corresponding Jordan block. 
- The Jordan blocks are independent of each other.
- Geometric multiplicity = dim(ker(A - lambda I))

#### Minkowski-Hasse Theorem (*𝕂 = ℚ* or *𝕂 = ℤ<sub>p</sub>*)
  
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
- Let *A* be a Hermitian matrix. Then *A* is unitarily diagonalizable. (https://mkilme01.pages.tufts.edu/MATH150_02/Chapt5_all.pdf)
- For every matrix *A*, *AA<sup>T</sup>* and *A<sup>T</sup>A* are symmetric and hence, the eigenvectors are all orthogonal.

- (Converse) If *B* is an orthogonal matrix and *B<sup>T</sup>AB* is diagonal, then *A* is symmetric.

#### Euclidean Geometry

#### Jordan Canonical Form

#### Linear Dynamical System

#### Quivers

##### Gabriel's Theorem

#### Nilpotence / Unipotence

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

### Exam Area

#### Final Exam Prep 😤
See my [Finals Sheet](https://github.com/jianzhi-1/math-ucb/blob/main/fa21-h110/MathH110FinalsSheet.pdf)
- [x] 10 Finals
- [x] 14 Finals
- [x] 15 Finals (H)
- [x] 19 Finals
