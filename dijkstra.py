import networkx as nx
from heapq import heapify, heappop, heappush

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

def Dijkstra(G: nx.Graph, s):
    # init
    distances = {node: float("inf") for node in G.nodes}    # lambda(v)
    predecessors = {node: None for node in G.nodes}         # pi(v)
    distances[s] = 0
    
    # lista de prioridades
    Q = []
    heapify(Q)
    for node in distances:
        heappush(Q, (distances[node], node))
    
    print(Q)
    while Q:
        current_distance, current_node = heappop(Q)
        print(f'{current_node=}')                 # extrair node com maior prioridade
        for v in list(G.adj[current_node]):                         # para cada vizinho do node atual:
            print(f'{v=}')
            weight = G.get_edge_data(v, current_node)['weight']     # peso da aresta entre o node atual e um de seus vizinhos
            new_distance = current_distance + weight
            if new_distance < distances[v]:
                # o melhor caminho para chegar em v é pelo node atual                         
                distances[v] = new_distance
                predecessors[v] = current_node
                Q = update_priority(Q, v, new_distance)
            print(Q)
            print(predecessors)
            print()
            
    print(distances)
    print(predecessors)
    
def update_priority(Q, element, new_priority):
    # Remover a entrada existente
    Q = [item for item in Q if item[1] != element]
    
    # Inserir o novo elemento com prioridade atualizada
    heappush(Q, (new_priority, element))
    
    return Q

Dijkstra(G, 0)
    