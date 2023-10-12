def romberg(f, a, b, n):
    h = b - a
    R11 = h/2*(f(a) + f(b))
    R = [R11]
    print("R1 = ", R)
    for i in range(2, n + 1):
        tempR, res = [], 0
        for k in range(1, 2**(i - 2) + 1):
            res += f(a + (k - 0.5)*h)
        R21 = 1/2*(R[0] + h*res)
        tempR.append(R21)
        for j in range(2, i + 1):
            R2j = tempR[-1] + (tempR[-1] - R[j - 2])/(4**(j - 1) - 1)
            tempR.append(R2j)
        print("R{} = ".format(i), tempR)
        R, h = tempR, h/2
    return R[-1]

romberg(lambda x: x*np.log(x + 1), -0.75, 0.75, 3)
