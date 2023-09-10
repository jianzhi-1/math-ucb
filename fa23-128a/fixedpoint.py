def fixed_point(f, x0, params={"tol": 1e-2, "maxit": 10}):
  tol = params["tol"]
  maxit = params["maxit"]
  x = x0
  for _ in range(maxit):
    fx = f(x)
    if abs(fx - x) <= tol: return fx
    x = fx
  raise Exception("convergence failed")
