import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import Dijkstra

G = nx.Graph()

# vértices
nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
G.add_nodes_from(nodes)

# arestas ponderadas
edges = [
    (0, 1, 4), (0, 6, 7), (1, 2, 9), (1, 6, 11), (1, 7, 20),
    (2, 3, 6), (2, 4, 2), (3, 4, 10), (3, 5, 5), (4, 5, 15),
    (4, 7, 1), (4, 8, 5), (5, 8, 12), (6, 7, 1), (7, 8, 3)
]
G.add_weighted_edges_from(edges)


# definindo a posição dos nós
pos = {
    6: (0, -0.5), 1: (0, 0.5), 2: (1, 0.5), 3: (1.5, 0.5), 4: (1, 0),
    5: (2, 0), 0: (-1, 0), 7: (1, -0.5), 8: (1.5, -0.5)
}
plt.figure(figsize=(8, 6))

nx.draw(G, pos, with_labels=True, node_color='#404040', edge_color='#f06334', linewidths=3,
        width=4, node_size=1300, font_color='white', font_size=16, font_weight='bold', edgecolors='#f06334')

# pesos das arestas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=16, font_color='#404040')

plt.show() 

################################################################################################################

# dijkstra:
root = 0
pred, dist = Dijkstra(G, root)

# árvores de caminhos mínimos
A = nx.Graph()
A.add_node(root)
for node in pred:
    if node != root:
        A.add_node(node)
        A.add_edge(node, pred[node])
        
pos = {
    6: (0.75, 0.25), 1: (1.25, 0.25), 0: (1, 0.5), 3: (1, -0.75), 4: (1, -0.25),
    5: (1, -1), 2: (1, -0.5), 7: (0.75, 0), 8: (0.5, -0.25)
}
plt.figure(figsize=(8, 6))
        
nx.draw(A, pos, with_labels=True, node_color='#404040', edge_color='#f06334', linewidths=3,
        width=4, node_size=1300, font_color='white', font_size=16, font_weight='bold', edgecolors='#f06334')

# criar rótulos com a distância mínima ao lado de cada nó
labels = {node: f'\n\n\n(d={dist[node]})' for node in A.nodes()}
nx.draw_networkx_labels(A, pos, labels, font_size=16, font_color='black', font_weight='bold')

plt.show()