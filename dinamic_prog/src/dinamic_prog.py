import time
import os
from matplotlib import pyplot as plt

# Lista de moedas (em centavos, como inteiros)
coins = [100, 50, 25, 10, 5]

def calculate_minimum_change(change_value: int) -> tuple:
    """
    Calculates the minimum number of coins needed to make a given amount.

    Args:
        change_value: The target amount.

    Returns:
        The minimum number of coins needed, or -1 if it's not possible.
    """
    dp = [float('inf')] * (change_value + 1)
    dp[0] = 0

    start = time.time()
    for coin in coins:
        for i in range(coin, change_value + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    result = dp[change_value] if dp[change_value] != float('inf') else -1
    
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
image_path = os.path.join(base_dir, "results", "dynamic_execution_time.png")  # TrocoMinimo/results/dynamic_execution_time.png

# Verificar se o arquivo sets.txt existe
if not os.path.exists(file_path):
    print(f"Erro: Arquivo '{file_path}' não encontrado.")
    exit(1)

# Leitura do arquivo sets.txt
try:
    with open(file_path, "r") as file:
        for line in file:
            value = int(line.strip())  # Assume valores inteiros em centavos
            change_values.append(value)
            _, exec_time = calculate_minimum_change(value)
            execution_times.append(exec_time)
except ValueError:
    print("Erro: O arquivo 'sets.txt' contém valores inválidos.")
    exit(1)

# Gerar o gráfico com os resultados usando programação dinâmica
plt.plot(change_values, execution_times, marker='o')
plt.title("Time with Dynamic Programming")
plt.xlabel("Change Value in cents")
plt.ylabel("Execution Time (s)")
plt.grid(True)

# Salvar a imagem
plt.savefig(image_path, bbox_inches='tight')
