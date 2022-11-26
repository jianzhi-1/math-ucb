def make_X(n, m):
    X = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            if j == 0: X[i][j] = 1.
            else: X[i][j] = max(0., float(i) - (float(j) - 1.))
    return X

def log_likelihood(tau, sigma, Y, C=1e6):
    n = len(Y)
    X = make_X(n, n)
    diag = tau*tau*np.ones(n)
    diag[0] = diag[1] = C
    Q0 = np.diag(diag)
    Sig = X@Q0@X.T + (sigma**2)*np.identity(n)
    return -n*np.log(np.sqrt(2.*np.pi)) - 0.5*np.linalg.slogdet(Sig)[1] - (0.5)*Y.T@np.linalg.inv(Sig)@Y

def log_posterior(tau, sigma, Y):
    return log_likelihood(tau, sigma, Y) - np.log(tau) - np.log(sigma)

def spline(Y, taurange, sigmarange, C=1e6):
    besttau, bestsigma = None, None
    bestres = None
    for tau in taurange:
        for sigma in sigmarange:
            cur = log_posterior(tau, sigma, Y)
            if bestres is None or cur > bestres:
                bestres = cur
                besttau, bestsigma = tau, sigma
    
    n = len(Y)
    X = make_X(n, n)
    diag = besttau*besttau*np.ones(n)
    diag[0] = diag[1] = C
    Q0 = np.diag(diag)
    beta = (1./(bestsigma**2))*np.linalg.inv(np.linalg.inv(Q0) + (1./(bestsigma**2))*X.T@X)@X.T@Y
    
    return beta, besttau, bestsigma

beta, besttau, bestsigma = spline(train_data, np.arange(0.001, 0.1, 0.002), np.arange(5., 10., 0.1))
plt.plot(np.arange(n), make_X(n, n_train)@beta, label='smooth')
