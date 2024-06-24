import time

# Array (using Python list) implementation
class Array:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def insert(self, index, item):
        self.items.insert(index, item)

    def remove(self, item):
        self.items.remove(item)

    def get(self, index):
        return self.items[index]

    def size(self):
        return len(self.items)

# Linked List implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def get(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        return current.data

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Time complexity comparison
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# Test array operations
array = Array()
print("Array Operations:")
print("Append time:", measure_time(array.append, 1))
print("Insert time:", measure_time(array.insert, 0, 2))
print("Get time:", measure_time(array.get, 0))
print("Remove time:", measure_time(array.remove, 2))
print("Size:", array.size())

# Test linked list operations
linked_list = LinkedList()
print("\nLinked List Operations:")
print("Append time:", measure_time(linked_list.append, 1))
print("Insert time:", measure_time(linked_list.insert, 0, 2))
print("Get time:", measure_time(linked_list.get, 0))
print("Remove time:", measure_time(linked_list.remove, 2))
print("Size:", linked_list.size())

# Demonstrate array vs linked list for large number of insertions at the beginning
n = 10000
array_time = measure_time(lambda: [array.insert(0, i) for i in range(n)])
linked_list_time = measure_time(lambda: [linked_list.insert(0, i) for i in range(n)])

print(f"\nTime to insert {n} elements at the beginning:")
print(f"Array: {array_time:.6f} seconds")
print(f"Linked List: {linked_list_time:.6f} seconds")