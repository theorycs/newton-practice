# This code uses multivariate Newton's method to find a local optimum
# of a function with multiple input variables. It numerically estimates
# the gradient and Hessian using scipy.differentiate, then repeatedly
# updates the input vector using numpy.linalg.solve until the change
# in the input vector is smaller than the specified tolerance.
# The optimize function also limits the number of iterations to prevent
# the algorithm from running indefinitely if it does not converge.
# The function returns both the location of the optimum and the
# corresponding value of the function.


import numpy as np
from scipy.differentiate import derivative, hessian


def gradient(f, x):
    """Calculate the gradient of a multivariate function f at x."""

    x = np.asarray(x, dtype=float)
    g = np.empty(len(x))

    for i in range(len(x)):

        def fi(t):
            y = x.copy()
            y[i] = t
            return f(y)

        result = derivative(fi, x[i])
        g[i] = result.df

    return g


def optimize(x, f, tol=1e-6, max_iter=100):
    """Find a local optimum of a multivariate function using Newton's method."""

    x = np.asarray(x, dtype=float)

    for _ in range(max_iter):

        # Calculate the gradient
        g = gradient(f, x)

        # Calculate the Hessian
        H = hessian(f, x).ddf

        # Solve H p = g
        p = np.linalg.solve(H, g)

        # Newton update
        x_new = x - p

        # Stop when the change in x is sufficiently small
        if np.linalg.norm(x_new - x) < tol:
            return {"x": x_new, "value": f(x_new)}

        x = x_new

    return {"x": x, "value": f(x)}