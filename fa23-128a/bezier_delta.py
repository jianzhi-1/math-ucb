def bezier_delta(n, points, ldelta, rdelta):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    alpha = [p[0] for p in ldelta]
    beta = [p[1] for p in ldelta]
    alphap = [p[0] for p in rdelta]
    betap = [p[1] for p in rdelta]
    a = np.zeros((n, 4))
    b = np.zeros((n, 4))
    for i in range(n):
        a[i][0] = x[i]
        b[i][0] = y[i]
        a[i][1] = 3*alpha[i]
        b[i][1] = 3*beta[i]
        a[i][2] = 3*(x[i + 1] - x[i]) - 3*(alphap[i + 1] + 2*alpha[i])
        b[i][2] = 3*(y[i + 1] - y[i]) - 3*(betap[i + 1] + 2*beta[i])
        a[i][3] = 2*(x[i] - x[i + 1]) + 3*(alpha[i] + alphap[i + 1])
        b[i][3] = 2*(y[i] - y[i + 1]) + 3*(beta[i] + betap[i + 1])
    return a, b

assert bezier(1, [(1, 1), (6, 2)], [(1.25, 1.5), (None, None)], [(None, None), (5, 3)]) == bezier_delta(1, [(1, 1), (6, 2)], [(0.25, 0.5), (None, None)], [(None, None), (1, -1)])
