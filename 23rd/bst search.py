class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

r = None

r = insert(r, 7)
r = insert(r, 35)
r = insert(r, -4)
r = insert(r, -9)
r = insert(r, 8)
r = insert(r, 62)
r = insert(r, -25)
r = insert(r, 25)
r = insert(r, 16)
r = insert(r, 17)
r = insert(r, 77)
r = insert(r, -39)
r = insert(r, 100)


print("Inorder traversal:")
inorder(r)
print()

key = 16
result = search(r, key)

if result:
    print(f"Node with value {key} found in the BST.")
else:
    print(f"Node with value {key} not found in the BST.")

