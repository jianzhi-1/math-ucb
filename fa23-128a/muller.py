def muller(f, p0, p1, p2, tol=1e-6, maxit=40):

    ### initialisation
    h1 = p1 - p0
    h2 = p2 - p1
    delta1 = (f(p1) - f(p0))/h1
    delta2 = (f(p2) - f(p1))/h2
    d = (delta2 - delta1)/(h1 + h2)
    i = 3

    while i <= maxit:

        b = delta2 + h2*d
        D = (b*b - 4*f(p2)*d)**0.5
        E = None
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        h = -2.*f(p2)/E
        p = p2 + h

        if abs(h) < tol:
            return p
        
        ### prepare for next iteration
        p0 = p1
        p1 = p2
        p2 = p
        h1 = p1 - p0
        h2 = p2 - p1
        delta1 = (f(p1) - f(p0))/h1
        delta2 = (f(p2) - f(p1))/h2
        d = (delta2 - delta1)/(h1 + h2)
        i = i + 1

### Use cases
# print(muller(lambda x: x**4 - 2*x**3 - 12*x**2 + 16*x - 40, 0.0, -0.1, -0.2))
# print(muller(lambda x: 16*x**4 + 88*x**3 + 159*x**2 + 76*x - 240, -1.6, -1.55, -1.5))
