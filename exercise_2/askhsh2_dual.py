from pulp import *

# Create a minimization problem instance
prob = LpProblem("Dual Problem", LpMinimize)

# Define the variables
y1 = LpVariable("y1", lowBound=0)
y2 = LpVariable("y2", lowBound=0)
y3 = LpVariable("y3", lowBound=0)
y4 = LpVariable("y4", lowBound=0)
y5 = LpVariable("y5", lowBound=0)
y6 = LpVariable("y6", lowBound=0)
y7 = LpVariable("y7", lowBound=0)
y8 = LpVariable("y8", lowBound=0)

# Set the objective function (negation of the original coefficients)
prob += -6*y1 + 6*y2 - 2*y3 - 5*y4 + 2*y5 + 10*y6 - 5*y7 + 25*y8

# Add the constraints
prob += -2*y3 + y4 - y5 + y6 >= 3
prob += y1 - y2 - 3*y3 - y7 + y8 >= -2
prob += -y1 + y2 + 3*y3 + 2*y4 >= -5
prob += 3*y1 - 3*y2 + y3 - 2*y4 >= 7
prob += -4*y1 + 4*y2 >= 8

# Solve the problem
prob.solve()

# Print the optimal solution
print("Optimal Solution:")
for variable in prob.variables():
    print(f"{variable.name}: {variable.varValue}")

# Print the optimal objective value (negation of the original objective value)
print("Optimal Objective Value:")
print(value(prob.objective))

# Define the key variables
key_variables = [y1, y2, y3, y4, y5, y6, y7, y8]
# Print the basic B matrix
print("Basic B matrix:")
B = []
for constraint in prob.constraints:
    equation = prob.constraints[constraint]
    row = [equation[var].coeff if var in equation else 0 for var in key_variables]
    B.append(row)

for row in B:
    print(row)