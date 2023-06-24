class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    current = root
    stack = []
    done = False

    while not done:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            done = True

def postorder(root):
    if root is None:
        return

    stack1 = []
    stack2 = []

    stack1.append(root)

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        print(node.data, end=" ")

def preorder(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.data, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Example usage:
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print the tree using inorder traversal
print("Inorder traversal:")
inorder(root)
print()

# Print the tree using postorder traversal
print("Postorder traversal:")
postorder(root)
print()

# Print the tree using preorder traversal
print("Preorder traversal:")
preorder(root)
print()
