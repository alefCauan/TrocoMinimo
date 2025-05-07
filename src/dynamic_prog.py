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
        The minimum number of coins needed, or -1 if it's not possible, and execution time.
    """
    if change_value == 0:
        return 0, 0.0

    dp = [0] + [change_value + 1] * change_value  # Usa um valor máximo fixo

    start = time.perf_counter()

    for coin in coins:
        for i in range(coin, change_value + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    end = time.perf_counter()

    result = dp[change_value] if dp[change_value] <= change_value else -1
    return result, end - start

