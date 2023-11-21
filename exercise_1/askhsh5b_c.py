from pulp import *
import numpy as np
import itertools

# Create the problem variable
prob = LpProblem("LP Problem", LpMinimize)

# Create the decision variables
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
x5 = LpVariable("x5", lowBound=0)
x6 = LpVariable("x6", lowBound=0)

# Set the objective function
prob += 12*x1 - 10*x2 - 30*x3, "Z"

# Add the constraints
prob += -3*x1 + 2*x2 + 8*x3 + x4 == 17
prob += -1*x1 + 1*x2 + 3*x3 + x5 == 9
prob += -2*x1 + 1*x2 + 8*x3 + x6 == 16

# Solve the problem
prob.solve()

# If an optimal solution is found, print the optimal value and decision variables
if LpStatus[prob.status] == "Optimal":
    print("Optimal Value of Z =", value(prob.objective))
    for v in prob.variables():
        print(v.name, "=", v.varValue)



# Define the matrix A and the vector b
A = np.array([[-3, 2, 8, 1, 0, 0],
              [-1, 1, 3, 0, 1, 0],
              [-2, 1, 8, 0, 0, 1]])
b = np.array([17, 9, 16])

# Find all possible sets of basic variables
basic_var_indices = [set(indices) for indices in itertools.combinations(range(A.shape[1]), 3)]

# Find the basic solutions for each set of basic variables
basic_solutions = []
for indices in basic_var_indices:
    A_basic = A[:, list(indices)]
    x_basic = np.linalg.solve(A_basic, b)
    x = np.zeros(A.shape[1])
    x[list(indices)] = x_basic
    basic_solutions.append(x)

# Print the basic solutions
print("\nBasic solutions:\n", x)
for x in basic_solutions:
    print(x)



# Find the degenerate basic solutions
deg_solutions = []
for sol in basic_solutions:
    if 0 in sol:
        deg_solutions.append(sol)

# Print the degenerate basic solutions
if len(deg_solutions) > 0:
    print("\nDegenerate basic solutions:")
    for solution in deg_solutions:
      print(np.around(solution, 2), end="\n")

else:
    print("There are no degenerate basic solutions.")

# Round the basic solutions to 8 decimal places
basic_solutions_rounded = np.around(basic_solutions, 8)

# Define the solutions to match
solutions_to_match = np.array([[6.33333333, 7.33333333, 2.66666667],
                               [1., 10., -0.],
                               [-0., 8.5, -0.],
                               [-0., -0., 2.],
                               [-0., -0., -0.]])

# Match the basic solutions with the solutions to match
for i, solution in enumerate(basic_solutions_rounded):
    for j, solution_to_match in enumerate(solutions_to_match):
        try:
            if np.array_equal(solution[:3], solution_to_match):
                print(f"Basic solution {i+1} matches vertex {j+1}\n")
                print("Basic solution:", solution)
                print("Vertex to match:", solution_to_match,"\n")
                break
        except ValueError:
            continue