import time

def is_satisfied(formula, assignment):
    """Verifica se a fórmula booleana é satisfeita para uma atribuição dada."""
    for clause in formula:
        clause_satisfied = False
        for i, val in enumerate(clause):
            if val == 1 and assignment[i] == 1:
                clause_satisfied = True
                break
            elif val == 0 and assignment[i] == 0:
                clause_satisfied = True
                break
        if not clause_satisfied:
            return False
    return True

def backtrack(formula, assignment, var_count):
    """Função de Backtracking para encontrar uma solução satisfatória."""
    if len(assignment) == var_count:
        return assignment if is_satisfied(formula, assignment) else None
    
    # Tentar atribuir 0 e 1 para a próxima variável
    for value in [0, 1]:
        result = backtrack(formula, assignment + [value], var_count)
        if result:
            return result
    return None

def solve_sat(formula, var_count):
    """Resolve o problema de SAT usando Backtracking."""
    return backtrack(formula, [], var_count)

def read_sat_input(file_path):
    """Lê a entrada do arquivo de SAT."""
    with open(file_path, 'r') as f:
        var_count = int(f.readline().strip())
        formula = [list(map(int, line.strip().split())) for line in f if line.strip()]
    return var_count, formula

if __name__ == "__main__":
    file_path = "sat_input.txt"  # Substituir pelo caminho correto
    var_count, formula = read_sat_input(file_path)
    
    start_time = time.time()
    solution = solve_sat(formula, var_count)
    exec_time = time.time() - start_time
    
    if solution:
        print(f"Solução encontrada: {solution}")
    else:
        print("Não existe solução.")
    print(f"Tempo de execução: {exec_time:.4f} segundos")
