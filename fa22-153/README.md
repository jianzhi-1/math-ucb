# STAT 153
### Introduction to Time Series
UC Berkeley Fall 2022, taught by Professor Aditya

- [x] Week 0: Frequentist Linear Model, Linear Regression
- [x] Week 1: Bayesian Linear Trend Model, Bayesian Constant Function
- [x] Week 2: Bayesian Linear Seasonality Model
- [x] Week 3: Periodogram, Spectral Analysis
- [x] Week 4: Bayesian Model Selection, Evidence, Approximation to Evidence
- [x] Week 5: Akaike Information Criterion (AIC), Bayesian Information Criterion (BIC), Cross-Validation, Zellner Prior
- [ ] Week 6:
- [ ] Week 7:
- [ ] Week 8:
- [ ] Week 9:
- [ ] Week 10:
- [ ] Week 11:
- [ ] Week 12:
- [ ] Week 13:
- [ ] Week 14:

### Implementation
##### Headers
```python
%matplotlib inline
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import genfromtxt
import cvxpy as cp # convex optimization
from scipy.optimize import linprog # matrix inverse
from scipy.special import gamma, loggamma # model selection
from scipy import stats # t-distribution
import statsmodels.api as sm # autocorrelation
from statsmodels.graphics import tsaplots # autocorrelation
```

##### Plotting
```python
plt.figure(figsize=(15,10))
plt.plot(np.arange(n), y)
plt.xlabel('Months since 2004') 
plt.ylabel('Interest in "Playoffs" (United States)')
plt.title('Interest in "Playoffs" (United States) since 2004')
plt.show()
```

##### t-distributions

Remember that scale is the standard deviation. Need to take square root.

##### Discrete Fourier Transform
```python
# insert code here
```

##### R to CSV
```R
write.csv(df,"Desktop/STAT153/df.csv")
```
