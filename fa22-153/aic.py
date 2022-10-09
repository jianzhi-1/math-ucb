def aic(X, y):
    n, p = X.shape
    betahat = np.linalg.inv(X.T@X)@X.T@y
    return n*np.log(2.*np.pi*np.sum((y - X@betahat)**2)/n) + n + 2.*p
