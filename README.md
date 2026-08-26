# Newton's Method

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

A practice implementation of **Newton's method** for studying local convergence and numerical optimization in both univariate and multivariate cases.

The project explores how the familiar one-dimensional formulation of Newton's method generalizes to multiple dimensions through the **Jacobian matrix, gradient vector, and Hessian matrix**.

## Overview

Newton's method is an iterative numerical method that can be used for both **root finding** and **optimization**. This project implements the method in two settings:

- **Univariate:** functions of a single variable
- **Multivariate:** functions of multiple variables

The univariate case uses the first and second derivatives, while the multivariate case extends these ideas using the Jacobian, gradient, and Hessian.

## Univariate Newton's Method

### Root Finding
For a scalar function \(f(x)\), Newton's method finds a root by iteratively applying:

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.
\]

The method uses the first derivative to approximate the function locally by its tangent line and iteratively improve the estimate of the root.

### Optimization
Newton's method can also be applied to finding extrema of a scalar function. Since an extremum occurs where \(f'(x) = 0\), Newton's method can be applied to \(f'(x)\), giving the iteration:

\[
x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}.
\]

Here, the second derivative provides the curvature information used to update the current estimate.

## Multivariate Newton's Method

### Root Finding
For a system of nonlinear equations represented by a vector-valued function \(F(x) = 0\), the scalar derivative is replaced by the **Jacobian matrix** \(J_F(x)\). The Newton iteration becomes:

\[
x_{n+1} = x_n - J_F(x_n)^{-1}F(x_n).
\]

In practice, the corresponding linear system is solved directly rather than explicitly computing the matrix inverse.

### Optimization
For a scalar function of several variables \(f(x)\), an extremum occurs where the **gradient** vanishes: \(\nabla f(x) = 0\). Applying Newton's method to this system gives:

\[
x_{n+1} = x_n - H_f(x_n)^{-1}\nabla f(x_n),
\]

where \(H_f(x)\) is the **Hessian matrix** of second derivatives. The gradient generalizes the first derivative, while the Hessian generalizes the second derivative and describes the local curvature of the function.

## What This Project Covers

- Newton's method for root finding in one dimension
- Newton's method for optimization in one dimension
- Multivariate Newton's method for solving nonlinear systems
- Multivariate Newton optimization
- Derivative-based iterative updates
- Jacobian matrices for nonlinear systems
- Gradient vectors for multivariate optimization
- Hessian matrices for second-order optimization
- Local convergence behavior
- Numerical stopping and convergence criteria
- Examples for experimentation and verification

## Local Convergence

Newton's method is primarily a **locally convergent** method. When the initial guess is sufficiently close to the desired solution and the relevant derivatives satisfy appropriate conditions, Newton's method can exhibit **quadratic convergence**.

However, convergence is not guaranteed for an arbitrary initial guess. Depending on the function and starting point, the iteration may converge to a different solution, fail to converge, or encounter numerical difficulties.

## Numerical Considerations

Although the mathematical formulation of Newton's method involves an inverse derivative, Jacobian, or Hessian, numerical implementations generally avoid explicitly computing matrix inverses. Instead, the Newton step is obtained by solving the corresponding linear system.

Important practical considerations include:

- Choice of initial guess
- Size of the Newton step
- Residual or gradient magnitude
- Singular or poorly conditioned Jacobians and Hessians
- Failure to converge
- Convergence to an unintended solution
- Numerical precision

## Project Structure

The repository is organized as follows:

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── newton.py               # Main implementation
├── newton2.py              # Alternative implementation
├── multivariate.py         # Multivariate Newton methods
├── test_newton.py          # Unit tests
├── test_newton-2.py        # Additional tests
├── newton-save.py          # Saved/backup version
└── .ipynb_checkpoints/     # Jupyter notebook checkpoints (if any)
    └── ...
```

## Usage

### Clone the repository

```bash
git clone https://github.com/theorycs/newton-practice.git
cd newton-practice
```

### Run the examples

The core implementations are in the Python files. You can run the main scripts directly. For example, to execute the univariate implementation:

```bash
python newton.py
```

To run the multivariate examples:

```bash
python multivariate.py
```

### Run tests

To verify the implementations, run the test scripts:

```bash
python test_newton.py
python test_newton-2.py
```

## Dependencies

This project is written in Python and relies on standard libraries. If you need to install any dependencies, you can typically use:

```bash
pip install numpy matplotlib scipy  # if needed
```

(Check the individual script files for specific import statements.)

## Purpose

This repository is primarily a **practice and learning implementation** rather than a production numerical-analysis library. The goal is to connect the mathematical formulation of Newton's method with an actual implementation and to explore how the concepts of derivatives, Jacobians, gradients, and Hessians extend from one dimension to multiple dimensions.

## References

The implementation is based on standard numerical analysis and optimization concepts, including Newton's method, local convergence, nonlinear systems, and second-order optimization.

## License

This project is dedicated to the public domain under the [CC0 1.0 Universal License](LICENSE). You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.
