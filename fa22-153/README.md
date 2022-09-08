# STAT 153
### Introduction to Time Series
UC Berkeley Fall 2022, taught by Professor Aditya

- [x] Week 0: Frequentist Linear Model (lec1)
- [x] Week 1: Bayesian Linear Trend Model, Bayesian Constant Function (lab1)
- [ ] Week 2: Bayesian Linear Seasonality Model (lec4)
- [ ] Week 3: 
- [ ] Week 4: 
- [ ] Week 5: 

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
from scipy import stats # t-distribution
import statsmodels.api as sm # autocorrelation
from statsmodels.graphics import tsaplots # autocorrelation
```

##### t-distributions

Remember that scale is the standard deviation. Need to take square root.
