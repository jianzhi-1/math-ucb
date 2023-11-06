def runge_kutta(f, a, b, N, alpha):
    h = (b - a)/N
    t = a
    w = alpha
    res = [(t, w)]
    for i in range(N):
        K1 = h*f(t, w)
        K2 = h*f(t + h/2, w + K1/2)
        K3 = h*f(t + h/2, w + K2/2)
        K4 = h*f(t + h, w + K3)
        w = w + (K1 + 2*K2 + 2*K3 + K4)/6
        t = a + (i + 1)*h
        res.append((t, w))
    return res

print(runge_kutta(lambda t, y: y - t**2 + 1, 0, 2, 10, 0.5))
