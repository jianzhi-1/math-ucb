def backward_euler(f, fy, a, b, N, alpha, M, tol=1e-6):
    h = (b - a)/N
    t = a
    w = alpha
    arr = [(t, w)]

    for i in range(N):
        wi = arr[-1][1] # past value
        w0 = wi # guess previous value
        j = 1
        flag = 0

        while flag == 0:
            w = w0 - (w0 - wi - h*f(t + h, w0))/(1. - h*fy(t + h, w0))
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

res = backward_euler(lambda t, y: -10.*y+10*t+1, lambda t, y: -10, 0, 1, 10, np.exp(1), 10)
