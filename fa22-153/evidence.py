def evidence(X, y):
    n, p = X.shape
    betahat = np.linalg.inv(X.T@X)@X.T@y
    return gamma(p/2)*gamma((n-p-1)/2)/((np.linalg.norm(X@betahat))**p)/((np.linalg.norm(y - X@betahat))**(n-p))

def log_evidence(X, y):
    n, p = X.shape
    betahat = np.linalg.inv(X.T@X)@X.T@y
    return np.log(gamma(p/2)) + np.log(gamma((n-p-1)/2)) - p*np.log(np.linalg.norm(X@betahat)) - (n - p)*np.log(np.linalg.norm(y - X@betahat))
