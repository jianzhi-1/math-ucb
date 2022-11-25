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
