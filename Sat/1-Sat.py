import time
import sys
sys.setrecursionlimit(20000)  # Aumenta o limite para 20.000


# Variáveis globais para contagem
step_count = 0        # Contador de passos (iterações/recursões)
recursion_depth = 0   # Profundidade da árvore de recursão
max_depth = 0         # Profundidade máxima atingida
finished = False      # Indicador de solução encontrada

# Função para verificar se a atribuição é uma solução
def is_a_solution(assignment, k, var_count, formula):
    return k == var_count and is_satisfied(formula, assignment)

# Função para processar uma solução válida
def process_solution(assignment, k, formula):
    global finished
    if is_satisfied(formula, assignment):
        print(f"Solução encontrada: {assignment}")
        finished = True  # Termina o backtracking

# Função para gerar candidatos (0 ou 1)
def construct_candidates(assignment, k, var_count):
    return [0, 1]

# Função para verificar se a fórmula é satisfeita com a atribuição atual
def is_satisfied(formula, assignment):
    for clause in formula:
        if not any(
            (val == 1 and assignment[i] == 1) or  # Variável não-negada deve ser 1
            (val == 0 and assignment[i] == 0)     # Variável negada deve ser 0, para virar 1
            for i, val in enumerate(clause) if val != -1
        ):
            return False  # Se uma cláusula não é satisfeita, retorna falso
    return True  # Se todas as cláusulas forem satisfeitas, a solução é válida

# Função principal de backtracking
def backtrack(assignment, k, var_count, formula):
    global finished, step_count, recursion_depth, max_depth

    step_count += 1  # Conta cada passo (chamada da função)

    recursion_depth += 1  # Aumenta a profundidade da recursão
    max_depth = max(max_depth, recursion_depth)  # Atualiza a profundidade máxima

    if is_a_solution(assignment, k, var_count, formula):
        process_solution(assignment, k, formula)
    else:
        if k < var_count:  # Limite de variáveis
            candidates = construct_candidates(assignment, k, var_count)
            for candidate in candidates:
                assignment.append(candidate)  # Atribui um valor (0 ou 1)
                backtrack(assignment, k + 1, var_count, formula) 
                assignment.pop()  # Remove a atribuição após o retorno da recursão
                if finished:
                    return

    recursion_depth -= 1  # Diminui a profundidade ao retornar da recursão

# Função para resolver o problema SAT
def solve_sat(formula, var_count):
    global finished, step_count, max_depth
    finished = False  # Reseta a variável de terminação
    step_count = 0  # Reseta o contador de passos
    max_depth = 0  # Reseta a profundidade máxima
    start_time = time.time()  # Inicia a contagem do tempo

    backtrack([], 0, var_count, formula)

    end_time = time.time()  # Finaliza a contagem do tempo
    execution_time = end_time - start_time  # Tempo total de execução

    # Exibe as estatísticas
    print(f"Tempo de execução: {execution_time:.6f} segundos")
    print(f"Número de passos (iterações): {step_count}")
    print(f"Profundidade máxima da árvore de recursão: {max_depth}")

# Função para ler o arquivo de entrada
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        var_count = int(file.readline().strip())
        formula = []
        for line in file:
            clause = list(map(int, line.strip().split()))
            formula.append(clause)
    return formula, var_count

# Ponto de entrada do programa
if __name__ == "__main__":
    input_file = 'input1.txt'
    
    # Lê a fórmula e a quantidade de variáveis do arquivo
    formula, var_count = read_input_file(input_file)
    
    # Chama a função para resolver o SAT
    solve_sat(formula, var_count)
    
    # Se não houver solução, exibe a mensagem
    if not finished:
        print("Não existe solução.")
