from pulp import *

# Define the parameters
P = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Long-term profit for each program
C = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]  # Investment required for each program
Q = 1000  # Total available investment
total_cost = 0
# Create the LP problem
prob = LpProblem("Investment_Decisions", LpMaximize)

# Create the decision variables
x = LpVariable.dicts("x", range(1, 11), cat='Binary')  # x1 to x10

# Set the objective function
prob += lpSum(P[j - 1] * x[j] for j in range(1, 11))

# Add the constraints
prob += lpSum(C[j - 1] * x[j] for j in range(1, 11)) <= Q  # Total investment constraint
prob += x[3] + x[4] <= 1  # Mutual exclusivity of programs 3 and 4
prob += x[5] + x[6] <= 1  # Mutual exclusivity of programs 5 and 6
prob += x[5] + x[6] <= x[3] + x[4]  # Dependency between programs 5 or 6 and 3 or 4
prob += 2 <= lpSum(x[j] for j in [1, 2, 7, 8, 9, 10]) <= 4  # Minimum and maximum program selection

# Solve the problem
prob.solve()

# Print the optimal solution and the selected programs
print("Optimal Solution:")
print("Objective Value (Overall long-term profit):", value(prob.objective))
print("Selected Programs:")
for j in range(1, 11):
    if value(x[j]) == 1:
        print("Program", j)

print("Selected Programs and Total Cost:")
for j in range(1, 11):
    if value(x[j]) == 1:
        print("Program", j, "- Total Cost:", C[j - 1])
        total_cost += C[j - 1]
        
print("Total Cost of Selected Programs:", total_cost)