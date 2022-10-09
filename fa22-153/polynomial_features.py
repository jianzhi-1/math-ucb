def polynomial_features(X, k):
    # generates polynomial features
    ls = []
    ls.append(np.ones(len(X)))
    for i in range(1, k + 1):
        ls.append(X**i)
    return np.vstack(ls).T
