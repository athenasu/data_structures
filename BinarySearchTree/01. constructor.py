"""
    Create a constructor for binary search tree
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        # we are not setting up the new node now as we did before
        # the root and other nodes will use the insert method
        self.root = None


my_tree = BinarySearchTree()

print(my_tree.root)