# EECS 126
### Probability and Random Processes
UC Berkeley Spring 2022, taught by Prof Kannan Ramchandran

- [x] Week 1: Introduction (lec1); Probability review (lec2)
- [x] Week 2: Distributions (lec3, lec4)
- [ ] Week 3:
- [ ] Week 4:
- [ ] Week 5:
- [ ] Week 6:


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

##### Convergence

##### Law of Large Numbers

##### Discrete-Time Markov Chains

### Random Processes

##### Transforms

##### Central Limit Theorem

##### Information Theory

##### MLE, MAP


### Estimation

### Applications

##### LLSE, MMSE

##### Kalman Filtering, Tracking


### Exam Area

#### Midterm 1 Prep 😤
- [x] 14 Fall
- [ ] YY Spring/Fall

#### Midterm 2 Prep 😤
- [ ] YY Spring/Fall

#### Final Exam Prep 😤
- [ ] YY Spring/Fall
