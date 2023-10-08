import numpy as np

def bezier(n, points, lguide, rguide):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    xp = [p[0] for p in lguide]
    yp = [p[1] for p in lguide]
    xm = [p[0] for p in rguide]
    ym = [p[1] for p in rguide]
    a = np.zeros((n, 4))
    b = np.zeros((n, 4))
    for i in range(n):
        a[i][0] = x[i]
        b[i][0] = y[i]
        a[i][1] = 3*(xp[i] - x[i])
        b[i][1] = 3*(yp[i] - y[i])
        a[i][2] = 3*(x[i] + xm[i + 1] - 2*xp[i])
        b[i][2] = 3*(y[i] + ym[i + 1] - 2*yp[i])
        a[i][3] = x[i + 1] - x[i] + 3*xp[i] - 3*xm[i + 1]
        b[i][3] = y[i + 1] - y[i] + 3*yp[i] - 3*ym[i + 1]
    return a, b


print(bezier(1, [(0, 0), (5, 2)], [(1, 1), (None, None)], [(None, None), (6, 3)]))
