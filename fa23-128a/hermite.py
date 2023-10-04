import numpy as np
def f(x, fx, fpx):
    n = len(x) - 1
    Q = dict()
    z = dict()
    for i in range(n + 1):
        z[2*i] = x[i]
        z[2*i + 1] = x[i]
        Q[(2*i, 0)] = fx[i]
        Q[(2*i + 1, 0)] = fx[i]
        Q[(2*i + 1, 1)] = fpx[i]
    
        if i != 0:
            Q[(2*i, 1)] = (Q[2*i, 0] - Q[2*i - 1, 0])/(z[2*i] - z[2*i - 1])
    for i in range(2, 2*n + 2):
        for j in range(2, i + 1):
            Q[(i, j)] = (Q[(i, j - 1)] - Q[(i - 1, j - 1)])/(z[i] - z[i - j])
    return Q, z

def query(Q, x, z):
    i = 0
    ans = 0
    while (i, 0) in Q:
        curans = Q[(i, i)]
        for j in range(i):
            curans *= (x - z[j])
        ans += curans
        i += 1
    return ans

def print_Q(Q):
    i = 0
    while (i, 0) in Q:
        for j in range(i + 1):
            print(round(Q[(i, j)], 4), end=" ")
        print()
        i += 1
    

Q, z = f([1.3, 1.6, 1.9], [0.6200860, 0.4554022, 0.2818186], [-0.5220232, -0.5698959, -0.5811571])

# Textbook example
# print_Q(Q)
# print(query(Q, 1.5, z))

""" 3.4 Q6a
x = np.array([1., 1.05])
fx = 3*x*np.exp(x) - np.exp(2*x)
fpx = 3*x*np.exp(x) + 3*np.exp(x) - 2*np.exp(2*x)

Q, z = f(x, fx, fpx)
print_Q(Q)
print(query(Q, 1.03, z))
print((3*1.03*np.exp(1.03) - np.exp(2*1.03)))
print(query(Q, 1.03, z) - (3*1.03*np.exp(1.03) - np.exp(2*1.03)))
"""

""" 3.4 Q6b
x = np.array([1., 1.05, 1.07])
fx = 3*x*np.exp(x) - np.exp(2*x)
fpx = 3*x*np.exp(x) + 3*np.exp(x) - 2*np.exp(2*x)

Q, z = f(x, fx, fpx)
print_Q(Q)
print(query(Q, 1.03, z))
print(query(Q, 1.03, z) - (3*1.03*np.exp(1.03) - np.exp(2*1.03)))
"""



