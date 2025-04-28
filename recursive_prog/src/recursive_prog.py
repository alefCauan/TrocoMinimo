import time
import os
import sys
from matplotlib import pyplot as plt

# Aumentar ainda mais o limite de recursão
sys.setrecursionlimit(50000)

# Lista de moedas
coins = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.10, 0.05]

def calculate_minimum_change_recursive(change_value: float, result=None) -> list:
    if result is None:
        result = []
    
    # Arredondar o valor para evitar problemas com ponto flutuante
    change_value = round(change_value, 2)
    
    # Caso base: quando o valor do troco for zero ou próximo de zero
    if change_value <= 0.001:
        return result
    
    # Encontrar a maior moeda que pode ser usada e usar o máximo possível dela
    for coin in coins:
        if change_value >= coin:
            # Calcular quantas vezes podemos usar esta moeda
            num_coins = int(change_value // coin)
            result.extend([coin] * num_coins)
            remaining = round(change_value - (coin * num_coins), 2)
            
            # Verificação adicional para evitar loops infinitos
            if remaining < 0.001:
                return result
                
            return calculate_minimum_change_recursive(remaining, result)
    
    return result



def measure_recursive_execution(value: float) -> tuple:
    start = time.time()
    result = calculate_minimum_change_recursive(value)
    end = time.time()
    exec_time = end - start
    return result, exec_time

execution_times = []
change_values = []

# Obter o diretório base do script
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(script_dir)

# Caminhos absolutos para os arquivos
file_path = os.path.join(base_dir, "sets", "sets.txt")
image_path = os.path.join(base_dir, "results", "recursive_execution_time.png")  # Nome novo para a imagem

# Verificar se o arquivo sets.txt existe
if not os.path.exists(file_path):
    print(f"Erro: Arquivo '{file_path}' não encontrado.")
    exit(1)

# Leitura do arquivo sets.txt
try:
    with open(file_path, "r") as file:
        for line in file:
            value = float(line.strip())
            change_values.append(value)
            _, exec_time = measure_recursive_execution(value)
            execution_times.append(exec_time)
except ValueError:
    print("Erro: O arquivo 'sets.txt' contém valores inválidos.")
    exit(1)

# Gerar o gráfico
plt.plot(change_values, execution_times, marker='o', color='red')
plt.title("Time with Recursive Algorithm")
plt.xlabel("Change Value in millions")
plt.ylabel("Execution Time (s)")
plt.grid(True)

# Salvar a imagem
plt.savefig(image_path, bbox_inches='tight')
plt.show()
