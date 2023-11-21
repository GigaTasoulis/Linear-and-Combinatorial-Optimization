import numpy as np

# Define the objective function coefficients
c = np.array([-2, -4, -1, -1], dtype=float)  # Convert to float

# Define the constraint coefficients
A = np.array([[1, 3, 0, 1], [2, 1, 0, 0], [0, 1, 4, 1]], dtype=float)
b = np.array([8, 6, 6], dtype=float)

# Identify the non-basic variable index
nonbasic_variable_index = 3  # Assuming x₄ is the non-basic variable

# Check if the coefficient of the non-basic variable is already zero
if c[nonbasic_variable_index] == 0:
    print("The coefficient of the non-basic variable is already zero.")
else:
    # Find the entering constraint
    entering_constraint_index = None
    min_ratio = np.inf

    for i in range(len(A)):
        if A[i, nonbasic_variable_index] != 0:
            ratio = b[i] / A[i, nonbasic_variable_index]
            if ratio >= 0 and ratio < min_ratio:
                min_ratio = ratio
                entering_constraint_index = i

    if entering_constraint_index is None:
        print("No entering constraint found.")
    else:
        # Perform the pivot operation to convert the non-basic variable into a basic variable
        pivot_element = A[entering_constraint_index, nonbasic_variable_index]
        A[entering_constraint_index, :] /= pivot_element
        b[entering_constraint_index] /= pivot_element

        for i in range(len(A)):
            if i != entering_constraint_index:
                ratio = A[i, nonbasic_variable_index] / A[entering_constraint_index, nonbasic_variable_index]
                A[i, :] -= ratio * A[entering_constraint_index, :]
                b[i] -= ratio * b[entering_constraint_index]

        # Update the objective function coefficient of the non-basic variable
        c -= c[nonbasic_variable_index] * A[entering_constraint_index, :] / pivot_element

        print("Objective function coefficients after conversion:")
        print(c)
