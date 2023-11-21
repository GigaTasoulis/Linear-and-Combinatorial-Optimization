import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.DiGraph()

# Add nodes
G.add_node("x1x2x3s1s2s3")

# Add edges
G.add_edges_from([("x1x2x3s1s2s3", "x1s1"), ("x1x2x3s1s2s3", "x2"), ("x1x2x3s1s2s3", "x3"), ("x1s1", "s2"), ("x2", "s3"), ("x3", "s1")])

# Define node positions
pos = {"x1x2x3s1s2s3": (0, 0), "x1s1": (1, 1), "x2": (0, 2), "x3": (2, 2), "s2": (2, 1), "s3": (1, 0), "s1": (2, 0)}

# Draw the graph
nx.draw_networkx(G, pos, node_color='lightblue', node_size=1500, font_size=18, font_color='black', font_weight='bold')
plt.axis('off')
plt.show()
