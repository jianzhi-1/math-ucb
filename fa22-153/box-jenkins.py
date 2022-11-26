# STEP 1: Preprocess Data
### Differencing
def difference(y, ls=None):
    diff_list = ls
    if ls is None: diff_list = [1]
    res = y
    for d in diff_list: res = res[d:] - res[:len(res) - d]
    return res

### Check ACF and PACF are mostly regular and can be fit with a (seasonal) ARMA model
def plot_acf_pacf(y, lags=None):
    n = len(y)
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))
    pacf = sm.tsa.pacf(y, nlags=lags)
    acf = sm.tsa.acf(y, nlags=lags)
    axs[0].stem(acf)
    axs[0].set_title('ACF')
    axs[0].set_xlabel('Lag')
    axs[0].set_ylabel('ACF Coefficient')
    axs[0].axhline(y=0.0, color='black', linestyle='-')
    axs[0].axhline(y=1.96*(n**-0.5), color='red', linestyle='--')
    axs[0].axhline(y=-1.96*(n**-0.5), color='red', linestyle='--')
    axs[1].stem(pacf)
    axs[1].set_title('PACF')
    axs[1].set_xlabel('Lag')
    axs[1].set_ylabel('PACF Coefficient')
    axs[1].axhline(y=0.0, color='black', linestyle='-')
    axs[1].axhline(y=1.96*(n**-0.5), color='red', linestyle='--')
    axs[1].axhline(y=-1.96*(n**-0.5), color='red', linestyle='--')
    plt.show()

# STEP 2: Fit ARMA(p, q)
def get_best_arima(Y, pmax=6, qmax=6):
    prange = range(0, pmax+1)
    qrange = range(0, qmax+1)
    bestp_aic, bestq_aic = None, None
    bestp_bic, bestq_bic = None, None
    best_aic, best_bic = None, None
    for p in prange:
        for q in qrange:
            mod = sm.tsa.SARIMAX(Y, order=(p, 0, q), seasonal_order=(1, 0, 0, 12))
            res = mod.fit()
            print("AIC", res.aic)
            print("BIC", res.bic)
            if best_aic is None or res.aic < best_aic:
                best_aic = res.aic
                bestp_aic, bestq_aic = p, q
            if best_bic is None or res.bic < best_bic:
                best_bic = res.bic
                bestp_bic, bestq_bic = p, q
    return (bestp_aic, bestq_aic), (bestp_bic, bestq_bic)

def predict(Y, l, p, q):
    mod = sm.tsa.SARIMAX(Y, order=(p, 0, q), seasonal_order=(1, 0, 0, 12))
    res = mod.fit()
    pred = np.array(res.predict(len(Y), len(Y) + l - 1))
    return pred

aic_best, bic_best = get_best_arima(d_residue)
pred = predict(residue, n_test, bic_best[0], bic_best[1])
