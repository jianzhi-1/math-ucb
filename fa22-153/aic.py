def aic(X, y):
    n = len(X)
    betahat = np.linalg.inv(X.T@X)@X.T@y
    p = len(betahat)
    return n*np.log(2.*np.pi*np.sum((y - X@betahat)**2)/n) + n + 2.*p
