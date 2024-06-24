import time
import random
import matplotlib.pyplot as plt

print("Welcome to the Searching and Sorting Algorithms Tutorial!")

# Searching Algorithms

def linear_search(arr, target):
    """
    Linear Search: Sequentially check each element in the list.
    Time Complexity: O(n)
    """
    print(f"\nPerforming Linear Search for {target} in {arr}")
    for i in range(len(arr)):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == target:
            print(f"Target {target} found at index {i}")
            return i
    print(f"Target {target} not found in the list")
    return -1

def binary_search(arr, target):
    """
    Binary Search: Repeatedly divide the search interval in half.
    Time Complexity: O(log n)
    Requirement: The list must be sorted.
    """
    print(f"\nPerforming Binary Search for {target} in {arr}")
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Checking middle element at index {mid}: {arr[mid]}")
        if arr[mid] == target:
            print(f"Target {target} found at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} < {target}, searching right half")
            left = mid + 1
        else:
            print(f"{arr[mid]} > {target}, searching left half")
            right = mid - 1
    print(f"Target {target} not found in the list")
    return -1

# Sorting Algorithms

def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly swap adjacent elements if they are in the wrong order.
    Time Complexity: O(n^2)
    """
    print(f"\nPerforming Bubble Sort on {arr}")
    n = len(arr)
    for i in range(n):
        print(f"Pass {i+1}")
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"Swapped {arr[j+1]} and {arr[j]}: {arr}")
        if not swapped:
            print("No swaps needed, array is sorted")
            break
    return arr

def insertion_sort(arr):
    """
    Insertion Sort: Build the final sorted array one item at a time.
    Time Complexity: O(n^2)
    """
    print(f"\nPerforming Insertion Sort on {arr}")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"Inserting {key}")
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Shifted {arr[j+1]} right: {arr}")
        arr[j + 1] = key
        print(f"Inserted {key} at position {j+1}: {arr}")
    return arr

def selection_sort(arr):
    """
    Selection Sort: Repeatedly select the smallest element from the unsorted portion.
    Time Complexity: O(n^2)
    """
    print(f"\nPerforming Selection Sort on {arr}")
    for i in range(len(arr)):
        min_idx = i
        print(f"Pass {i+1}, finding minimum from index {i} to {len(arr)-1}")
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Swapped {arr[min_idx]} with {arr[i]}: {arr}")
    return arr

def measure_time(func, *args):
    """Measure the execution time of a function."""
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

print("\n--- Demonstrating Searching Algorithms ---")
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13

print("\nLinear Search:")
linear_search(arr, target)

print("\nBinary Search:")
binary_search(arr, target)

print("\n--- Demonstrating Sorting Algorithms ---")
unsorted = [64, 34, 25, 12, 22, 11, 90]

print("\nBubble Sort:")
bubble_sort(unsorted.copy())

print("\nInsertion Sort:")
insertion_sort(unsorted.copy())

print("\nSelection Sort:")
selection_sort(unsorted.copy())

print("\n--- Comparing Time Complexities ---")
print("Generating random arrays of increasing sizes and measuring sorting times...")

sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
bubble_times = []
insertion_times = []
selection_times = []

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    bubble_times.append(measure_time(bubble_sort, arr.copy()))
    insertion_times.append(measure_time(insertion_sort, arr.copy()))
    selection_times.append(measure_time(selection_sort, arr.copy()))

plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, label='Bubble Sort')
plt.plot(sizes, insertion_times, label='Insertion Sort')
plt.plot(sizes, selection_times, label='Selection Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Time Complexities')
plt.legend()
plt.show()

print("\nThe graph shows how the execution time of each sorting algorithm grows with input size.")
print("Notice how all algorithms show a roughly quadratic growth, confirming their O(n^2) time complexity.")

print("\n--- Comparing Searching Algorithms ---")
print("Generating a sorted array and performing multiple searches...")

sorted_arr = list(range(10000))
linear_times = []
binary_times = []

for _ in range(100):
    target = random.randint(0, 9999)
    linear_times.append(measure_time(linear_search, sorted_arr, target))
    binary_times.append(measure_time(binary_search, sorted_arr, target))

print("\nAverage Search Times:")
print(f"Linear Search: {sum(linear_times) / len(linear_times):.6f} seconds")
print(f"Binary Search: {sum(binary_times) / len(binary_times):.6f} seconds")

print("\nNotice how Binary Search is significantly faster than Linear Search for large sorted arrays.")
print("This demonstrates the O(log n) time complexity of Binary Search compared to the O(n) of Linear Search.")

print("\nThis concludes our tutorial on searching and sorting algorithms.")
print("Remember, understanding these fundamental algorithms is crucial for efficient data manipulation and problem-solving in computer science!")