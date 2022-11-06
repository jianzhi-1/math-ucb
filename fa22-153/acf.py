def acf(y):
    """Returns ACF and significance band of time series."""
    n = len(y)
    ybar = np.sum(y)/n
    sos = np.sum((y - ybar)**2)
    acfls = np.zeros(n)
    for i in range(n):
        yfront = y[:n-i].copy()
        yback = y[i:].copy()
        yfront -= ybar
        yback -= ybar
        acfls[i] = np.sum(yfront*yback)/sos
    sig_band = 1.96*(n**(-0.5))
    return acfls, sig_band

### Plotting
acf_ls, sig_band = acf(y)
plt.figure(figsize=(15,10))
plt.stem(acf_ls[:100])
plt.axhline(sig_band, color="red", linestyle='--')
plt.axhline(-sig_band, color='red', linestyle='--')
plt.xlabel('lag') 
plt.ylabel('ACF')
plt.title('ACF Plot')
plt.show()

### Inbuilt Autocorrelation
autocorrelation = sm.tsa.acf(y)
plt.plot(np.arange(len(autocorrelation)), autocorrelation)
plt.axhline(y=0.0, color='black', linestyle='-')
plt.axhline(y=1.96*n**-0.5, color='red', linestyle='--')
plt.axhline(y=-1.96*n**-0.5, color='red', linestyle='--')
plt.xlabel('Lag') 
plt.ylabel('Autocorrelation coefficient')
plt.title('Autocorrelation Plot')
plt.show()
