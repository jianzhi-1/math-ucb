def modified_euler(f, a, b, N, alpha):
    h = (b - a)/N
    t = a
    w = alpha
    res = [(t, w)]
    for i in range(N):
        tnext = a + (i + 1)*h
        val = f(t, w)
        w = w + h/2*(val + f(tnext, w + h*val))
        t = tnext
        res.append((t, w))
    return res

#print(modified_euler(lambda t, y: y - t**2 + 1, 0, 2, 10, 0.5))
print(modified_euler(lambda t, y: y - t**2 + 1, 0, 0.5, 10, 0.5))
