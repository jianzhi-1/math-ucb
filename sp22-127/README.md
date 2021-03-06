# EECS 127
### Optimization Models in Engineering
UC Berkeley Spring 2022, taught by Prof Thomas Courtade

- [x] Week 1: Introduction (lec1); Linear algebra review (lec2)
- [x] Week 2: Projection (lec3); Four fundamental subspaces (lec4)
- [x] Week 3: Matric decompositions (lec5); Singular value decomposition (lec6)
- [x] Week 4: Low rank approximation (lec7); Least squares and variants (lec8)
- [x] Week 5: Review of Linear Algebra (lec9); Linear Programming (lec10)
- [x] Week 6: Quadratic Programming (lec11); Second Order Cone Programming (lec12)
- [x] Week 7: Robust Optimization (lec13); Convexity (lec14)
- [x] Week 8: Separation Theorem (lec15); Farkas' Lemma (lec16)
- [x] Week 9: Midterm; Fenchel Duality (lec17)
- [x] Week 10: ๐ Spring Break ๐
- [x] Week 11: Midterm Review (lec18); Lagrange Duality (lec19)
- [x] Week 12: Slater's Condition (lec20); KKT Conditions (lec21)
- [x] Week 13: Interior Point Algorithm; Finding Feasible Point
- [x] Week 14: Unconstrained Optimization Algorithm; Bisection, Gradient Descent
- [x] Week 15: Support Vector Machine (lec26); Network Economics Problem (lec27)

### Implementation
##### Headers
```python3
%matplotlib inline
import numpy as np
import pandas as pd
import cvxpy as cp
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import genfromtxt
from scipy.optimize import linprog
```

### Numpy
```python3
a = np.array([[1, 2], [3, 4]])
# hstack
# vstack
```

##### Pandas
```python3
data.drop(data.tail(1).index,inplace=True)
arr = data.to_numpy().astype(int)
data = pd.read_csv('senate_data_with_parties.csv', header=None) 
```

##### PCA
```python3
U, s, Vt = np.linalg.svd(arr, full_matrices=False) # Vt is given in the transposed form
```

โ, โ, ฮฉ, โ, โ, โฅ, โค, โ, โ, โ, โ, ร, โ, ร, โ, ฮฃ, ยท, โ, โ, โ, โจ, โฉ, โ, โ

### Multivariable Calculus
- Gradient of *f:โ<sup>n</sup> โ โ* at *x<sub>0</sub>* is a *n*-vector given by: *โf = \[โf/โx<sub>i</sub>]
- *g(x) = f(Ax + b) โ โg = A<sup>T</sup>โf(Ax + b)* 
- Gradient is perpendicular to level sets, and points in the direction of steepest increase.
- First order approximation of *f(x)*: *f(x<sub>0</sub>) + โf(x<sub>0</sub>)<sup>T</sup>(x - x<sub>0</sub>)*
- First order approximation of *f(x)*: *f(x) = f(x<sub>0</sub>) + J(x - x<sub>0</sub>)* where *J* is the **Jacobian matrix** of *f* at *x<sub>0</sub>*. (so *J<sub>ij</sub> = โf<sub>i</sub>/โx<sub>j</sub>*.

### Linear Algebra

##### First Principles
- Hyperplane *H = {x | a<sup>T</sup>x = b}*
- Equivalently, if *x<sub>0</sub> โ H*, then a hyperplane is the set of vectors *x* s.t. *x - x<sub>0</sub>* is orthogonal to *a*.
- Projection of *0* to the hyperplane: point *ba* (assuming *a* normalized)
- Geometrically, *|b|* is the length of closest point *x* on the hyperplane from the origin.
- Halfspace *H = {x | a<sup>T</sup>x โฅ b}*
- For any two matrices *A โ โ<sup>m ร n</sup>, B โ โ<sup>n ร m</sup>*, *tr(AB) = tr(BA)*
- The scalar product of two same type matrices is symmetric and is the sum of product of respective components: *โจA, Bโฉ = tr(A<sup>T</sup>B)*
- \[Rank-Nullity Theorem] For *A โ โ<sup>m ร n</sup>*, *rank(A) + dim null(A) = n*
- \[Fundamental Theorem of Linear Algebra] *rank(A)<sup>โ</sup> = null(A<sup>T</sup>)*

##### Properties of Special Matrices

###### Full Column Rank Matrices
- A matrix *A โ โ<sup>m ร n</sup>* has full column rank if all columns are linearly independent. (implies *m โฅ n*)
- A matrix *A* has full column rank if and only if *โB โ โ<sup>n ร m</sup>* s.t. *BA = I<sub>n</sub>*
- *A = Q\[R<sub>1</sub> 0]<sup>T</sup>*
- *B = \[R<sub>1</sub><sup>-1</sup> 0]Q<sup>T</sup>*
- *B = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>*
- In general, left inverses are not unique.


###### Full Row Rank Matrices
- A matrix *A โ โ<sup>m ร n</sup>* has full row rank if all rows are linearly independent. (implies *n โฅ m*)
- A matrix *A* has full row rank if and only if *โB โ โ<sup>n ร m</sup>* s.t. *AB = I<sub>m</sub>*
- *A<sup>T</sup> = Q\[R<sub>1</sub><sup>T</sup> 0]<sup>T</sup>*
- *A = \[R<sub>1</sub><sup>T</sup> 0]Q<sup>T</sup>*
- *B = A<sup>T</sup>(AA<sup>T</sup>)<sup>-1</sup>*
- In general, right inverses are not unique.
- Full row rank matrices define a linear map that is onto.
- Full row rank if and only if *AA<sup>T</sup>* is invertible.


###### Symmetric Matrices

###### Orthogonal Matrices
- *U<sup>T</sup>U = UU<sup>T</sup> = I<sub>n</sub>*
- Preserves length and angles: *โจUx, Uyโฉ = โจx, yโฉ*

###### Dyads
- *A = uv<sup>T</sup>* for some *u, v*
- *Ax = uv<sup>T</sup>x = (v<sup>T</sup>x)u โ Span(u) โx*

โ, โ, ฮฉ, โ, โ, โฅ, โค, โ, โ, โ, โ, ร, โ, ร, โ, ฮฃ, ยท, โ, โ, โ, โจ, โฉ

##### QR Decomposition
- Factorizes a matrix *A = QR* where *Q* is orthogonal (i.e. *Q<sup>T</sup>Q = I*) and *R* is upper-triangular.
- *A โ โ<sup>m ร n</sup>* is full rank (*rank(A) = n =* number of columns of *A*)
  - *Q = \[q<sub>1</sub> ... q<sub>n</sub>]* where *q<sub>i</sub>* are the vectors from Gram-Schmidt process on *a<sub>i</sub>*
  - *R โ โ<sup>n ร n</sup>* is equal to the coefficients obtained during Gram-Schmidt (either a projection or a scaling factor)
  - *R* is invertible implies *A* is full rank.
- *A โ โ<sup>m ร n</sup>* is **not** full rank
  - Key idea is to permutate the matrix *A* such that all the linearly independent column vectors come first.
  - *AP = Q\[R<sub>1</sub> R<sub>2</sub>]*
  - *Q โ โ<sup>m ร r</sup> = \[q<sub>1</sub> ... q<sub>r</sub>]* where *q<sub>i</sub>* are the vectors from Gram-Schmidt process
  - *R<sub>1</sub> โ โ<sup>r ร r</sup>* is a square, invertible, upper-triangular matrix and equal to the coefficients obtained during Gram-Schmidt
  - *R<sub>2</sub> โ โ<sup>r ร (n-r)</sup>* is the equal to the coefficients obtained during Gram-Schmidt of the dependent column vectors of *A*
  - *P* is a permutation (therefore orthogonal) matrix that moves all independent column vectors to the left
- Full QR Decomposition
  - Key idea: append *I<sub>m</sub>* to the matrix *A*
  - *AP = QR*
  - *Q โ โ<sup>m ร m</sup>* is always orthogonal (since we can always find *m* independent vectors)
  - *R โ โ<sup>m ร (n+m)</sup> = \[\[R<sub>1</sub> R<sub>2</sub>] \[0 0]]* where *R<sub>1</sub>* is invertible and gives *rank(A)*.
  - *P* is a permutation (therefore orthogonal) matrix
- Solving linear equations with QR decomposition: see formulas (TODO)

##### Norms
###### *l<sub>p</sub>* Norm
- *โxโ<sub>p</sub> = (ฮฃ<sub>i</sub>x<sub>i</sub><sup>p</sup>)<sup>1/p</sup>*, *p โ โ*
- *โxโ<sub>โ</sub> = max<sub>i</sub>|x<sub>i</sub>|*

###### Dual Norm
- For a given norm *โยทโ*, define the **dual norm** *โยทโ<sub>\*</sub>* s.t. *โyโ<sub>\*</sub> = max<sub>x</sub> x<sup>T</sup>y* with *โxโ โค 1*.
  - Intuitively, the dual norm of a vector is the maximum value achieved after applying a linear function with norm *1* to it.
  - On Wikipedia, dual norm is the measure of size for a continuous linear function defined on vector space.
- *x<sup>T</sup>y โค โxโโyโ<sub>\*</sub>*
- Norm dual to the Euclidean norm is itself.
- Norm dual to the *l<sub>โ</sub>* norm is the *l<sub>1</sub>* norm

###### Operator Norm
- Given two normed vector spaces *V, W*, a linear map *A:V โ W* is **continuous** iff *โc* s.t. *โAvโ โค cโvโ โv โ V*
- Intuitively, a continuous operator *A* never increases a vector by more than a factor of *c*.
- Consequence: image of a bounded set is bounded, so all continuous operators are bounded operators.
- *โAโ<sub>op</sub> := inf\{c โฅ 0 | โAvโ โค cโvโ โv โ V}*
- TODO: there are multiple other equivalent definitions

###### Frobenius Norm
- *โAโ<sub>F</sub> = sqrt(Tr(A<sup>T</sup>A))*
- Equivalent to the Euclidean norm of treating *A* as a vector of length *nm*
- Invariant under orthonormal transformation of basis
- Intuitively, captures the *average effect of noise*.

###### Largest Singular Value (LSV) Norm
- *โAโ<sub>LSV</sub> = max<sub>v | โvโ<sub>2</sub> &lt; 1</sub> โAvโ<sub>2</sub>*
- Intuitively, captures the *worst case effect of noise*.

###### Variant of LSV Norm
- *โAโ<sub>โ, 1</sub> = max<sub>v | โvโ<sub>โ</sub> &lt; 1</sub> โAvโ<sub>1</sub>*
- Intuitively, captures the *worst case effect of noise*, but considers all vectors *v* with largest component less than *1*.

##### Projection
- Line *x<sub>0</sub> + tu*, *u* not necessarily normalized; point *x*.
- Optimal *t*: *t<sup>\*</sup> = (u<sup>T</sup>(x - x<sub>0</sub>)/(u<sup>T</sup>u)*
- Projected vector: *z<sup>\*</sup> = x<sub>0</sub> + (u<sup>T</sup>(x - x<sub>0</sub>))/(u<sup>T</sup>u) u*

##### Singular Value Decomposition

##### Principal Component Analysis

##### Linear Programming
- Farkas' Lemma: Let *A โ โ<sup>mรn</sup>* and *b โ โ<sup>n</sup>*, then **exactly one** of the following assertions is true.
  - There exists *x โ โ<sup>n</sup>* such that *Ax = b* and *x โฅ 0*.
  - There exists *y โ โ<sup>m</sup>* such that *A<sup>T</sup>y โฅ 0* and *b<sup>T</sup>y < 0*.

### Duality

###### Conjugate (Fenchel) Duality

###### Weak Duality

###### Strong Duality Theorem

##### Convex Duality

โ, โ, ฮฉ, โ, โ, โฅ, โค, โ, โ, โ, โ, ร, โ, ร, โ, ฮฃ, ยท, โ, โ, โ, โจ, โฉ, โ, โ, รฐ

### Optimization

##### Least Squares
Solve *min<sub>x</sub> โAx-yโ<sub>2</sub><sup>2</sup>*
- Definitions
  - *y*: output vector
  - *A*: design matrix
  - *r = Ax - y*: residual vector
- At optimal, *r = Ax - y โ range(A)*
- Optimal solution (supposing *A* is full column rank): *x<sup>\*</sup> = (A<sup>T</sup>A)<sup>-1</sup>A<sup>T</sup>y*
- Need to understand this: https://inst.eecs.berkeley.edu/~ee127/sp21/livebook/thm_set_solns_ls.html (TODO)

###### Equivalence
- Projection to range: Equivalent to projecting *y* onto *range(A)*.
- Minimum distance to feasibility: Find the smallest *รฐy* s.t. *Ax = y + รฐy* becomes feasible.
- Regression: Fit each component of *y* with a corresponding fixed linear input *a<sub>i</sub>* with *x* being the linear combination that governs all inputs: *min<sub>x</sub> ฮฃ(y<sub>i</sub> - a<sub>i</sub><sup>T</sup> x)<sup>2</sup>*
  - Can think of it as: *(a<sub>i</sub>, y<sub>i</sub>)* is a data point
  - Want to fit a linear function *x* to minimise the total error.

##### Linearly Constrained Least Squares
Solve *min<sub>x</sub> โAx-yโ<sub>2</sub><sup>2</sup>*, given *Cx = d*
- Key idea: make sure *x* is in the solution set by augmenting the design matrix
- Reduces to LS problem *min<sub>x</sub> โA'x-y'โ<sub>2</sub><sup>2</sup>* where *A' = AN* and *y' = y - Ax<sub>0</sub>* where *x<sub>0</sub>* is a particular solution.

##### Minimum Norm
Solve *min<sub>x</sub> โxโ<sub>2</sub><sup>2</sup>*, given *Ax = y*

##### Regularized Least Squares
Solve *min<sub>x</sub> โAx-yโ<sub>2</sub><sup>2</sup> + ฮปโxโ<sub>2</sub><sup>2</sup>* where *ฮป > 0* is usually a small parameter.


##### Weighted Regularized Least Squares
Solve *min<sub>x</sub> โAx-yโ<sub>2</sub><sup>2</sup> + x<sup>T</sup>Wx* where *W* is positive definite.
- Solution: unique, given by *x<sup>*</sup> = (A<sup>T</sup>A + W)<sup>-1</sup>A<sup>T</sup>y

##### Kernel Least Squares
???



##### Conic Optimization

##### Convex Optimization



### Applications

##### Dynamical Systems
- See MATH H110 notes

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

```Matlab
>> U = orth(A); % an orthogonal matrix whose columns span range(A)
>> r = rank(A);
>> U = null(A); % an orthogonal matrix whose columns span null(A)
```

```Matlab
>> x = A\y; % finds unique least square solution, given A is full column rank
```


### Exam Area

#### Midterm Prep ๐ค
See my [Midterm Sheet](https://github.com/jianzhi-1/math-ucb/blob/main/sp22-127/EECS127MidtermSheetFinal.pdf)
- [x] 20 Quiz 2
- [x] 20 Quiz 1
- [x] 19 Fall Midterm 1
- [x] 19 Spring Midterm 1
- [x] 18 Fall Midterm 1
- [x] 16 Spring Midterm 1

#### Final Exam Prep ๐ค
See my [Final Sheet](https://github.com/jianzhi-1/math-ucb/blob/main/sp22-127/EECS127FinalSheet.pdf)
