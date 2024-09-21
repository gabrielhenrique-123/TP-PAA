import time

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

if __name__ == "__main__":
    file_path = "independent_set_input.txt"  # Substituir pelo caminho correto
    num_vertices, graph = read_graph_input(file_path)
    
    start_time = time.time()
    max_independent_set = find_max_independent_set(graph, num_vertices)
    exec_time = time.time() - start_time
    
    print(f"Maior conjunto independente: {max_independent_set}")
    print(f"Tamanho do conjunto independente: {len(max_independent_set)}")
    print(f"Tempo de execução: {exec_time:.4f} segundos")
