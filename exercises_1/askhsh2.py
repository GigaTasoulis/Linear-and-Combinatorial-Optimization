import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# plotting the feasible region
d = np.linspace(0,2,300)
x1,y = np.meshgrid(d,d)

# define the constraints
con1 = y >= 0
con2 = 4.5*y >= 5.1-(6*x1)
con3 = 9*y <= 8.4-(6*x1)
con4 = 9*y <= 10.8-(12*x1)

feasible_region = (con1 & con2 & con3 & con4).astype(int)
plt.imshow(feasible_region, extent=(x1.min(),x1.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3)

# plot the lines defining the constraints
x1 = np.linspace(0, 16, 2000)

# y >= 0
y1 = x1*0

# 6x1 + 4,5x2 >= 5,1 
y2 = (5.1-6*x1)/4.5

# 6x1 + 9x2 <= 8,4 
y3 = (8.4-6*x1)/9

# 12x1 + 9x2 <= 10,8 
y4 = (10.8-(12*x1))/9




# Finding the vertices of the feasible area
A = np.array([[-6, -4.5], [6, 9], [12, 9], [-1, 0], [0, -1]])
b = np.array([-5.1, 8.4, 10.8, 0, 0])


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
        con2 = 4.5*y >= 5.1-(6*z1)
        con3 = 9*y <= 8.4-(6*z1)
        con4 = 9*y <= 10.8-(12*z1)
        
        # check if all constraints are satisfied
        if con1 and con2 and con3 and con4:
            print("Solution for pair", i+1, "and", j+1, ":", x, "satisfies the constraints.")
            vertices.append(x)
      except np.linalg.LinAlgError:
        continue

vertices = np.array(vertices)
x_values = vertices[:, 0]
y_values = vertices[:, 1]
z_values = 6*x_values + 7.5*y_values
min_z_index = np.argmin(z_values)
min_z_vertex = vertices[min_z_index]
min_z_value = np.min(z_values)
print("The vertex that minimizes the function is", min_z_vertex,"and the value is",min_z_value)


# Plot the feasible region
plt.plot(x1, y2, label=r'$6x_1 + 4.5x_2 \geq 5.1$',color='r')
plt.plot(x1, y3, label=r'$6x_1 + 9x_2 \leq 8.4$',color='b')
plt.plot(x1, y4, label=r'$12x_1 + 9x_2 \leq 10.8$',color='g')

plt.xlim(0, 2)
plt.ylim(0, 2)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend()

# plot the optimal solution points for each objective function
plt.plot(vertices[0][0], vertices[0][1], 'ro', markersize=5)
plt.plot(vertices[1][0], vertices[1][1], 'ro', markersize=5)
plt.plot(vertices[2][0], vertices[2][1], 'ro', markersize=5)
plt.plot(vertices[3][0], vertices[3][1], 'ro', markersize=5)

# Show the plot
plt.show()
