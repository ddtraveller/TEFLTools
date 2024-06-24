import time
import matplotlib.pyplot as plt

def constant_time(n):
    return 1

def linear_time(n):
    total = 0
    for i in range(n):
        total += i
    return total

def quadratic_time(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

def measure_time(func, n):
    start = time.time()
    func(n)
    end = time.time()
    return end - start

# Measure execution times for different input sizes
input_sizes = range(10, 1001, 10)
constant_times = []
linear_times = []
quadratic_times = []

for n in input_sizes:
    constant_times.append(measure_time(constant_time, n))
    linear_times.append(measure_time(linear_time, n))
    quadratic_times.append(measure_time(quadratic_time, n))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, constant_times, label='O(1) - Constant')
plt.plot(input_sizes, linear_times, label='O(n) - Linear')
plt.plot(input_sizes, quadratic_times, label='O(n^2) - Quadratic')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity Comparison')
plt.legend()
plt.show()

print("Big O Notation Examples:")
print("O(1) - Constant Time: Accessing an array element by index")
print("O(n) - Linear Time: Finding the maximum element in an unsorted array")
print("O(n^2) - Quadratic Time: Bubble sort algorithm")
print("O(log n) - Logarithmic Time: Binary search in a sorted array")
print("O(n log n) - Linearithmic Time: Efficient sorting algorithms like Merge Sort")