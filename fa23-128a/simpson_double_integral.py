def simpson_double_integral(f, a, b, c, d, m, n):
    assert m % 2 == 0
    assert n % 2 == 0
  
    h = (b - a)/n
    j1 = 0
    j2 = 0
    j3 = 0

    for i in range(n + 1):
        # compute integral_{c(x_i)}^{d(x_i)} f(xi, y) dy
        # fix xi = a + i*h

        x = a + i*h
        hx = (d(x) - c(x))/m
        k1 = f(x, c(x)) + f(x, d(x))
        k2 = 0
        k3 = 0

        for j in range(1, m):
            y = c(x) + j*hx
            Q = f(x, y)
            if j % 2 == 0: k2 = k2 + Q
            else: k3 = k3 + Q

        L = (k1 + 2*k2 + 4*k3)*hx/3 # integral_{c(x_i)}^{d(x_i)} f(xi, y) dy

        if i == 0 or i == n:
            j1 += L
        elif i % 2 == 0:
            j2 += L
        else:
            j3 += L
    
    J = h*(j1 + 2*j2 + 4*j3)/3 # final integral

    return J

### Textbook example
# print(simpson_double_integral(lambda x, y: np.exp(y/x), 0.1, 0.5, lambda x: x**3, lambda x: x**2, 10, 10))
