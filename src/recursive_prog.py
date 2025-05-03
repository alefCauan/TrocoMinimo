import time
import os
import sys
from matplotlib import pyplot as plt

# Aumentar ainda mais o limite de recursão
sys.setrecursionlimit(50000)

# Lista de moedas
coins = [100, 50, 25, 10, 5]

def calculate_minimum_change_recursive(change_value: int, result=None) -> list:
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



def measure_recursive_execution(value: int) -> tuple:
    start = time.time()
    result = calculate_minimum_change_recursive(value)
    end = time.time()
    exec_time = end - start
    return result, exec_time
