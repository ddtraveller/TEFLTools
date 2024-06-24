print("Welcome to the Introduction to Recursion and Trees!")

# Recursion Examples

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    print(f"Computing factorial({n})")
    if n == 0 or n == 1:
        print(f"Base case reached: factorial({n}) = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) = {n} * factorial({n-1}) = {result}")
        return result

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    print(f"Computing fibonacci({n})")
    if n <= 1:
        print(f"Base case reached: fibonacci({n}) = {n}")
        return n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"fibonacci({n}) = fibonacci({n-1}) + fibonacci({n-2}) = {result}")
        return result

# Binary Tree Implementation

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert(self, value):
        """Insert a value into the binary tree."""
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self):
        """Perform an inorder traversal of the tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Demonstrate recursion
print("\nDemonstrating Factorial Calculation:")
factorial(5)

print("\nDemonstrating Fibonacci Calculation:")
fibonacci(5)

# Demonstrate binary tree
print("\nDemonstrating Binary Tree:")
tree = BinaryTree(5)
for value in [3, 7, 2, 4, 6, 8]:
    tree.insert(value)

print("Inorder traversal of the binary tree:")
print(tree.inorder_traversal())

# Recursive problem-solving: Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, destination):
    """Solve the Tower of Hanoi problem recursively."""
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

print("\nSolving Tower of Hanoi with 3 disks:")
tower_of_hanoi(3, 'A', 'B', 'C')

print("\nThis concludes our introduction to recursion and trees!")