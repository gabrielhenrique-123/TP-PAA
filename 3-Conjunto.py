import time

def branch_and_bound_clique(graph, candidates, clique, max_clique):
    """Implementa o Branch and Bound para encontrar o maior clique."""
    if len(clique) > len(max_clique[0]):
        max_clique[0] = clique[:]
    
    for v in candidates:
        new_candidates = [w for w in candidates if graph[v][w] == 1]
        branch_and_bound_clique(graph, new_candidates, clique + [v], max_clique)
        
def invert_graph(graph, num_vertices):
    """Inverte as arestas de um grafo."""
    inverted_graph = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:
                inverted_graph[i][j] = 1 - graph[i][j]
    return inverted_graph

def find_max_independent_set(graph, num_vertices):
    """Encontra o maior conjunto independente usando a redução para Clique."""
    inverted_graph = invert_graph(graph, num_vertices)
    return find_max_clique(inverted_graph, num_vertices)

def find_max_clique(graph, num_vertices):
    """Encontra o maior clique no grafo."""
    max_clique = [[]]
    candidates = list(range(num_vertices))
    branch_and_bound_clique(graph, candidates, [], max_clique)
    return max_clique[0]

if __name__ == "__main__":
    # Exemplo de entrada direta para o problema de Conjunto Independente
    num_vertices = 9
    graph = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0]
    ]
    
    start_time = time.time()
    max_independent_set = find_max_independent_set(graph, num_vertices)
    exec_time = time.time() - start_time
    
    print(f"Maior conjunto independente: {max_independent_set}")
    print(f"Vértices do conjunto independente: {', '.join(map(str, max_independent_set))}")
    print(f"Tempo de execução: {exec_time:.4f} segundos")
