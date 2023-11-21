def simplex_iteration(tableau):
    # Find the pivot column and row
    pivot_col = min(range(len(tableau[0]) - 1), key=lambda i: tableau[0][i])
    ratios = [(i, tableau[i][-1] / tableau[i][pivot_col]) for i in range(1, len(tableau))]
    pivot_row = min(filter(lambda x: x[1] >= 0, ratios), key=lambda x: x[1])[0]

    # Update the pivot element
    pivot = tableau[pivot_row][pivot_col]
    pivot_row_vals = [val / pivot for val in tableau[pivot_row]]
    for i, row in enumerate(tableau):
        if i == pivot_row:
            continue
        factor = row[pivot_col] / pivot
        tableau[i] = [row[j] - factor * pivot_row_vals[j] for j in range(len(row))]

    # Update the basis
    tableau[pivot_row] = pivot_row_vals
    basis = [pivot_col] + [row.index(1) for row in tableau[1:]]

    return tableau, basis

def print_tableau(tableau):
    for row in tableau:
        for item in row:
            print("{:7.2f}".format(item), end="")
        print()


# Define the initial tableau
tableau = [[1.15,   0.33,   1.47,   2.15,   0.00,  0.00,   4.33],
   [0.49,   1.00,   1.49,   0.49,   0.00,   0.00,   1.00],
   [2.58,   0.16,   0.74,  -0.42,   1.00,   0.00,   1.16],
   [-0.04,  -1.15,  -5.19,  -2.04,   0.00,   1.00,  -0.15]
]

# Print the initial tableau
print("Initial tableau:")
print_tableau(tableau)

try:
    # Perform one Simplex iteration
    tableau, basis = simplex_iteration(tableau)
    # Extract the updated solution
    optimal_value = -tableau[0][-1]
    optimal_solution = [0] * len(tableau[0])  # initialize to all zeros
    for i, j in enumerate(basis[1:]):
        optimal_solution[j] = tableau[i + 1][-1]

    # Print the updated tableau
    print("\nUpdated tableau:")
    print_tableau(tableau)

    # Print the optimal value and solution
    print("\nOptimal value: {}\nOptimal solution: {}".format(optimal_value, optimal_solution[:-1]))
except ZeroDivisionError:
    print("Simplex Method terminated.")



