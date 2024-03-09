# Node class for the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def remove(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.value = min_value(root.right)
        root.right = remove(root.right, root.value)
    return root

def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

def search(root, value):
    if root is None or root.value == value:
        return root is not None
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)
    
# In-order traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)
        
# Pre-order traversal
def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)
        
# Post-order traversal
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

def build_bst():
    root = None
    values = input("Enter 5 to 10 values (1-10) separated by spaces: ").split()
    values = [int(value) for value in values if 1 <= int(value) <= 10]
    if 5 <= len(values) <= 10:
        for value in values:
            root = insert(root, value)
    return root

# Main function
def main():
    root = build_bst()
    if root is None:
        return

    while True:
        print("\nChoose an operation:")
        print("1. Insert a value")
        print("2. Remove a value")
        print("3. Search for a value")
        print("4. In-order traversal")
        print("5. Pre-order traversal")
        print("6. Post-order traversal")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter a value to insert: "))
            if 1 <= value <= 10:
                root = insert(root, value)
            else:
                print("Please enter a value between 1 and 10.")
        elif choice == 2:
            value = int(input("Enter a value to remove: "))
            root = remove(root, value)
        elif choice == 3:
            value = int(input("Enter a value to search: "))
            if search(root, value):
                print(f"The value {value} is present.")
            else:
                print(f"The value {value} is not present.")
        elif choice == 4:
            print("In-order traversal:")
            inorder_traversal(root)
        elif choice == 5:
            print("Pre-order traversal:")
            preorder_traversal(root)
        elif choice == 6:
            print("Post-order traversal:")
            postorder_traversal(root)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()