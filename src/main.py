import time
import os
from matplotlib import pyplot as plt

from dynamic_prog import calculate_minimum_change
from recursive_prog import measure_recursive_execution

def compare_algorithms(change_values):
    dynamic_times = []
    recursive_times = []
    
    for value in change_values:
        _, dynamic_time = calculate_minimum_change(value)
        dynamic_times.append(dynamic_time)
        
        _, recursive_time = measure_recursive_execution(value)
        recursive_times.append(recursive_time)
    
    return dynamic_times, recursive_times

def plot_individual(data, change_values, title, filename, color, label):
    plt.figure()
    plt.plot(change_values, data, marker='o', color=color, label=label)
    plt.title(title)
    plt.xlabel("Change Value (cents)")
    plt.ylabel("Execution Time (s)")
    plt.grid(True)
    plt.legend()
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    
    file_path = os.path.join(base_dir, "sets", "sets.txt")
    dynamic_image_path = os.path.join(base_dir, "results", "dynamic_execution_time.png")
    recursive_image_path = os.path.join(base_dir, "results", "recursive_execution_time.png")
    comparison_image_path = os.path.join(base_dir, "results", "comparison_execution_time.png")
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    
    change_values = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                value = int(line.strip())
                change_values.append(value)
    except ValueError:
        print("Error: File 'sets.txt' contains invalid values.")
        exit(1)
    
    dynamic_times, recursive_times = compare_algorithms(change_values)
    
    plot_individual(
        dynamic_times, 
        change_values, 
        "Time with Dynamic Programming", 
        dynamic_image_path, 
        'blue', 
        'Dynamic Programming'
    )
    plot_individual(
        recursive_times, 
        change_values, 
        "Time with Recursive Algorithm", 
        recursive_image_path, 
        'red', 
        'Recursive'
    )
    
    plt.figure()
    plt.plot(change_values, dynamic_times, marker='o', label='Dynamic Programming', color='blue')
    plt.plot(change_values, recursive_times, marker='o', label='Recursive', color='red')
    plt.title("Execution Time Comparison: Dynamic vs Recursive")
    plt.xlabel("Change Value (cents)")
    plt.ylabel("Execution Time (s)")
    plt.grid(True)
    plt.legend()
    plt.savefig(comparison_image_path, bbox_inches='tight')
    plt.close()
    