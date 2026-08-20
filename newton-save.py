def optimize(x, f, tol=1e-6, max_iter=100):
    h = 1e-5

    def d(f, x):
        return (f(x + h) - f(x)) / h

    for _ in range(max_iter):
        d1 = d(f, x)
        d2 = d(lambda x: d(f, x), x)

        x_new = x - d1 /d2
 
        if abs(x_new - x) < tol:
            return x_new

    x = x_new

    return x