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
- [ ] YY Spring/Fall

#### Midterm 2 Prep 😤
- [ ] YY Spring/Fall

#### Final Exam Prep 😤
- [ ] YY Spring/Fall
