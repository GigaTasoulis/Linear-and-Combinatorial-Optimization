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

# Calculate the basis indices
basis_indices = np.where(np.abs(optimal_solution) > 1e-6)[0]

# Calculate the matrix B using the basis indices
B = A[:, basis_indices]
# Calculate the inverse of matrix B
B_inv = np.linalg.inv(B)

print("\nBest Matrix B:")
print(B)

print("\nInverse of Matrix B (B^-1):")
print(B_inv)

basic_variables = np.where(np.isclose(optimal_solution, 0) == False)[0]
nonbasic_variables = np.where(np.isclose(optimal_solution, 0))[0]
variable_names = ['x1', 'x2', 'x3', 'x4']

basic_variable_names = [variable_names[i] for i in basic_variables]
nonbasic_variable_names = [variable_names[i] for i in nonbasic_variables]

print("Basic Variables:", basic_variable_names)
print("Non-Basic Variables:", nonbasic_variable_names)

# Substituting optimal point into the constraints
optimal_point = result.x
rhs = b  # Right-hand side of the inequalities

binding_constraints = []
nonbinding_constraints = []

for i in range(len(A)):
    constraint_value = np.dot(A[i], optimal_point)
    if np.isclose(constraint_value, rhs[i]):
        binding_constraints.append(i + 1)
    else:
        nonbinding_constraints.append(i + 1)

print("Binding Constraints:", binding_constraints)
print("Non-Binding Constraints:", nonbinding_constraints)



# Plot the feasible region
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1, x2 = np.meshgrid(np.linspace(0, 10, 50), np.linspace(0, 10, 50))
x3 = np.minimum(2 - 0.5 * x2, (6 - x2 - x1) / 4) 
x4 = np.minimum(8 - x1 - 3 * x2, 6 - x2 - 4 * x3)

ax.plot_surface(x1, x2, x3, alpha=0.3)
ax.plot_surface(x1, x2, x4, alpha=0.3)
ax.plot([0, 10], [0, 0], [0, 0], 'r-')
ax.plot([0, 10], [0, 0], [0, 10], 'r-')
ax.plot([0, 10], [10, 10], [0, 0], 'r-')
ax.plot([0, 10], [10, 10], [10, 10], 'r-')
ax.plot([0, 10], [0, 0], [10, 10], 'r-')
ax.plot([0, 10], [0, 0], [0, 10], 'r-')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3,x4')

# Plot the optimal vertex
ax.scatter(optimal_solution[0], optimal_solution[1], optimal_solution[2], color='r', label='Optimal Vertex')
ax.legend()

plt.show()


