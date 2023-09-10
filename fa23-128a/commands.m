params = struct("tol", 1e-2, "MaxIt", 20);
f = @(x) 2*x*cos(2*x) - (x - 2)^2;
[fun, dfun, x, out] = NewtonMethod(f, df, 3.5, params);
[x, out] = SecantMethod(f, 2.45, 2.55, params);

format longg; % more decimal places
