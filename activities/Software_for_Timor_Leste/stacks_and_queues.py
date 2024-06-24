class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def front(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Stack application: Balanced parentheses checker
def is_balanced(expression):
    stack = Stack()
    opening = "({["
    closing = ")}]"
    pairs = {")": "(", "}": "{", "]": "["}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()

# Queue application: Print queue simulation
import random

def print_queue_simulation(num_jobs, print_rate):
    queue = Queue()
    total_wait_time = 0
    
    for _ in range(num_jobs):
        queue.enqueue(random.randint(1, 20))  # Random number of pages
    
    time = 0
    while not queue.is_empty():
        job = queue.dequeue()
        wait_time = time
        time += job / print_rate
        total_wait_time += wait_time
        print(f"Job of {job} pages completed. Wait time: {wait_time:.2f} minutes")
    
    avg_wait_time = total_wait_time / num_jobs
    print(f"\nAverage wait time: {avg_wait_time:.2f} minutes")

# Demonstrate stack operations
print("Stack Demo:")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)
print("Pop:", stack.pop())
print("Peek:", stack.peek())
print("Size:", stack.size())

# Demonstrate queue operations
print("\nQueue Demo:")
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Queue:", queue.items)
print("Dequeue:", queue.dequeue())
print("Front:", queue.front())
print("Size:", queue.size())

# Demonstrate balanced parentheses checker
print("\nBalanced Parentheses Checker:")
expressions = ["((()))", "((())", "({[]})", "({[}])"]
for expr in expressions:
    print(f"{expr}: {'Balanced' if is_balanced(expr) else 'Not balanced'}")

# Demonstrate print queue simulation
print("\nPrint Queue Simulation:")
print_queue_simulation(num_jobs=5, print_rate=10)  # 10 pages per minute