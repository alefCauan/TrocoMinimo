import time
import os
from matplotlib import pyplot as plt

# Lista de moedas (em centavos, como inteiros)
coins = [100, 50, 25, 10, 5]

def calculate_minimum_change(change_value: int) -> tuple:
    """
    Calculates the minimum number of coins needed to make a given amount using recursion with memoization.

    Args:
        change_value: The target amount.

    Returns:
        The minimum number of coins needed, or -1 if it's not possible, and execution time.
    """
    # Memoization cache
    memo = {}
    
    def min_coins(value: int) -> int:
        # Base cases
        if value == 0:
            return 0
        if value < 0:
            return float('inf')
        
        # Check if already computed
        if value in memo:
            return memo[value]
        
        # Try each coin and find minimum
        min_count = float('inf')
        for coin in coins:
            if coin <= value:
                result = min_coins(value - coin)
                if result != float('inf'):
                    min_count = min(min_count, result + 1)
        
        # Store result in memo
        memo[value] = min_count
        return min_count
    
    start = time.time()
    result = min_coins(change_value)
    end = time.time()
    exec_time = end - start
    
    # Return -1 if no solution found
    return (result if result != float('inf') else -1, exec_time)