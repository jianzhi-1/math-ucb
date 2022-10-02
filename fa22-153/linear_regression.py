def linear_regression(X, y):
    assert len(X) == len(y)
    n = len(X) # number of data points
    betahat = np.linalg.inv(X.T@X)@X.T@y
    p = len(betahat) # number of parameters
    sigmahat = np.sqrt((1./(n - 2))*np.linalg.norm(y - X@betahat)**2)
    beta_confidence_interval = []
    sigma_confidence_interval = None
    for i in range(len(betahat)):
        beta_confidence_interval.append(stats.t.interval(0.95, n - 2, loc=betahat[i], scale=sigmahat*np.sqrt(np.linalg.inv(X.T@X)[i][i])))
    
    sbeta = np.linalg.norm(y - X@betahat, 2)**2 # sum of squared error
    sigma_higher_confidence = np.sqrt(sbeta/stats.chi2.interval(0.95, n - p)[0])
    sigma_lower_confidence = np.sqrt(sbeta/stats.chi2.interval(0.95, n - p)[1])
    sigma_confidence_interval = (sigma_lower_confidence, sigma_higher_confidence)
    
    return betahat, sigmahat, beta_confidence_interval, sigma_confidence_interval
