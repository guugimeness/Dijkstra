import networkx as nx
from heapq import heapify, heappop, heappush

def Dijkstra(G: nx.Graph, s):
    # init
    distances = {node: float("inf") for node in G.nodes}    # lambda(v)
    predecessors = {node: None for node in G.nodes}         # pi(v)
    distances[s] = 0    # lambda(raiz) = 0
    
    # fila de prioridades
    Q = []
    heapify(Q)
    for node in distances:
        heappush(Q, (distances[node], node))
    print(f'Fila inicial: {Q=}')
    print()

    # set para marcar os vértices que já saíram da fila
    visited = set()
    
    while Q:
        u_distance, u = heappop(Q)                  # extrair vértice com maior prioridade
        visited.add(u)                              
        
        for v in list(G.adj[u]):        # para cada vizinho de u:
            if v in visited:        # vértice saiu da fila -> não muda mais o caminho até ele
                continue
            
            print(f'{u=} {v=}')
            weight = G.get_edge_data(v, u)['weight']     # peso da aresta entre o node atual(u) e um de seus vizinhos(v): w(u, v)
            new_distance = u_distance + weight          
            
            if new_distance < distances[v]:         # verifica se é melhor chegar em v por u
                distances[v] = new_distance
                predecessors[v] = u
                Q = update_priority(Q, v, new_distance)
                
            print(f'{Q=}')
            print(f'{predecessors=}')
            print()
                
    return predecessors, distances

# método para atualizar a prioridade na fila
def update_priority(Q, element, new_priority):
    # remover a entrada existente
    Q = [item for item in Q if item[1] != element]
    
    # inserir o novo elemento com prioridade atualizada
    heappush(Q, (new_priority, element))
    
    return Q