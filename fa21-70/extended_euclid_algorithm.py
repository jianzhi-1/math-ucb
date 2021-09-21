def gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        d, x, y = gcd(b % a, a)
        return d, y - (b // a) * x, x

d, x, y = gcd(30, 50)
