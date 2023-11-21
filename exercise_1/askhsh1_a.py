import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


# plot the feasible region
d = np.linspace(-2,16,300)
x1,y = np.meshgrid(d,d)

# displays a 2D image and greys out the feasible area
plt.imshow( ((y>=0) & (2*y>=x1-1) & (2*y>=5-x1) & (y>=4-2*x1)).astype(int) , 
            extent=(x1.min(),x1.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3)


# plot the lines defining the constraints
x1 = np.linspace(0, 16, 2000)

# y >= 0
y1 = x1*0

# 2x1 + y ≥ 4
y2 = 4-2*x1

# x1 + 2y ≥ 5
y3 = (5-x1)/2

# x1 - 2y ≤ 1
y4 = (x1-1)/2


# Make plot
plt.plot(x1, 0*np.ones_like(y1), label="x1 >= 0")
plt.plot(x1, y2, label="2x1 + x2 >= 4")
plt.plot(x1, y3, label="x1 + 2x2 >= 5")
plt.plot(x1, y4, label="x1 - 2x2 <= 1")


# Find all possible vertices
A = np.array([[-2, -1], [-1, -2], [1, -2]])
b = np.array([-4, -5, 1])

vertices = []
for i in range(len(A)):
    for j in range(i+1, len(A)):
      try:
        sub_A = A[[i, j], :]
        sub_b = b[[i, j]]
        x = np.linalg.solve(sub_A, sub_b)
        # evaluate the constraints for the current solution
        y = x[1]
        z1 = x[0]
        con1 = y >= 0
        con2 = 2*y >= z1-1
        con3 = 2*y >= 5-z1
        con4 = y >= 4-2*z1
        
        # check if all constraints are satisfied
        if con1 and con2 and con3 and con4:
            print("Solution for pair", i+1, "and", j+1, ":", x, "satisfies the constraints.")
            vertices.append(x)
      except np.linalg.LinAlgError:
        continue

# vertices of objective function
vertices = np.array(vertices)
x_values = vertices[:, 0]
y_values = vertices[:, 1]
z_values = 2*x_values - 3*y_values # Objective Function
max_z_index = np.argmax(z_values)
max_z_vertex = vertices[max_z_index]
max_z_value = np.max(z_values)
print("The vertex that maximizes the function is", max_z_vertex,"and the value is",max_z_value)

# plot the optimal solution points for each objective function
plt.plot(vertices[0][0], vertices[0][1], 'ro', markersize=5)
plt.plot(vertices[1][0], vertices[1][1], 'ro', markersize=5)
plt.plot(0,4, 'ro', markersize=5)

# Define the limits for the display
plt.xlim(0,16)
plt.ylim(0,11)




plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.show()

