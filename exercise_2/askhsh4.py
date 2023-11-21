import numpy as np
from scipy.optimize import linprog

# Define the objective function coefficients
c = np.array([-1, -2, -1, 3, -1, -1, 1])

# Define the constraint coefficients matrix
A = np.array([
    [1, 1, 0, -1, 0, 2, -2],
    [0, 1, 0, -1, 1, -2, 2],
    [0, 1, 1, 0, 0, 1, -1],
    [0, 1, 0, -1, 0, -1, 1],
])

# Define the right-hand side of constraints
b = np.array([6, 4, 2, 1])

# Define the bounds for variables
bounds = [(0, None), (0, None),(0, None), (0, None), (0, None), (0, None), (0, None)]

# Solve the linear programming problem using the simplex method
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

# Check if the primal problem is successfully solved
if result.success:
    print("Primal problem solved successfully!")
    print("Objective function value:", -result.fun)

    # Print the primal solution
    print("Primal solution:")
    for i, variable in enumerate(result.x):
        print("x", i+1, "=", variable)
else:
    print("Primal problem could not be solved. Status:", result.message)
