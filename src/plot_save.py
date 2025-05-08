
import matplotlib.pyplot as plt
import os
import numpy as np

# Data for dynamic and recursive approaches
iterations = list(range(1, 11))

# Updated Dynamic data
dynamic_value1 = [0.000010, 0.000005, 0.000004, 0.000004, 0.000004, 0.000004, 0.000004, 0.000004, 0.000004, 0.000004]
dynamic_value2 = [0.000009, 0.000014, 0.000014, 0.000024, 0.000014, 0.000014, 0.000014, 0.000014, 0.000013, 0.000014]
dynamic_memory1 = [0.789062, 23.830078, 24.142578, 24.455078, 24.767578, 25.205078, 25.517578, 25.830078, 26.197266, 26.814453]
dynamic_memory2 = [27.697266, 62.876953, 63.244141, 63.611328, 63.978516, 64.470703, 64.837891, 65.205078, 65.572266, 66.189453]

# Updated Recursive data
recursive_value1 = [0.002596, 0.002492, 0.002493, 0.002471, 0.002478, 0.002468, 0.002457, 0.002521, 0.002499, 0.002512]
recursive_value2 = [36.297595, 37.038244, 37.276428, 37.288868, 36.771062, 36.643205, 36.546799, 36.766517, 36.548973, 37.562128]
recursive_memory1 = [27.105469, 27.634766, 27.947266, 28.259766, 28.634766, 29.009766, 29.322266, 29.689453, 30.181641, 30.673828]
recursive_memory2 = [71.458984, 71.892578, 72.259766, 72.626953, 73.056641, 73.486328, 73.853516, 74.220703, 74.712891, 75.205078]

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
    "Time with 20", "value1_comparison.png",
    "Time (s)", "Dynamic", "Recursive"
)

# Value 2 comparison
save_plot(
    iterations, dynamic_value2, recursive_value2,
    "Time with 40", "value2_comparison.png",
    "Time (s)", "Dynamic", "Recursive"
)

# Memory 1 comparison
save_plot(
    iterations, dynamic_memory1, recursive_memory1,
    "Memory with 20", "memory1_comparison.png",
    "Memory (KB)", "Dynamic", "Recursive"
)

# Memory 2 comparison
save_plot(
    iterations, dynamic_memory2, recursive_memory2,
    "Memory with 40", "memory2_comparison.png",
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
    ['20', '40'],
    [avg_dynamic_value1, avg_dynamic_value2],
    [avg_recursive_value1, avg_recursive_value2],
    "Time Comparison: Dynamic vs Recursive",
    "time_comparison_bar.png",
    "Average Time (s)",
    ["Dynamic", "Recursive"]
)

# Memory comparison bar plot
save_bar_plot(
    ['20', '40'],
    [avg_dynamic_memory1, avg_dynamic_memory2],
    [avg_recursive_memory1, avg_recursive_memory2],
    "Memory Comparison: Dynamic vs Recursive",
    "memory_comparison_bar.png",
    "Average Memory (KB)",
    ["Dynamic", "Recursive"]
)