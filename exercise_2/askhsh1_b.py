import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the objective function coefficients
c = np.array([-2, -4, -1, -1])

# Define the constraint coefficients
A = np.array([[1, 3, 0, 1], [2, 1, 0, 0], [0, 1, 4, 1]])
b = np.array([8, 6, 6])

# Define the bounds for variables (x1, x2, x3, x4 >= 0)
bounds = [(0, None)] * 4

# Solve the linear programming problem using the simplex method
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

# Extract the optimal solution and objective value
optimal_solution = result.x
objective_value = result.fun

# Print the optimal solution and objective value
print("Optimal Solution:")
print("x1 =", optimal_solution[0])
print("x2 =", optimal_solution[1])
print("x3 =", optimal_solution[2])
print("x4 =", optimal_solution[3])
print("Objective Value:", -objective_value)  # Negate the objective value to maximize

# Perturbation amount
c_perturb = 0.5

# Perturb x1 coefficient
c_perturbed = np.copy(c)
c_perturbed[0] += c_perturb

# Solve the linear programming problem with the perturbed x1 coefficient
result_perturbed = linprog(c_perturbed, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

# Extract the optimal solution and objective value with the perturbed x1 coefficient
optimal_solution_perturbed = result_perturbed.x
objective_value_perturbed = result_perturbed.fun

# Check if the objective value remains the same
if np.isclose(objective_value_perturbed, objective_value):
    print(f"Tolerance Interval for x1: ({c[0] - c_perturb}, {c[0] + c_perturb})")
else:
    print("Optimal solution does not remain on the same vertex when perturbing x1 coefficient.")

# Perturb x4 coefficient
c_perturbed = np.copy(c)
c_perturbed[3] += c_perturb

# Solve the linear programming problem with the perturbed x4 coefficient
result_perturbed = linprog(c_perturbed, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

# Extract the optimal solution and objective value with the perturbed x4 coefficient
optimal_solution_perturbed = result_perturbed.x
objective_value_perturbed = result_perturbed.fun

# Check if the objective value remains the same
if np.isclose(objective_value_perturbed, objective_value):
    print(f"Tolerance Interval for x4: ({c[3] - c_perturb}, {c[3] + c_perturb})")
else:
    print("Optimal solution does not remain on the same vertex when perturbing x4 coefficient.")
