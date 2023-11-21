import heapq

class Node:
    def __init__(self, level, profit, weight, include):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.include = include

    def __lt__(self, other):
        return self.profit > other.profit  # Sort nodes by profit (higher is better)


def branch_and_bound_backpack(weights, profits, capacity):
    n = len(weights)
    best_solution = [0] * n
    root = Node(-1, 0, 0, [])
    priority_queue = []
    heapq.heappush(priority_queue, root)
    max_profit = 0

    while priority_queue:
        node = heapq.heappop(priority_queue)

        level = node.level + 1
        weight = node.weight
        profit = node.profit

        if level == n:
            if profit > max_profit:
                max_profit = profit
                best_solution = node.include
            continue

        # Include the next item
        new_weight = weight + weights[level]
        new_profit = profit + profits[level]
        if new_weight <= capacity:
            include = node.include[:]
            include.append(1)
            heapq.heappush(priority_queue, Node(level, new_profit, new_weight, include))

        # Exclude the next item
        include = node.include[:]
        include.append(0)
        heapq.heappush(priority_queue, Node(level, profit, weight, include))

    return best_solution, max_profit


# Problem data
weights = [3, 4, 3, 3, 15, 13, 16]
profits = [12, 12, 9, 15, 90, 26, 112]
capacity = 35

# Solve the problem
best_solution, max_profit = branch_and_bound_backpack(weights, profits, capacity)

# Print the result
print("Best Solution:", best_solution)
print("Max Profit:", max_profit)
