def log_likelihood(tau, sigma, Y, C=1e6):
    n = len(Y)
    X = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if j == 0: X[i][j] = 1.
            else: X[i][j] = max(0., float(i) - (float(j) - 1.))
    diag = tau*tau*np.ones(n)
    diag[0] = diag[1] = C
    Q0 = np.diag(diag)
    Sig = X@Q0@X.T + (sigma**2)*np.identity(n)
    return -n*np.log(np.sqrt(2.*np.pi)) - 0.5*np.linalg.slogdet(Sig)[1] - (0.5)*Y.T@np.linalg.inv(Sig)@Y

def log_posterior(tau, sigma, Y):
    return log_likelihood(tau, sigma, Y) - np.log(tau) - np.log(sigma)

besttau, bestsigma = None, None
bestres = None
taurange = np.arange(0.001, 0.1, 0.002)
sigmarange = np.arange(5., 16., 0.5)
for tau in taurange:
    for sigma in sigmarange:
        cur = log_posterior(tau, sigma, y)
        if bestres is None or cur > bestres:
            bestres = cur
            besttau, bestsigma = tau, sigma

n = len(y)
X = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if j == 0: X[i][j] = 1.
        else: X[i][j] = max(0., float(i) - (float(j) - 1.))
diag = besttau*besttau*np.ones(n)
diag[0] = diag[1] = 1e6
Q0 = np.diag(diag)
beta = (1./(bestsigma**2))*np.linalg.inv(np.linalg.inv(Q0) + (1./(bestsigma**2))*X.T@X)@X.T@y
