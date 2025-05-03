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

