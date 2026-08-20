# This code uses Newton's method to find a local optimum of a function.
# It numerically estimates the first and second derivatives, then repeatedly
# updates x until the change in x is smaller than the specified tolerance.
# The optimize function returns both the location of the optimum and the
# corresponding value of the function.


def deriv(f, x, eps=1e-5):
    """Estimate the first derivative of f at x using a finite difference."""
    return (f(x + eps) - f(x)) / eps


def deriv2(f, x, eps=1e-5):
    """Estimate the second derivative of f at x using a finite difference."""
    return (f(x + eps) - 2 * f(x) + f(x - eps)) / eps**2


def optimize(x, f, tol=1e-6):
    """Find a local optimum of f using Newton's optimization method."""

    x_new = x - deriv(f, x) / deriv2(f, x)

    # We keep iterating while the change in x is greater than or equal to
    # the tolerance. In other words, we continue while we have NOT converged.
    while abs(x_new - x) >= tol:
        x = x_new
        x_new = x - deriv(f, x) / deriv2(f, x)

    return {"x": x_new, "value": f(x_new)}