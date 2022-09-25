# feature map, can include more linear features
def X(omega):
	return np.column_stack([np.ones(n), np.cos(omega*np.arange(n)), np.sin(omega*np.arange(n))])

# returns the pdf
def f(omega):
	Xw = X(omega)
	betahat = np.linalg.inv(Xw.T@Xw)@Xw.T@y
	return (p - n)*np.log(np.linalg.norm(y - Xw@betahat, 2)) - 0.5*np.log(np.linalg.det(Xw.T@Xw))

# returns OLS solution
def beta(x):
	return np.linalg.inv(x.T@x)@x.T@y

def frequency_estimate():
    omegarange = np.arange(0.01, 1.0, 0.00001)
    flist = []
    for omega in omegarange:
        flist.append(f(omega))
    flist = np.array(flist)
    flist -= np.max(flist)
    flist = np.exp(flist)
    flist = flist/np.sum(flist)

    idx = np.argmax(flist)
    omegastar = 0.01+idx*0.00001
    omegastar
    total = flist[idx]
    upper_confidence, lower_confidence = None, None
	
    # Uncertainty quantification
    for i in range(idx, 0, -1):
        if total > 0.475:
            lower_confidence = 0.01 + i*0.00001
            break
        total += flist[i]
    total = flist[idx]
    for i in range(idx, len(flist)):
        if total > 0.475:
            upper_confidence = 0.01 + i*0.00001
            break
        total += flist[i]
    plt.plot(omegarange, flist)
    plt.xlabel('omega') 
    plt.ylabel('f omega')
    plt.title('PDF plot of omega')
    plt.show()
    print("lower confidence interval = {}".format(lower_confidence))
    print("upper confidence interval = {}".format(upper_confidence))
	return omegastar, lower_confidence, upper_confidence
  
