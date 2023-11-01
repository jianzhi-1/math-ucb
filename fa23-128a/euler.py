def euler(f, a, b, N, alpha):
    h = (b - a)/N
    t = [a]
    w = [alpha]
    for i in range(1, N + 1):
        w.append(w[-1] + h*f(t[-1], w[-1]))
        t.append(a + i*h)
    return t, w
