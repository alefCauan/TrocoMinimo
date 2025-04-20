import time
import os
from matplotlib import pyplot as plt

# Lista de moedas
coins = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.10, 0.05]

def calculate_minimum_change(change_value: float) -> tuple:
    result = []
    start = time.time()

    for coin in coins:
        while change_value >= coin:
            result.append(coin)
            change_value -= coin

    end = time.time()
    exec_time = end - start
    return result, exec_time

execution_times = []
change_values = []

# Obter o diretório base do script (TrocoMinimo/src)
script_dir = os.path.dirname(os.path.abspath(__file__))  # Caminho absoluto de src
base_dir = os.path.dirname(script_dir)  # Sobe um nível para TrocoMinimo

# Caminhos absolutos para os arquivos
file_path = os.path.join(base_dir, "sets", "sets.txt")  # TrocoMinimo/sets/sets.txt
image_path = os.path.join(base_dir, "results", "dinamic_execution_time.png")  # TrocoMinimo/results/execution_time.png

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
            _, exec_time = calculate_minimum_change(value)
            execution_times.append(exec_time)
except ValueError:
    print("Erro: O arquivo 'sets.txt' contém valores inválidos.")
    exit(1)

# Gerar o gráfico com os resultados usando programação dinâmica
plt.plot(change_values, execution_times, marker='o')
plt.title("Time with Greedy Algorithm")  # Corrigido o título (não é programação dinâmica)
plt.xlabel("Change Value in millions")
plt.ylabel("Execution Time (s)")
plt.grid(True)

# Salvar a imagem
plt.savefig(image_path, bbox_inches='tight')
plt.show()