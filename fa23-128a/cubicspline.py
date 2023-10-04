import numpy as np
from scipy.interpolate import CubicSpline
x, y = np.array([0, 1, 2]), np.array([0, 1, 2])
spl = CubicSpline(x, y)
