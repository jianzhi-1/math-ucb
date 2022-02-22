# EECS 126
### Probability and Random Processes
UC Berkeley Spring 2022, taught by Prof Kannan Ramchandran

- [x] Week 1: Introduction (lec1); Probability review (lec2)
- [x] Week 2: Distributions (lec3, lec4)
- [x] Week 3:
- [x] Week 4: ; Moment Generating Functions (lec8)
- [x] Week 5: Convergence (lec9);
- [ ] Week 6:
- [ ] Week 7:
- [ ] Week 8:
- [ ] Week 9:
- [ ] Week 10:
- [ ] Week 11:
- [ ] Week 12:
- [ ] Week 13:
- [ ] Week 14:
- [ ] Week 15:


### Lab Hacks

##### Numpy Functions
```python3
np.sum(x, axis=1) # sum over rows
np.random.rand(x, y) # generate a random matrix of dimensions x x y in the range [0, 1]
np.count_nonzero(x, axis=1) # count the number of nonzero elements over rows
np.add(x, y)
np.square(x)
np.less_equal(x, 1)
np.random.rand() # generates a random number from 0 to 1
np.random.randint(x) # generates a random integer from [0, x) (note x is exclusive)
np.random.randint(x, size=(3, 5))
np.unique(x)

def contains_duplicates(X):
  return len(np.unique(X)) != len(X)

### Matrix multiplication
return S@A

```

##### Random
```python3
from numpy import random
print(random.rand())
print(random.rand(5))
print(random.rand(3, 3))

random.sample(range(self.num_chunks), n_of_chunks)
```

##### Plotting
```python3
plt.figure() # new figure to plot on
plt.hist(x, range=[xminrange, xmaxrange], bins=np.arange(xminrange, xmaxrange, 1)) # histogram with fixed x range and bin interval
```

##### Commonplace
- Bernoulli
```python3
x = round(random.rand())
```
- Binomial(n, p)
```python3
binomial = random.binomial(n, p, num_trials)
```
##### Itertools
Python library that provides generator for permutations and combinations
```python3
import itertools
itertools.product(RANKS, SUITS)

a = [3, 1, 4, 5]
itertools.combination(a, n) # returns generator of all possible combinations of n-tuple of a
```

### Probability

##### Basics
- *𝔼\[Y] = 𝔼\[𝔼\[Y|X]]*
- *Var\[Y]= Var\[𝔼\[Y|X]] + 𝔼\[Var\[Y|X]]*

##### Convergence and Borel Cantelli Lemmas
- \[Convergence in probability] Let *(Y<sub>n</sub>)<sub>n</sub>* be a sequence of random variables (not necessarily independent) and *a ∈ ℝ*. Say *(Y<sub>n</sub>)<sub>n</sub>* converges to *a* in probability if *∀ε > 0*, *lim<sub>n → ∞</sub> ℙ\[|Y<sub>n</sub> - a| ≥ ε] = 0*.
- \[Convergence with probability 1] Let *(Y<sub>n</sub>)<sub>n</sub>* be a sequence of random variables (not necesarily independent) and *c ∈ ℝ*. Say *(Y<sub>n</sub>)<sub>n</sub>* converges to *c* in probability 1 (or **almost surely**) if *ℙ\[lim<sub>n → ∞</sub>Y<sub>n</sub> = c] = 1*.
  - Equivalent definition: *ℙ\[ω ∈ Ω: lim<sub>n → ∞</sub> Y<sub>n</sub>(ω) = Y(ω)] = 1*
  - Equivalent definition: *∀ε > 0*, *ℙ\[lim sup \{ω ∈ Ω : |X<sub>n</sub>(ω) - X(ω)| > ε\}] = 0*
  - This is the same as pointwise convergence in MATH 104.
  - Implies convergence in probability by Fatou's lemma.
- Convergence with probability 1 implies convergence in probability.

- \[Borel Cantelli Lemma 1] Let *(A<sub>n</sub>)<sub>n</sub>* be a sequence of events such that *Σℙ\[Y<sub>n</sub>] < ∞*. Then *ℙ\[\{A<sub>n</sub> infinitely often}] = 0*. i.e. the set of outcomes where *A<sub>n</sub>* happens infinitely often has measure *0*.
- \[Borel Cantelli Lemma 2]
- \[Continuity of Probability]

##### Law of Large Numbers

##### Transforms

##### Central Limit Theorem

### Random Processes

##### Discrete-Time Markov Chains

##### Information Theory
###### Entropy
Discrete 
*H(X) = -Σ<sub>i</sub> ℙ\[X = x<sub>i</sub>] log ℙ\[X = x<sub>i</sub>]*

### MLE, MAP
##### Maximum Likelihood Estimation
*Θ<sub>MLE</sub> = argmax<sub>Θ</sub> ℙ\[X|Θ]*

##### Maximum A Posteriori
*Θ<sub>MAP</sub> = argmax<sub>Θ</sub> ℙ\[X|Θ]ℙ\[Θ]*

##### Estimation

### Applications

##### Binary Symmetric/Erasure Channel
*p* is the probability of error. *1 - p* is the probability of no error.
pg 119 Walrand

##### LLSE, MMSE

##### Kalman Filtering, Tracking


### Exam Area

#### Midterm 1 Prep 😤
See my [Midterm 1 Sheet](https://github.com/jianzhi-1/math-ucb/blob/main/sp22-126/EECS126_Midterm1Sheet.pdf)
- [x] 21 Fall
- [x] 21 Spring
- [x] 20 Fall
- [x] 20 Spring
- [x] 19 Fall
- [x] 19 Spring
- [x] 18 Fall
- [x] 18 Spring
- [x] 17 Fall
- [x] 14 Fall

#### Midterm 2 Prep 😤
- [ ] YY Spring/Fall

#### Final Exam Prep 😤
- [ ] YY Spring/Fall
