def adaptive_quadrature(f, aa, bb, tol0, n):

    ### Step 1: initialise
    app = 0
    i = 1
    tol = np.zeros(n + 1)
    a = np.zeros(n + 1)
    h = np.zeros(n + 1)
    fa = np.zeros(n + 1)
    fc = np.zeros(n + 1)
    fb = np.zeros(n + 1)
    s = np.zeros(n + 1)
    l = np.zeros(n + 1)

    tol[i] = 10*tol0
    a[i] = aa
    h[i] = (bb - aa)/2
    fa[i] = f(aa)
    fc[i] = f(aa + h[i])
    fb[i] = f(bb)
    s[i] = h[i]*(fa[i] + 4*fc[i] + fb[i])/3
    l[i] = 1

    ### Step 2: while loop

    while i > 0:

        ### Step 3: approximate both halves by Simpson

        fd = f(a[i] + h[i]/2)
        fe = f(a[i] + 3*h[i]/2)
        s1 = h[i]*(fa[i] + 4*fd + fc[i])/6
        s2 = h[i]*(fc[i] + 4*fe + fb[i])/6
        v1 = a[i]
        v2 = fa[i]
        v3 = fc[i]
        v4 = fb[i]
        v5 = h[i]
        v6 = tol[i]
        v7 = s[i]
        v8 = l[i]

        i = i - 1
      
        if abs(s1 + s2 - v7) < v6:
            app = app + (s1 + s2)
        else:
            if v8 >= n:
                raise Exception("Level exceeded")
            else:

                i = i + 1 # add one level for right half interval

                ### data for right half interval
                a[i] = v1 + v5
                fa[i] = v3
                fc[i] = fe
                fb[i] = v4
                h[i] = v5/2
                tol[i] = v6/2
                s[i] = s2
                l[i] = v8 + 1

                
                i = i + 1 # add one level for left half interval

                ### data for left half interval
                a[i] = v1
                fa[i] = v2
                fc[i] = fd
                fb[i] = v3
                h[i] = h[i - 1]
                tol[i] = tol[i - 1]
                s[i] = s1
                l[i] = l[i - 1]
    return app

### Textbook example
# print(adaptive_quadrature(lambda x: 100./(x**2)*np.sin(10./x), 1, 3, 1e-6, 100))
