class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)

def printPosorder(root):
    if root:
        printPosorder(root.left)
        printPosorder(root.right)
        print(root.val, end=" ")

def printPreorder(root):
    if root:
        print(root.val, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

# Example usage:
# Create a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print the tree using inorder traversal
print("Inorder traversal:")
printInorder(root)
print()

# Print the tree using postorder traversal
print("Postorder traversal:")
printPosorder(root)
print()

# Print the tree using preorder traversal
print("Preorder traversal:")
printPreorder(root)
print()
