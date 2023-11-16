import numpy as np
def runge_kutta_system(f, a, b, m, N, alpha):
    h = (b - a)/N
    t = a
    w = [[] for _ in range(m)]
    for j in range(m):
        w[j].append(alpha[j])
    for i in range(N):
        k1 = [0]*m
        k2 = [0]*m
        k3 = [0]*m
        k4 = [0]*m
        args = []
        for j in range(m):
            args.append(w[j][-1])
        for j in range(m):
            k1[j] = h*f[j](t, args)
        args = []
        for j in range(m):
            args.append(w[j][-1] + 0.5*k1[j])
        for j in range(m):
            k2[j] = h*f[j](t + h/2, args)
        args = []
        for j in range(m):
            args.append(w[j][-1] + 0.5*k2[j])
        for j in range(m):
            k3[j] = h*f[j](t + h/2, args)
        args = []
        for j in range(m):
            args.append(w[j][-1] + k3[j])
        for j in range(m):
            k4[j] = h*f[j](t + h, args)
        for j in range(m):
            w[j].append(w[j][-1] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j])/6.)
        t = a + i*h
    return w

print(runge_kutta_system([lambda t, args: -4*args[0] + 3*args[1] + 6, lambda t, args: -2.4*args[0] + 1.6*args[1] + 3.6], 0, 0.5, 2, 5, [0, 0]))
