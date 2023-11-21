import numpy as np
from scipy.optimize import linprog

# Define the objective function coefficients
c = np.array([3, -2, -5, 7, 8, 0, 0, 0, 0, 0, 0, 0])

# Define the constraint coefficients matrix
A = np.array([
    [0, 1, -1, 3, -4, 0, 0, 0, 0, 0, 0, 1],
    [-2, -3, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 2, -2, 0, 0, 1, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
])
# Define the key variables
key_variables = [1, 3, 4, 7, 8, 9, 10]

# Define the right-hand side of constraints
b = np.array([-6, -2, -5, 2, 10, -5, 25])

# Extract the columns corresponding to the key variables
B = A[:, key_variables]
# Print the basic table
print("Basic Table:")
print(B)

# Compute the complementary matrix
complementary_matrix = np.identity(B.shape[0]) - B

# Print the complementary matrix
print("Complementary Matrix:")
print(complementary_matrix)

# Define the lower bounds for variables
x_bounds = [(0, None)] * len(c)

# Solve the linear programming problem for the primal
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='simplex')

# Check if the primal problem is successfully solved
if result.success:
    print("Optimal solution found!")
    print("Objective function value:", result.fun)
    
    # Print the primal solution
    print("Primal solution:")
    for i, variable in enumerate(result.x):
        print("x", i+1, "=", variable)
else:
    print("Primal problem could not be solved. Status:", result.message)
