import time
import os
from matplotlib import pyplot as plt

# Lista de moedas (em centavos, como inteiros)
coins = [5, 10, 25, 50, 100]

def calculate_recursive_minimum(change_value: int, coins=(1, 5, 10, 25)) -> tuple:
    """
    Calcula o número mínimo de moedas para um valor dado, usando recursão pura (sem memoização).

    Args:
        change_value: Valor alvo.
        coins: Tupla de moedas disponíveis.

    Returns:
        Uma tupla com (mínimo de moedas ou -1 se não possível, tempo de execução)
    """
    def min_coins(value):
        if value == 0:
            return 0
        if value < 0:
            return float('inf')
        return min((min_coins(value - c) + 1 for c in coins), default=float('inf'))

    start = time.time()
    result = min_coins(change_value)
    exec_time = time.time() - start

    return (result if result != float('inf') else -1, exec_time)