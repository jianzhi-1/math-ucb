# EECS 127
### Optimization Models in Engineering
UC Berkeley Spring 2022, taught by Prof Thomas Courtade

- [x] Week 1: Introduction (lec1); Linear algebra review (lec2)
- [ ] Week 2:
- [ ] Week 3:


ℂ, ℝ, Ω, ∞, ∀, ≥, ≤, ∈, ∉, ⊆, ⊂, Ø, →, ×, ‖, Σ, ·, ∀

### Linear Algebra

##### First Principles

##### Norms
- *‖x‖<sub>p</sub> = (Σ<sub>i</sub>x<sub>i</sub><sup>p</sup>)<sup>1/p</sup>*, *p ∈ ℝ*
- *‖x‖<sub>∞</sub> = max<sub>i</sub>|x<sub>i</sub>|*

###### Dual Norm
- For a given norm *‖·‖*, define the **dual norm** *‖·‖<sub>*</sub>* s.t. *‖y‖<sub>*</sub> = max<sub>x</sub> x<sup>T</sup>y* with *‖x‖ ≤ 1*.
  - Intuitively, the dual norm of a vector is the maximum value achieved after applying a linear function with norm *1* to it.
  - On Wikipedia, dual norm is the measure of size for a continuous linear function defined on vector space.
- *x<sup>T</sup>y ≤ ‖x‖‖y‖<sub>*</sub>*

###### Operator Norm
- Given two normed vector spaces *V, W*, a linear map *A:V → W* is **continuous** iff *∃c* s.t. *‖Av‖ ≤ c‖v‖ ∀v ∈ V*
- Intuitively, a continuous operator *A* never increases a vector by more than a factor of *c*.
- Consequence: image of a bounded set is bounded, so all continuous operators are bounded operators.
- *‖A‖<sub>op</sub> := inf\{c ≥ 0 | ‖Av‖ ≤ c‖v‖ ∀v ∈ V}*
- TODO: there are multiple other equivalent definitions

##### Projection

##### Singular Value Decomposition

##### Principal Component Analysis

##### Linear Programming
- Farkas' Lemma: Let *A ∈ ℝ<sup>m×n</sup>* and *b ∈ ℝ<sup>n</sup>*, then **exactly one** of the following assertions is true.
  - There exists *x ∈ ℝ<sup>n</sup>* such that *Ax = b* and *x ≥ 0*.
  - There exists *y ∈ ℝ<sup>m</sup>* such that *A<sup>T</sup>y ≥ 0* and *b<sup>T</sup>y < 0*.

##### Duality

###### Weak Duality

###### Strong Duality Theorem

### Convex Optimization

##### Convex Duality

### Applications

### Matlab
```Matlab
>> x = [1; 2; -3];
>> r2 = norm(x,2); % l2-norm
>> r1 = norm(x,1); % l1 norm
>> rinf = norm(x,inf); % l-infty norm
```


### Exam Area

#### Midterm Prep 😤
- [ ] YY Spring/Fall

#### Final Exam Prep 😤
- [ ] YY Spring/Fall
