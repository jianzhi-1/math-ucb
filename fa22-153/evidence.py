def evidence(X, y):
    n = len(X)
    betahat = np.linalg.inv(X.T@X)@X.T@y
    p = len(betahat)
    return gamma(p/2)*gamma((n-p-1)/2)/((np.linalg.norm(X@betahat))**p)/((np.linalg.norm(y - X@betahat))**(n-p))
