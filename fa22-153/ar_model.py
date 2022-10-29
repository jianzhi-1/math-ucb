def ar_model(p, y):
    """
    p: order of AR model
    y: time series
    """
    
    # constructing the truncated feature matrix
    n = len(y)
    st = [np.ones(n - p)]
    for i in range(p - 1, -1, -1):
        st.append(y[i:n-p+i])
    X = np.vstack(st).T
    Y = y[p:]
    
    # inference
    phihat = np.linalg.inv(X.T@X)@X.T@Y
    sos = np.sum((Y-X@phihat)**2) # sum of squared error
    sigmahat = np.sqrt(sos/(n - 2*p - 1))
    
    # uncertainty quantification
    phi_confidence_interval = []
    sigma_confidence_interval = None
    for i in range(len(phihat)):
        phi_confidence_interval.append(stats.t.interval(0.95, n - 2*p - 1, loc=phihat[i], scale=sigmahat*np.sqrt(np.linalg.inv(X.T@X)[i][i])))
    sigma_higher_confidence = np.sqrt(sos/stats.chi2.interval(0.95, n - 2*p - 1)[0])
    sigma_lower_confidence = np.sqrt(sos/stats.chi2.interval(0.95, n - 2*p - 1)[1])
    sigma_confidence_interval = (sigma_lower_confidence, sigma_higher_confidence)
    
    return phihat, sigmahat, phi_confidence_interval, sigma_confidence_interval
  
def ar_model_prediction(y, phi, n):
    """
    y: time series
    phi: AR coefficients
    n: length to extend y to
    """
  
    while len(y) < n:
        cur = 0
        for i in range(len(phi)):
            if i == 0: cur += phi[i]
            else: cur += phi[i]*y[len(y) - i]
        y.append(cur)
    return y
