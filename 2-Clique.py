import time

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
    # Exemplo de entrada direta para o problema de Clique
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
    max_clique = find_max_clique(graph, num_vertices)
    exec_time = time.time() - start_time
    
    print(f"Maior clique encontrado: {max_clique}")
    print(f"Vértices do clique: {', '.join(map(str, max_clique))}")
    print(f"Tempo de execução: {exec_time:.4f} segundos")
