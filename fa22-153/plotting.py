plt.figure(figsize=(15,10))
plt.scatter(x, y, label='data')
plt.plot(x, X@betastar, c='orange', label='model')
plt.xlabel('x') 
plt.ylabel('y')
plt.legend()
plt.title('Plot of y against x')
plt.show()