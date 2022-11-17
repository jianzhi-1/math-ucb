mod = ARIMA(y, order=(0, 0, 1))
res = mod.fit()
res.summary()
