import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# define the values for x1, x2, and x3
n_points = 300
x1 = np.linspace(0, 10, n_points)
x2 = np.linspace(0, 10, n_points)
x3 = np.linspace(0, 10, n_points)

# define the constraints
con1 = -3*x1[:, np.newaxis, np.newaxis] + 2*x2[np.newaxis, :, np.newaxis] + 8*x3[np.newaxis, np.newaxis, :] <= 17
con2 = -x1[:, np.newaxis, np.newaxis] + x2[np.newaxis, :, np.newaxis] + 3*x3[np.newaxis, np.newaxis, :] <= 9
con3 = -2*x1[:, np.newaxis, np.newaxis] + x2[np.newaxis, :, np.newaxis] + 8*x3[np.newaxis, np.newaxis, :] <= 16


# Finding the vertices of the feasible area
A = np.array([[-3, 2, 8], [-1, 1, 3], [-2, 1, 8], [-1, 0, 0], [0, -1, 0], [0, 0, -1]])
b = np.array([17, 9, 16, 0, 0, 0])

vertices = []
for i in range(len(A)):
    for j in range(i+1, len(A)):
      for k in range(j+1, len(A)):
        try:
          sub_A = A[[i, j, k], :]
          sub_b = b[[i, j, k]]
          x = np.linalg.solve(sub_A, sub_b)
          # evaluate the constraints for the current solution
          x1 = x[0]
          x2 = x[1]
          x3 = x[2]
          con1 = -3*x1 + 2*x2 + 8*x3 <= 17
          con2 = -x1 + x2 + 3*x3 <= 9
          con3 = -2*x1 + x2 + 8*x3 <= 16
          con4 = x1 >= 0
          con5 = x2 >= 0
          con6 = x3 >= 0
          
          # check if all constraints are satisfied
          if con1 and con2 and con3 and con4 and con5 and con6:
            # print("Solution for pair", i+1, "and", j+1,"and", k+1, ":", x, "satisfies the constraints.")
            vertices.append(x)
          else: 
            #print("Solution for pair", i+1, "and", j+1, "and", k+1, ":", x, "does not satisfy the constraints.")
            continue
        except np.linalg.LinAlgError:
          continue


vertices = np.array(vertices)
print(vertices)

x1_values = vertices[:, 0]
x2_values = vertices[:, 1]
x3_values = vertices[:, 2]
z_values = 12*x1_values - 10*x2_values - 30*x3_values
min_z_index = np.argmin(z_values)
min_z_vertex = vertices[min_z_index]
min_z_value = np.min(z_values)
print("The vertex that minimizes the function is", min_z_vertex,"and the value is",min_z_value)

# Find the degenerate basic solutions
deg_solutions = []
for sol in vertices:
    if 0 in sol:
        deg_solutions.append(sol)
print("The degenerate solutions are\n",deg_solutions)