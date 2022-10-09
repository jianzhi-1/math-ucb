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
