import time
import os
from matplotlib import pyplot as plt
import tracemalloc

from dynamic_prog import calculate_minimum_change
from recursive_prog import calculate_recursive_minimum

def print_timers(timers: dict) -> None:
    for name, values in timers.items():
        if not values:  # Skip empty lists
            continue
        

        print(f"{name}")
        for value in values:
            print(f"{value:.6f}")

        # average = sum(values) / len(values)
        # minimum = min(values)
        # maximum = max(values)
        
        # print(f"\n{name}:")
        # print(f"Average: {average:.6f}")
        # print(f"Minimum: {minimum:.6f}")
        # print(f"Maximum: {maximum:.6f}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    
    file_path = os.path.join(base_dir, "sets", "sets.txt")
    
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
    
    names = ["value 1", "value 2"]
    memory_names = ["memory 1", "memory 2"]

    recursive_times = {name: [] for name in names + memory_names}
    dynamic_times = {name: [] for name in names + memory_names}

    # Saving the timers and peak memory for each function in each iteration
    for i, change in enumerate(change_values):
        for j in range(10):
            tracemalloc.start()
            _, time_dy = calculate_minimum_change(change)
            _, peak_dynamic = tracemalloc.get_traced_memory()
            dynamic_times[names[i]].append(time_dy)
            dynamic_times[memory_names[i]].append(peak_dynamic / 1024)  # Convert to KB
            tracemalloc.reset_peak()
            
            tracemalloc.start()
            _, time_rec = calculate_recursive_minimum(change)
            _, peak_recursive = tracemalloc.get_traced_memory()
            recursive_times[names[i]].append(time_rec)
            recursive_times[memory_names[i]].append(peak_recursive / 1024)  # Convert to KB
            tracemalloc.reset_peak()
    
    print_timers(dynamic_times)
    print_timers(recursive_times)