import numpy as np

# Runge-Kutta subalgorithm
def rk4(f, h, v0, x0):
    m = dict()
    m[0] = (x0, v0)
    m[1], m[2], m[3] = None, None, None
    for j in [1, 2, 3]:
        K1 = h*f(m[j - 1][0], m[j - 1][1])
        K2 = h*f(m[j - 1][0] + h/2, m[j - 1][1] + K1/2)
        K3 = h*f(m[j - 1][0] + h/2, m[j - 1][1] + K2/2)
        K4 = h*f(m[j - 1][0] + h, m[j - 1][1] + K3)
        m[j] = (m[0][0] + j*h, m[j - 1][1] + (K1 + 2*K2 + 2*K3 + K4)/6.)
    return m[1], m[2], m[3]

def adams_predictor_corrector(f, a, b, alpha, tol, hmax, hmin):
    t0 = a
    w0 = alpha
    h = hmax
    flag = 1
    last = 0

    res = [(t0, w0)]
    accepted = [(t0, w0)]

    (t1, w1), (t2, w2), (t3, w3) = rk4(f, h, w0, t0)
    res.append((t1, w1))
    res.append((t2, w2))
    res.append((t3, w3))
    nflag = 1
    i = 4
    t = t3 + h

    while flag == 1:
        wp = res[-1][1] + h/24.*(55.*f(res[-1][0], res[-1][1]) - 59.*f(res[-2][0], res[-2][1]) + 37.*f(res[-3][0], res[-3][1]) - 9.*f(res[-4][0], res[-4][1]))
        wc = res[-1][1] + h/24.*(9.*f(t, wp) + 19.*f(res[-1][0], res[-1][1]) - 5*f(res[-2][0], res[-2][1]) + f(res[-3][0], res[-3][1]))

        sigma = 19.*abs(wc - wp)/(270.*h)

        if sigma <= tol:
            # step 7 - 16
            res.append((t, wc)) # accepted

            if nflag == 1:
                # accept previous results
                accepted.append((res[-4], h))
                accepted.append((res[-3], h))
                accepted.append((res[-2], h))
                # accept current result
                accepted.append((res[-1], h))
            else:
                # previous result already accepted; accept current result
                accepted.append((res[-1], h))

            if last == 1:
                flag = 0
            else:
                # 10 - 16
                i = i + 1
                nflag = 0

                if sigma <= 0.1*tol or res[-1][0] + h > b:
                    # step 12 - 16
                    q = (tol/(2.*sigma))**0.25
                    if q > 4: h = 4.*h
                    else: h = q*h
                    h = min(hmax, h)
                    if res[-1][0] + 4.*h > b:
                        h = (b - res[-1][0])/4.
                        last = 1
                    (t1, w1), (t2, w2), (t3, w3) = rk4(f, h, res[-1][1], res[-1][0])
                    res.append((t1, w1))
                    res.append((t2, w2))
                    res.append((t3, w3))
                    nflag = 1
                    i = i + 3
                pass

        else:
            # step 17 - 19
            q = (tol/(2*sigma))**0.25
            if q < 0.1: h = 0.1*h
            else: h = q*h
            if h < hmin:
                flag = 0
                assert 0, "hmin exceeded"
            else:
                if nflag == 1:
                    i = i - 3
                    res = res[:-3] # reject previous results
                    (t1, w1), (t2, w2), (t3, w3) = rk4(f, h, res[-1][1], res[-1][0])
                    res.append((t1, w1))
                    res.append((t2, w2))
                    res.append((t3, w3))
                    i = i + 3
                    nflag = 1
        t = res[-1][0] + h
    return accepted

#print(adams_predictor_corrector(lambda t, y: y - t**2 + 1, 0, 2, 0.5, 1e-5, 0.2, 0.01))
print(adams_predictor_corrector(lambda t, y: 1./t*(y**2 + y), 1, 3, -2, 1e-4, 0.4, 0.01))
