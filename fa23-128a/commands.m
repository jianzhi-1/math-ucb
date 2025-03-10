interval = struct("a", 0.1, "b", 1.0)
[x, out] = bisection(f, interval, params)

params = struct("tol", 1e-2, "MaxIt", 20);
f = @(x) 2*x*cos(2*x) - (x - 2)^2;
[fun, dfun, x, out] = NewtonMethod(f, df, 3.5, params);
[x, out] = SecantMethod(f, 2.45, 2.55, params);

format longg; % more decimal places

g = @(x) 1 + sin(x)^2;
intv = [1 2];
x0 = 1;
params = struct("tol", 2e-14, "MaxIt", 30);
[x, out] = SteffensenMethod(g, x0, params)
% out.x stores the Steffensen computes i.e. p0(n)

for i = 1:17;
  x(i) - (x(i + 1) - x(i))^2/(x(i+2) - 2*x(i+1) + x(i));
end
