import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        # Lê a quantidade de vértices da primeira linha
        num_vertices = int(file.readline().strip())
        
        # Lê as próximas linhas e monta a matriz de adjacência
        graph = []
        for _ in range(num_vertices):
            row = list(map(int, file.readline().strip().split()))
            graph.append(row)
    
    return graph, num_vertices

def is_clique(graph, subset):
    """Verifica se um conjunto de vértices forma um clique."""
    return all(graph[i][j] == 1 for i in subset for j in subset if i != j)

def branch_and_bound_clique(graph, candidates, clique, max_clique):
    """Implementa o Branch and Bound para encontrar o maior clique."""
    if len(clique) > len(max_clique[0]):
        max_clique[0] = clique[:]
    
    for v in candidates:
        new_candidates = [w for w in candidates if graph[v][w] == 1]
        branch_and_bound_clique(graph, new_candidates, clique + [v], max_clique)

def find_max_clique(graph, num_vertices):
    """Encontra o maior clique no grafo."""
    max_clique = [[]]
    candidates = list(range(num_vertices))
    branch_and_bound_clique(graph, candidates, [], max_clique)
    return max_clique[0]

if __name__ == "__main__":
    # Nome do arquivo com a matriz de adjacência
    filename = "Entradas/grafo_200.txt"  # Certifique-se de que o arquivo esteja no mesmo diretório
    
    # Lê o grafo do arquivo
    graph, num_vertices = read_graph_from_file(filename)

    # Encontra o maior clique
    start_time = time.time()
    max_clique = find_max_clique(graph, num_vertices)
    exec_time = time.time() - start_time

    print(f"Maior clique encontrado: {max_clique}")
    print(f"Vértices do clique: {', '.join(map(str, max_clique))}")
    print(f"Tempo de execução: {exec_time:.4f} segundos")

    # Criar o grafo a partir da matriz de adjacência
    G = nx.from_numpy_array(np.array(graph))

    # Criar uma lista de cores para os nós e as arestas
    node_color = ['red' if node in max_clique else 'lightblue' for node in G.nodes()]
    edge_color = ['red' if (u in max_clique and v in max_clique) else 'lightgray' for u, v in G.edges()]

    # Desenhar o grafo
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color=node_color, edge_color=edge_color, node_size=700, font_size=10, font_color='black')
    plt.title('Grafo com Clique Máximo Destacado')
    plt.show()
