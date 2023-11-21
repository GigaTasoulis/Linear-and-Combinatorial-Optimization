import numpy as np
import matplotlib.pyplot as plt

# plot the feasible region
d = np.linspace(-2,16,300)
x1,y = np.meshgrid(d,d)

# define the constraints
con1 = y >= 0
con2 = 2*y >= x1-1
con3 = 2*y >= 5-x1
con4 = y >= 4-2*x1

# plot the feasible region as a grey shaded area
plt.imshow((con1 & con2 & con3 & con4).astype(int), extent=(x1.min(),x1.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3)

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

# plot the constraint lines
plt.plot(x1, y1, label="x1 >= 0")
plt.plot(x1, y2, label="2x1 + x2 >= 4")
plt.plot(x1, y3, label="x1 + 2x2 >= 5")
plt.plot(x1, y4, label="x1 - 2x2 <= 1")

# # objective function (i): max Z = 2x1 - 5x2 = 1
x2 = (2*x1 - 1)/5
plt.plot(x1, x2, 'yellow', label="(i) Z")

# # objective function (ii): max Z = 2x1 - 4x2 = 2
x2 = (2*x1-2)/4
plt.plot(x1, x2, 'black', label="(ii) Z")


# plot the optimal solution points for each objective function
plt.plot(3, 1, 'ro', markersize=5, label="max(Z2) -> (3,1)")
plt.plot(3, 1, 'go', markersize=5, label="max(Z1) -> (3,1)")


# set the axis limits and labels
plt.xlim(0,16)
plt.ylim(0,11)
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.show()
