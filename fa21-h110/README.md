# MATH H110
### Honors Linear Algebra
UC Berkeley Fall 2021, taught by Prof Alexander Givental

- [x] Week 0: Vectors (lec1)
- [x] Week 1: Conic Sections, Quadratic Forms (lec2), Complex Numbers (lec3)
- [x] Week 2: Classification of Linear Algebra Problems (lec4), Vector Spaces (lec5)
- [ ] Week 3: Bases, Dimension (lec6)
- [ ] Week 4:
- [ ] Week 5:
- [ ] Week 6:
- [ ] Week 7:
- [ ] Week 8:
- [ ] Week 9:

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

#### Determinants

#### Rank

#### Gaussian Elimination

#### Inertia Theorem

#### Minkowski-Hasse Theorem

#### Spectral Theorem

- (Symmetric Matrices) Suppose *A* is a *n x n* real symmetric matrix. Then
  - every eigenvalue λ of *A* is a real number and there exists a real eigenvalue *u* s.t. *Au = λu*
  - eigenvectors corresponding to unique eigenvalues are necessarily orthogonal i.e. *u<sub>i</sub> · u<sub>j</sub> = 0*
  - there exists a real diagonal matrix *D* and an orthogonal matrix *U* such that *A = UDU<sup>T</sup>*, where *D = diag(λ<sub>1</sub>, ..., λ<sub>n</sub>)* and *U = [u<sub>1</sub> ... u<sub>n</sub>]*

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
