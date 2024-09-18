import networkx as nx
import matplotlib.pyplot as plt

nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
G = nx.Graph()

G.add_nodes_from(nodes)

# Arestas
edges = [
    (0, 1, 4), (0, 6, 7), (1, 2, 9), (1, 6, 11), (1, 7, 20),
    (2, 3, 6), (2, 4, 2), (3, 4, 10), (3, 5, 5), (4, 5, 15),
    (4, 7, 1), (4, 8, 5), (5, 8, 12), (6, 7, 1), (7, 8, 3)
]
G.add_weighted_edges_from(edges)

# Definindo a posição dos nós
pos = {
    6: (0, -0.5), 1: (0, 0.5), 2: (1, 0.5), 3: (1.5, 0.5), 4: (1, 0),
    5: (2, 0), 0: (-1, 0), 7: (1, -0.5), 8: (1.5, -0.5)
}
plt.figure(figsize=(8, 6))

nx.draw(G, pos, with_labels=True, node_color='#404040', edge_color='#f06334', linewidths=3,
        width=4, node_size=1300, font_color='white', font_size=16, font_weight='bold', edgecolors='#f06334')

# Pesos das arestas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=16, font_color='#404040')

plt.show()