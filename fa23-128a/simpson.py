def f(x): return 1./np.sqrt(np.pi*2)*np.exp(-0.5*x*x)

def simpson(f, n, a, b, eps=1e-6):
    assert n % 2 == 0
    h = (b - a)/n
    arr = np.arange(a, b + eps, h)
    res = 0
    for i in range(len(arr)):
        if i != 0 and i != len(arr) - 1: 
            if i % 2 == 0: res += 2.*f(arr[i])
            else: res += 4.*f(arr[i])
        else: res += f(arr[i])
    return res*(h/3)

simpson(f, 14, -1, 1)
simpson(f, 30, -2, 2)
simpson(f, 48, -3, 3)
