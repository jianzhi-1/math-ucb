# MATH H110
### Honors Linear Algebra
UC Berkeley Fall 2021, taught by Prof Alexander Givental

- [x] Week 0: Vectors (lec1)
- [x] Week 1: Conic Sections, Quadratic Forms (lec2), Complex Numbers (lec3)
- [ ] Week 2:
- [ ] Week 3:

### Notes

#### Quadratic Forms

###### Ellipse
- Defined as set of points with the same sum of distance to two points (the foci)
- *(x/α)<sup>2</sup> + (y/β)<sup>2</sup> = 1*
- *α*, *β* refers to semi-major and semi-minor axes respectively
- Can prove geometrically that foci are at *(±f, 0)* where *f<sup>2</sup> = α<sup>2</sup> - β<sup>2</sup>*
- A light ray generated from one focus reflects at the boundary to end up at the other focus 

###### Parabola
- Defined as set of points of equal distance from a point (the focus) and a line (the directrix)
- *y = kx<sup>2</sup>*
- Can prove geometrically that the focus is *(0, f)* where *f = 1/4k* and the line is *y = -f*
- A light ray perpendicular to the directrix, reflected off the concave portion of the parabola will hit the focus

###### Hyperbola
- Defined as set of points with the same difference of distance to two points (the foci)
- *(x/α)<sup>2</sup> - (y/β)<sup>2</sup> = 1*
- Can prove geometrically that the foci are *(±f, 0)* where *f<sup>2</sup> = α<sup>2</sup> + β<sup>2</sup>*
- A light ray emitted from one foci and reflected off the hyperbola is congruent to a light ray emitted from the other foci to the point of reflection
- Equivalently, the tangent of the hyperbola at that point bisects the angle formed with the two foci

#### LPU Decomposition

#### Spectral Theorem

- (Symmetric Matrices) Suppose *A* is a *n x n* real symmetric matrix. Then
  - every eigenvalue λ of *A* is a real number and there exists a real eigenvalue *u* s.t. *Au = λu*
  - eigenvectors corresponding to unique eigenvalues are necessarily orthogonal i.e. *u<sub>i</sub> · u<sub>j</sub> = 0*
  - there exists a real diagonal matrix *D* and an orthogonal matrix *U* such that *A = UDU<sup>T</sup>*, where *D = diag(λ<sub>1</sub>, ..., λ<sub>n</sub>)* and *U = [u<sub>1</sub> ... u<sub>n</sub>]

#### Jordan Canonical Form

#### Quotient Space

#### Nilpotence

#### Dual Space

#### Annihilators

#### Cornerstones of Linear Algebra

##### Rank Theorem
Any *m x n* matrix *A* can be row **and** column reduced into the following form, where *k = rank(A)*:

[ I<sub>k</sub> 0 ]

[ 0 0 ]

Row and column operations preserve the rank.

##### Inertia Theorem

##### Orthogonal Diagonalization Theorem

##### Jordan Canonical Form Theorem
