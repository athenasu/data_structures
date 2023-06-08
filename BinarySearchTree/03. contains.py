"""
    Create a contains method to search through the tree
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value) -> bool:
        # if root is none, return False-> we don't need this because temp will be None, and will return False
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            # if value == temp.value, return True
            if value == temp.value:
                return True
            # if value < temp.value, temp = temp.left
            if value < temp.value:
                temp = temp.left
            # else, temp = temp.right
            else:
                temp = temp.right
        return False

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)


print(my_tree.root.value) # 2
print(my_tree.root.left.value) # 1
print(my_tree.root.right.value) # 3

print(my_tree.contains(2)) # True
print(my_tree.contains(10)) # False