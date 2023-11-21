# Import PuLP modeler functions
from pulp import *

# Create the model
model = LpProblem(name="Employee Scheduling Problem", sense=LpMinimize)

# Define decision variables
shifts = range(1, 6)
hours = range(1, 11)
x = LpVariable.dicts("x", (shifts, hours), lowBound=0, cat='Integer')

# Define objective function
model += 170 * (x[1][1] + x[1][2] + x[1][3] + x[1][4]) \
         + 160 * (x[2][2] + x[2][3] + x[2][4] + x[2][5]) \
         + 175 * (x[3][4] + x[3][5] + x[3][6] + x[3][7]) \
         + 180 * (x[4][6] + x[4][7] + x[4][8] + x[4][9]) \
         + 195 * (x[5][9] + x[5][10]), "Total Cost"

# Define constraints
for h in hours:
    model += lpSum([x[s][h] for s in shifts]) >= 1, f"At least 1 employee must work hour {h}"

# Define constraints
model += x[1][1] >= 48, "Time-Period 1"
model += x[1][2] + x[2][2] >= 79, "Time-Period 2"
model += x[1][3] + x[2][3] >= 65, "Time-Period 3"
model += x[1][4] + x[2][4] + x[3][4] >= 87, "Time-Period 4"
model += x[2][5] + x[3][5] >= 64, "Time-Period 5"
model += x[3][6] + x[4][6] >= 73, "Time-Period 6"
model += x[3][7] + x[4][7] >= 82, "Time-Period 7"
model += x[4][8] + x[5][8] >= 43, "Time-Period 8"
model += x[4][9] + x[5][9] >= 52, "Time-Period 9"
model += x[5][10] >= 15, "Time-Period 10"

# Solve the model
status = model.solve()

# Print the status of the solution
print(f"Status: {LpStatus[status]}")

if status == 1:
    # Print the total cost
    print(f"Total Cost: ${value(model.objective)}")

    # Print the optimal schedule
    for s in shifts:
        print(f"Shift {s}: {int(sum([x[s][h].varValue for h in hours]))} employees")
else:
    print("No feasible solution found.")





