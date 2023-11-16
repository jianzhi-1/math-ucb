import numpy as np

# for solving stiff ODEs

def trapezoid_newton(f, fy, a, b, N, alpha, M, tol=1e-6):
    h = (b - a)/N
    t = a
    w = alpha
    arr = [(t, w)]

    for i in range(N):
        k1 = w + h/2*f(t, w)
        w0 = k1
        j = 1
        flag = 0

        while flag == 0:
            w = w0 - (w0 - h/2.*f(t + h, w0) - k1)/(1. - h/2.*fy(t + h, w0))
            if abs(w - w0) < tol:
                flag = 1
            else:
                j = j + 1
                w0 = w
                if j > M:
                    raise Exception("max iterations exceeded")
        t = a + (i + 1)*h
        arr.append((t, w))
    return arr

print(trapezoid_newton(lambda t, y: 5*np.exp(5*t)*(y - t)**2 + 1, lambda t, y: 10*np.exp(5*t)*(y - t), 0, 1, 5, -1, 10))
