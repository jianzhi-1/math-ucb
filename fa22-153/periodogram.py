# gives the nth sinusoidal vector
def u(x):
    uu = np.arange(n) * 2. * np.pi * 1j * x / n
    return np.exp(uu)

# returns the periodogram given timeseries y
def periodogram(y):
    pg = []
    for i in range(n//2):
        bj = np.abs(np.dot(y, u(i)))**2/n  # bj = I(j/n) = |<y, u(i)>|^2/n
        pg.append(bj)
    return pg

pg = periodogram(y)
plt.plot(np.arange(len(pg))/n, pg)
plt.xlabel('Fourier frequency') 
plt.ylabel('Periodogram')
plt.title('Periodogram')
plt.show()
best_fourier_frequency = np.argmax(pg)/n
print("Fourier frequency = {}".format(best_fourier_frequency))
print("Period = {}".format(1./best_fourier_frequency))
