fig, axs = plt.subplots(4, 2, figsize=(15, 15))
for k in range(1, 9):
    Xk = polynomial_features(X, k)
    axs[(k - 1)//2, (k - 1)%2].scatter(np.arange(n), y, s=0.5, c='orange')
    axs[(k - 1)//2, (k - 1)%2].plot(np.arange(n), Xk@betastar(Xk, y))
    axs[(k - 1)//2, (k - 1)%2].set_title('Model {}'.format(k))
    axs[(k - 1)//2, (k - 1)%2].set_xlabel('Month since 2004 Jan')
    axs[(k - 1)//2, (k - 1)%2].set_ylabel('Interest in "yahoo"')
