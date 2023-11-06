def runge_kutta_fehlberg(f, a, b, alpha, tol, hmax, hmin):
    t = a
    w = alpha
    h = hmax
    flag = 1

    res = [(t, w)]

    while flag == 1:
        K1 = h*f(t, w)
        K2 = h*f(t + 1./4.*h, w + 1./4.*K1)
        K3 = h*f(t + 3./8.*h, w + 3./32.*K1 + 9./32.*K2)
        K4 = h*f(t + 12./13.*h, w + 1932./2197.*K1 - 7200./2197.*K2 + 7296./2197.*K3)
        K5 = h*f(t + h, w + 439./216.*K1 - 8.*K2 + 3680./513.*K3 - 845./4104.*K4)
        K6 = h*f(t + 1./2.*h, w - 8./27.*K1 + 2.*K2 - 3544./2565.*K3 + 1859./4104.*K4 - 11./40.*K5)
        R = 1./h*abs(1./360.*K1 - 128./4275.*K3 - 2197./75240.*K4 + 1./50.*K5 + 2./55.*K6)
        if R <= tol:
            t = t + h
            w = w + 25./216.*K1 + 1408./2565.*K3 + 2197./4104.*K4 - 1./5.*K5
            res.append((t, w))
        delta = 0.84*(tol/R)**0.25
        if delta <= 0.1:
            h = 0.1*h
        elif delta >= 4:
            h = 4*h
        else:
            h = delta*h
        h = min(h, hmax)
        if t >= b:
            flag = 0
        elif t + h > b:
            h = b - t
        elif h < hmin:
            flag = 0
            assert False, "minimum h exceeded"
    return res

print(runge_kutta_fehlberg(lambda t, y: y - t**2 + 1, 0, 2, 0.5, 1e-5, 0.25, 0.01))
