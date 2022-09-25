# gives the nth sinusoidal vector
def u(x):
    uu = np.arange(n) * 2. * np.pi * 1j * x / n
    return np.exp(uu)

# returns the periodogram given timeseries y
def periodogram(y):
  periodogram = []
  for i in range(n//2):
      bj = np.abs(np.dot(y, u(i)))**2/n  # bj = I(j/n) = |<y, u(i)>|^2/n
      periodogram.append(bj)
  return periodogram

plt.plot(np.arange(len(periodogram))/n, periodogram)
plt.xlabel('Fourier frequency') 
plt.ylabel('Periodogram')
plt.title('Periodogram')
plt.show()
best_fourier_frequency = np.argmax(periodogram)/n
print("Fourier frequency = {}".format(best_fourier_frequency))
print("Period = {}".format(1./best_fourier_frequency))
