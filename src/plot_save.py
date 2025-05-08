import matplotlib.pyplot as plt
import os
import numpy as np

# Data for dynamic and recursive approaches
iterations = list(range(1, 11))

# Dynamic data
dynamic_value1 = [10.020486, 10.065243, 10.023443, 9.792127, 9.693773, 10.102236, 9.445680, 9.418045, 9.881601, 9.534019]
dynamic_value2 = [9.403212, 9.460287, 9.304473, 9.541313, 9.822198, 9.759624, 9.682617, 9.640107, 12.540857, 10.908152]
dynamic_memory1 = [17760.074219, 17761.710938, 17761.804688, 17761.898438, 17761.992188, 17762.210938, 17762.304688, 17762.398438, 17762.492188, 17762.835938]
dynamic_memory2 = [42788.644531, 42788.863281, 42788.957031, 42789.050781, 42789.144531, 42789.363281, 42789.457031, 42789.550781, 42789.644531, 42789.988281]

# Recursive data
recursive_value1 = [0.000178, 0.000181, 0.000172, 0.000190, 0.000167, 0.000169, 0.000177, 0.000176, 0.000176, 0.000175]
recursive_value2 = [0.000155, 0.000156, 0.000142, 0.000149, 0.000149, 0.000157, 0.000154, 0.000147, 0.000900, 0.000141]
recursive_memory1 = [211.261719, 212.781250, 212.875000, 212.968750, 213.125000, 213.281250, 213.375000, 213.468750, 213.687500, 213.906250]
recursive_memory2 = [508.539062, 508.695312, 508.789062, 508.882812, 509.039062, 509.195312, 509.289062, 509.382812, 509.601562, 509.820312]

# Set up file paths
script_dir = os.path.dirname(os.path.abspath(__file__))  # dir/src/
base_dir = os.path.dirname(script_dir)  # dir/
results_dir = os.path.join(base_dir, "results")  # dir/results/

# Ensure results directory exists
os.makedirs(results_dir, exist_ok=True)

# Function to create and save a plot
def save_plot(x_data, y1_data, y2_data, title, filename, ylabel, label1, label2):
    plt.figure(figsize=(8, 6))
    plt.plot(x_data, y1_data, marker='o', label=label1, color='blue')
    plt.plot(x_data, y2_data, marker='o', label=label2, color='red')
    plt.title(title)
    plt.xlabel("Iteration")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(results_dir, filename), bbox_inches='tight')
    plt.close()

# Save each plot individually
# Value 1 comparison
save_plot(
    iterations, dynamic_value1, recursive_value1,
    "Time with 1347637", "value1_comparison.png",
    "Time (s)", "Dynamic", "Recursive"
)

# Value 2 comparison
save_plot(
    iterations, dynamic_value2, recursive_value2,
    "Time with 3231923", "value2_comparison.png",
    "Time (s)", "Dynamic", "Recursive"
)

# Memory 1 comparison
save_plot(
    iterations, dynamic_memory1, recursive_memory1,
    "Memory with 1347637", "memory1_comparison.png",
    "Memory (KB)", "Dynamic", "Recursive"
)

# Memory 2 comparison
save_plot(
    iterations, dynamic_memory2, recursive_memory2,
    "Memory with 3231923", "memory2_comparison.png",
    "Memory (KB)", "Dynamic", "Recursive"
)

# Calculate averages for bar plots
avg_dynamic_value1 = sum(dynamic_value1) / len(dynamic_value1)
avg_recursive_value1 = sum(recursive_value1) / len(recursive_value1)
avg_dynamic_value2 = sum(dynamic_value2) / len(dynamic_value2)
avg_recursive_value2 = sum(recursive_value2) / len(recursive_value2)
avg_dynamic_memory1 = sum(dynamic_memory1) / len(dynamic_memory1)
avg_recursive_memory1 = sum(recursive_memory1) / len(recursive_memory1)
avg_dynamic_memory2 = sum(dynamic_memory2) / len(dynamic_memory2)
avg_recursive_memory2 = sum(recursive_memory2) / len(recursive_memory2)

# Set up file paths
script_dir = os.path.dirname(os.path.abspath(__file__))  # dir/src/
base_dir = os.path.dirname(script_dir)  # dir/
results_dir = os.path.join(base_dir, "results")  # dir/results/
os.makedirs(results_dir, exist_ok=True)

# Function to create and save a bar plot with values on top
def save_bar_plot(x, heights1, heights2, title, filename, ylabel, labels):
    plt.figure(figsize=(8, 6))
    x_pos = np.arange(len(x))
    bars1 = plt.bar(x_pos - 0.2, heights1, 0.4, label=labels[0], color='cyan')
    bars2 = plt.bar(x_pos + 0.2, heights2, 0.4, label=labels[1], color='red')
    
    # Add values on top of each bar
    for bar in bars1:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 f'{height:.6f}' if ylabel == "Average Time (s)" else f'{height:.2f}',
                 ha='center', va='bottom')
    for bar in bars2:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 f'{height:.6f}' if ylabel == "Average Time (s)" else f'{height:.2f}',
                 ha='center', va='bottom')
    
    plt.xlabel("Value/Memory Type")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(x_pos, x)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, filename), bbox_inches='tight')
    plt.close()

# Time comparison bar plot
save_bar_plot(
    ['Value 1', 'Value 2'],
    [avg_dynamic_value1, avg_dynamic_value2],
    [avg_recursive_value1, avg_recursive_value2],
    "Time Comparison: Dynamic vs Recursive",
    "time_comparison_bar.png",
    "Average Time (s)",
    ["Dynamic", "Recursive"]
)

# Memory comparison bar plot
save_bar_plot(
    ['Memory 1', 'Memory 2'],
    [avg_dynamic_memory1, avg_dynamic_memory2],
    [avg_recursive_memory1, avg_recursive_memory2],
    "Memory Comparison: Dynamic vs Recursive",
    "memory_comparison_bar.png",
    "Average Memory (KB)",
    ["Dynamic", "Recursive"]
)