from pulp import *

# Create a maximization problem instance
prob = LpProblem("Primal Problem", LpMaximize)

# Define the variables
x1 = LpVariable("x1", lowBound=-2, upBound=10)
x2 = LpVariable("x2", lowBound=5, upBound=25)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
x5 = LpVariable("x5")

# Set the objective function
prob += 3*x1 - 2*x2 - 5*x3 + 7*x4 + 8*x5

# Add the constraints
prob += x2 - x3 + 3*x4 - 4*x5 == -6
prob += 2*x1 + 3*x2 - 3*x3 - x4 >= 2
prob += x1 + 2*x3 - 2*x4 <= -5

# Solve the problem
prob.solve()

# Print the status of the solution
print("Status:", LpStatus[prob.status])

# Print the optimal solution
print("Optimal Solution:")
for variable in prob.variables():
    print(f"{variable.name}: {variable.varValue}")

# Print the optimal objective value
print("Optimal Objective Value:")
print(value(prob.objective))
