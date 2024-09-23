import time

def is_satisfied(formula, assignment):
    """Verifica se a fórmula booleana é satisfeita para uma atribuição dada."""
    print(assignment)
    for clause in formula:
        if not any(
            (val == 1 and assignment[i] == 1) or  # Variável é 1 na clausula 1 e no assignment é 1 também
            (val == 0 and assignment[i] == 0)     # Variável é 0 e no assignment é 0 também, virando 1
            for i, val in enumerate(clause) if val != -1  # Ignora variáveis não presentes
        ):
            return False  # Se uma cláusula não é satisfeita, retorna False
    return True  # Se todas as cláusulas forem satisfeitas, retorna True

def backtrack(formula, assignment, var_count):
    """Função de Backtracking para encontrar uma solução satisfatória."""
    if len(assignment) == var_count:
        if is_satisfied(formula, assignment):
            return assignment
        else:
            return None
    
    # Testa atribuir 0 ou 1 para a próxima variável
    for value in [0, 1]:
        result = backtrack(formula, assignment + [value], var_count)
        if result:
            return result
    return None

def solve_sat(formula, var_count):
    """Resolve o problema de SAT usando Backtracking."""
    return backtrack(formula, [], var_count)

def read_input_file(file_path):
    """Lê o arquivo de entrada e retorna a fórmula e a contagem de variáveis."""
    with open(file_path, 'r') as file:
        var_count = int(file.readline().strip())
        formula = []
        for line in file:
            clause = list(map(int, line.strip().split()))
            formula.append(clause)
        print(formula)
    return formula, var_count

if __name__ == "__main__":
    # Substitua 'input.txt' pelo caminho do seu arquivo de entrada
    input_file = 'input.txt'
    
    formula, var_count = read_input_file(input_file)
    
    start_time = time.time()
    solution = solve_sat(formula, var_count)
    exec_time = time.time() - start_time
    
    if solution:
        print(f"Solução encontrada: {solution}")
    else:
        print("Não existe solução.")
    print(f"Tempo de execução: {exec_time:.4f} segundos")
