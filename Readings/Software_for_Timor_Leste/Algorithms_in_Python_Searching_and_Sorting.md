# Introduction

Searching and sorting are fundamental operations in computer science. These algorithms form the basis of many complex operations and are essential for efficient data manipulation and retrieval. 

## Vocabulary

- **Algorithm**: A sequence of well-defined instructions to solve a particular problem.
- **Data Structure**: A way of organizing and storing data for efficient access and modification.
- **Time Complexity**: A measure of how the running time of an algorithm increases with the size of the input data.
- **Space Complexity**: A measure of how the memory usage of an algorithm increases with the size of the input data.
- **Brute Force**: A straightforward approach to solving a problem, usually by trying all possible solutions. 
- **Divide and Conquer**: A strategy of recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.
- **In-place**: An algorithm is said to be in-place if it does not need an extra space and produces an output in the same memory that contains the data by transforming the input 'in-place'. 
- **Stable**: A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.
- **Deterministic**: An algorithm that, given a particular input, will always produce the same output, with the underlying machine always passing through the same sequence of states.
- **Non-Deterministic**: An algorithm that, given a particular input, could exhibit different behaviors on different runs due to randomness or other factors.

## Searching Algorithms

Searching algorithms are designed to check for an element or retrieve an element from any data structure where it is stored.

### Linear Search 

Linear search is the simplest searching algorithm that sequentially checks each element in the list until a match is found or the whole list has been searched.

```python
def linear_search(arr, x):
    """
    Performs a linear search on an array.
    
    :param arr: The array to search
    :param x: The value to search for
    :return: The index of the first occurrence of x in arr, or -1 if x is not found
    """
    for i in range(len(arr)):
        if arr[i] == x:  
            return i   # Return the index if x is found
    return -1   # Return -1 if x is not found
```

- **Time Complexity**: O(n) - where n is the number of elements
  - Best case: O(1) if the target element is found at the first position
  - Worst case: O(n) if the target element is at the last position or not present at all
  - Average case: O(n)
- **Space Complexity**: O(1) - only a few variables are used, regardless of the size of the input
- **Use Case**: Suitable for small lists or unsorted data

#### Example

Suppose you have an array of numbers `[5, 2, 4, 6, 1, 3]` and you want to search for the number 4.

With linear search:
1. Compare 4 with the first element, 5. Not equal, so move to the next element.  
2. Compare 4 with 2. Not equal, move to the next.
3. Compare 4 with the third element, 4. Equal, so return the index 2.

The linear search function will return 2, indicating that 4 is at index 2 in the array.

If the target was 7, the linear search would compare with every element and, not finding a match, would return -1 to indicate that 7 is not in the array.

### Binary Search

Binary search is an efficient algorithm for searching a sorted array by repeatedly dividing the search interval in half. 

```python
def binary_search(arr, x):
    """
    Performs a binary search on a sorted array.
    
    :param arr: The sorted array to search
    :param x: The value to search for
    :return: The index of x in arr if found, or -1 if x is not found
    """
    low = 0  
    high = len(arr) - 1
    mid = 0

    while low <= high: 
        mid = (high + low) // 2

        # If x is greater, ignore left half  
        if arr[mid] < x: 
            low = mid + 1

        # If x is smaller, ignore right half 
        elif arr[mid] > x: 
            high = mid - 1

        # x is present at mid 
        else: 
            return mid

    # If we reach here, then the element was not present 
    return -1
```

- **Time Complexity**: O(log n)
  - Best case: O(1) if the target element is at the middle of the array
  - Worst case: O(log n) 
  - Average case: O(log n)
- **Space Complexity**: O(1) 
- **Use Case**: Ideal for large, sorted datasets
- **Requirement**: The list must be sorted

#### Example

Let's look at how binary search works with the same array as before, but this time sorted: `[1, 2, 3, 4, 5, 6]`. We're again searching for the number 4.

1. The search begins with the middle element, 3. Since 4 is greater than 3, we can ignore the entire lower half of the array. 
2. The middle of the upper half is 5. Since 4 is less than 5, we can ignore the upper quarter.
3. The middle of the remaining portion is 4, which is our target. The function returns the index 3.

If the target was 0, the process would continue until `low` becomes greater than `high`. At this point, the function would return -1, indicating that 0 is not in the array.

Binary search is much more efficient than linear search for large, sorted arrays. While linear search would compare the target with every single element, binary search discards half of the remaining elements at each step, drastically reducing the number of comparisons needed.

## Sorting Algorithms

Sorting algorithms arrange elements in a list in a specific order, typically ascending or descending.

### Bubble Sort

Bubble sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

```python
def bubble_sort(arr):
    """
    Sorts an array using bubble sort.
    
    :param arr: The array to be sorted
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

- **Time Complexity**: O(n^2) 
  - Best case: O(n) when the array is already sorted
  - Worst case: O(n^2)
  - Average case: O(n^2)
- **Space Complexity**: O(1)
- **Stable**: Yes
- **Use Case**: Educational purposes, very small datasets

#### Example

Let's sort the array `[64, 34, 25, 12, 22, 11, 90]` using bubble sort.

First Pass:
- `[64, 34, 25, 12, 22, 11, 90]` -> `[34, 64, 25, 12, 22, 11, 90]`, swaps 64 and 34
- `[34, 64, 25, 12, 22, 11, 90]` -> `[34, 25, 64, 12, 22, 11, 90]`, swaps 64 and 25
- `[34, 25, 64, 12, 22, 11, 90]` -> `[34, 25, 12, 64, 22, 11, 90]`, swaps 64 and 12
- `[34, 25, 12, 64, 22, 11, 90]` -> `[34, 25, 12, 22, 64, 11, 90]`, swaps 64 and 22
- `[34, 25, 12, 22, 64, 11, 90]` -> `[34, 25, 12, 22, 11, 64, 90]`, swaps 64 and 11
- No swap for 90 as it's already the largest element.

The largest element, 90, has bubbled to the right. The array is not fully sorted yet, so we move to the next pass.

Second Pass:
- `[34, 25, 12, 22, 11, 64, 90]` -> `[25, 34, 12, 22, 11, 64, 90]`, swaps 34 and 25
- `[25, 34, 12, 22, 11, 64, 90]` -> `[25, 12, 34, 22, 11, 64, 90]`, swaps 34 and 12
- `[25, 12, 34, 22, 11, 64, 90]` -> `[25, 12, 22, 34, 11, 64, 90]`, swaps 34 and 22
- `[25, 12, 22, 34, 11, 64, 90]` -> `[25, 12, 22, 11, 34, 64, 90]`, swaps 34 and 11
- No swaps for 64 and 90.

Now, the two largest elements (64 and 90) are in their final positions. The process continues until no more swaps are needed.

After the final (sixth) pass, the array is fully sorted:
`[11, 12, 22, 25, 34, 64, 90]`

While bubble sort is easy to understand and implement, it's highly inefficient and impractical for large datasets due to its quadratic time complexity. 

### Insertion Sort

Insertion sort is another simple comparison-based sorting algorithm that builds the final sorted array one element at a time. It's much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

```python
def insertion_sort(arr):
    """
    Sorts an array using insertion sort.
    
    :param arr: The array to be sorted
    """
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
```

- **Time Complexity**: O(n^2)
  - Best case: O(n) when the array is already sorted
  - Worst case: O(n^2) 
  - Average case: O(n^2)
- **Space Complexity**: O(1)
- **Stable**: Yes
- **Use Case**: Small datasets, partially sorted arrays

#### Example

Let's sort the same array `[64, 34, 25, 12, 22, 11, 90]` using insertion sort.

We start from the second element and compare it with the element(s) before it. If the element before it is larger, we swap them.

First Pass:
- `[64, 34, 25, 12, 22, 11, 90]`, 34 is less than 64, so it's swapped.
- Result: `[34, 64, 25, 12, 22, 11, 90]`

Second Pass:
- `[34, 64, 25, 12, 22, 11, 90]`, 25 is less than 64, so it's swapped.
- `[34, 25, 64, 12, 22, 11, 90]`, 25 is less than 34, so it's swapped again.
- Result: `[25, 34, 64, 12, 22, 11, 90]`

Third Pass:
- `[25, 34, 64, 12, 22, 11, 90]`, 12 is less than 64, 34, and 25, so it's swapped until it's at the beginning.
- Result: `[12, 25, 34, 64, 22, 11, 90]`

The process continues until the array is fully sorted after the sixth pass:
`[11, 12, 22, 25, 34, 64, 90]`

At each step, insertion sort takes an element from the input data and inserts it into its correct position in the sorted part of the array. This is more efficient than bubble sort if the input is already partially sorted, as it doesn't need to go through the entire array for each element.

### Selection Sort

Selection sort is an in-place comparison-based sorting algorithm that divides the input list into two parts: a sorted portion at the left end and an unsorted portion at the right end. Initially, the sorted portion is empty and the unsorted portion is the entire input list.

```python
def selection_sort(arr):
    """
    Sorts an array using selection sort.
    
    :param arr: The array to be sorted
    """
    
    # Traverse through all array elements 
    for i in range(len(arr)):
        
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

- **Time Complexity**: O(n^2)
  - Best case: O(n^2) 
  - Worst case: O(n^2)
  - Average case: O(n^2) 
- **Space Complexity**: O(1)
- **Stable**: No (can be made stable with additional space)
- **Use Case**: Small datasets, situations where memory writes are expensive

#### Example

Once again, let's sort the array `[64, 34, 25, 12, 22, 11, 90]` using selection sort.

First Pass:
- The minimum element is 11. Swap it with the first element.
- Result: `[11, 34, 25, 12, 22, 64, 90]`

Second Pass:
- The minimum element in the remaining unsorted array is 12. Swap it with the second element.
- Result: `[11, 12, 25, 34, 22, 64, 90]`

Third Pass:
- The minimum element in the remaining unsorted array is 22. Swap it with the third element.
- Result: `[11, 12, 22, 34, 25, 64, 90]`

The process continues until the array is fully sorted after the sixth pass:
`[11, 12, 22, 25, 34, 64, 90]`

At each step, selection sort selects the minimum element from the unsorted part of the array and swaps it with the leftmost unsorted element, gradually building the sorted portion from left to right.

While selection sort improves on bubble sort by making fewer swaps (which could be expensive if elements are large structures), it's still not very efficient due to its quadratic time complexity.

### Merge Sort

Merge sort is a divide-and-conquer algorithm that splits the unsorted list into n sublists, each containing one element (a list of one element is considered sorted), then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining, which is the sorted list.

```python
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        
        # Dividing the array elements into left and right halves
        L = arr[:mid]
        R = arr[mid:]
        
        # Sorting the first half
        merge_sort(L)
        
        # Sorting the second half
        merge_sort(R)
        
        i = j = k = 0
        
        # Copying data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
arr[k] = L[i]
i += 1
else:
arr[k] = R[j]
j += 1
k += 1
Copy    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
Copy
- **Time Complexity**: O(n log n) in all cases
  - Best case: O(n log n)
  - Worst case: O(n log n) 
  - Average case: O(n log n)
- **Space Complexity**: O(n) 
- **Stable**: Yes
- **Use Case**: When stability is required, for linked lists, for external sorting

#### Example

Let's sort the array `[64, 34, 25, 12, 22, 11, 90]` using merge sort.

First, we divide the array into two halves:
- Left half: `[64, 34, 25, 12]`
- Right half: `[22, 11, 90]`

We recursively sort the left half:
- Divide `[64, 34, 25, 12]` into `[64, 34]` and `[25, 12]`
- Recursively sort `[64, 34]` and `[25, 12]`
- Merge the sorted halves: `[25, 12]` and `[34, 64]` to get `[12, 25, 34, 64]`

Similarly, we recursively sort the right half:
- Divide `[22, 11, 90]` into `[22]` and `[11, 90]`
- Recursively sort `[11, 90]` 
- Merge the sorted halves: `[11, 90]` and `[22]` to get `[11, 22, 90]`

Finally, we merge the sorted left and right halves:
- Merge `[12, 25, 34, 64]` and `[11, 22, 90]`
- Final sorted array: `[11, 12, 22, 25, 34, 64, 90]`

Merge sort always divides the array into two halves and takes linear time to merge two halves. It is one of the most efficient general-purpose sorting algorithms, especially for larger datasets, due to its guaranteed O(n log n) time complexity. However, it does require O(n) additional space for the temporary arrays.

### Quick Sort

Quick sort is a divide-and-conquer algorithm that selects a 'pivot' element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

```python
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

Time Complexity:

Best case: O(n log n) when the partition always picks the middle element as pivot
Worst case: O(n^2) when the partition always picks greatest or smallest element as pivot
Average case: O(n log n)


Space Complexity: O(log n) due to recursion
Stable: No
Use Case: When average expected time is crucial, as it is the fastest in practice

Example
Let's sort the array [64, 34, 25, 12, 22, 11, 90] using quick sort.
First, we select a pivot element. Let's choose the last element, 90.
We partition the array into two sub-arrays based on the pivot:

Elements less than 90: [64, 34, 25, 12, 22, 11]
Elements greater than 90: []

Now, we recursively sort the sub-array [64, 34, 25, 12, 22, 11].
We select 11 as the pivot and partition:

Elements less than 11: []
Elements greater than 11: [64, 34, 25, 12, 22]

We recursively sort [64, 34, 25, 12, 22], selecting 22 as the pivot:

Elements less than 22: [12]
Elements greater than 22: [64, 34, 25]

We keep recursively sorting until we have sub-arrays of size 1, which are by definition sorted.
Finally, we combine the sorted sub-arrays:
[11, 12, 22, 25, 34, 64, 90]
Quick sort is often faster in practice than other O(n log n) algorithms, because its inner loop can be efficiently implemented on most architectures. However, its worst-case time complexity of O(n^2) makes it susceptible to adversarial inputs, and it is not a stable sort.
Comparison of Algorithms
Searching Algorithms
Linear Search vs. Binary Search:

Linear search is simpler but less efficient for large datasets.
Binary search is much faster for large datasets but requires the data to be sorted.

Sorting Algorithms
Bubble Sort vs. Insertion Sort vs. Selection Sort:

All have O(n^2) time complexity, making them inefficient for large datasets.
Insertion sort generally performs better than bubble sort and is adaptive (efficient for nearly sorted data).
Selection sort makes the least number of swaps and can be preferable when memory write is costly.

More Efficient Sorting Algorithms (not implemented in the script but worth mentioning):

Merge Sort: O(n log n) time complexity, stable, but requires O(n) extra space.
Quick Sort: O(n log n) average case time complexity, in-place, but unstable and has O(n^2) worst case.
Heap Sort: O(n log n) time complexity, in-place, but unstable.

Real-World Applications
Searching:

Database queries
Find functions in text editors
Locating items in e-commerce platforms

Sorting:

Organizing data in spreadsheets
Arranging items in e-commerce (by price, rating, etc.)
Optimizing database indexing

Big O Notation
Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. In computer science, it is used to classify algorithms according to how their runtime or space requirements grow as the input size grows.
Here are some common time complexities and their notations:

O(1) (constant time): The running time of the algorithm is constant, regardless of the size of the input data. Example: accessing an array element by its index.
O(log n) (logarithmic time): The running time of the algorithm grows logarithmically with the size of the input data. Example: binary search.
O(n) (linear time): The running time of the algorithm grows linearly with the size of the input data. Example: linear search, traversing an array.
O(n log n) (quasilinear time): The running time of the algorithm is a combination of linear and logarithmic. Many efficient sorting algorithms like Merge sort and Quick sort have an average time complexity of O(n log n).
O(n^2) (quadratic time): The running time of the algorithm is proportional to the square of the size of the input data. Example: simple sorting algorithms like bubble sort, insertion sort, and selection sort.
O(2^n) (exponential time): The running time of the algorithm doubles for every additional element in the input data. Example: recursive calculation of Fibonacci numbers.
O(n!) (factorial time): The running time of the algorithm multiplies by an additional factor for every element. Example: generating all permutations of a list.

c is some fixed constant that depends on the implementation details, hardware, etc., but doesn't change with the size of the input.
Big O notation provides an upper bound on the growth rate of a function and is used to describe the worst-case scenario. For example, the worst-case time complexity of Quick Sort is O(n^2), but its average-case complexity is O(n log n).
Understanding these notations helps in analyzing the performance of algorithms and choosing the most efficient one for a given problem and input size. In most cases, we aim for algorithms with time complexities of O(n log n) or better.
Conclusion
Understanding searching and sorting algorithms is crucial for any computer scientist or software developer. While simple algorithms like linear search and bubble sort are easy to understand and implement, they become inefficient for large datasets. More advanced algorithms like binary search for searching and merge sort and quick sort for sorting offer significant performance improvements for larger scales of data.
The choice of algorithm depends on various factors including the size of the dataset, whether the data is sorted, memory constraints, and the specific requirements of the application. As you continue to develop your skills, exploring more advanced algorithms and understanding their trade-offs will be key to writing efficient and scalable software.
Remember, the goal is not just to implement these algorithms, but to understand when and why to use each one. This knowledge forms the foundation for solving complex computational problems and optimizing software performance. With practice and experience, you'll develop the intuition to choose the right algorithm for each situation.
As you progress in your computer science journey, keep learning about new algorithms and data structures. Challenge yourself to understand their inner workings and analyze their time and space complexities. Implement them, experiment with them, and see how they perform in real-world scenarios.
The field of algorithms is vast and ever-evolving, with new techniques being developed all the time to solve increasingly complex problems. By mastering the fundamentals and staying curious, you'll be well-equipped to tackle whatever challenges come your way. Happy coding!