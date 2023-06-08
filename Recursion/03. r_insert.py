"""
    Write an insert method using recursion for a BinaryTree
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value) -> bool:
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
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def __r_insert(self, current_node, value):
        # once we get to the end of the tree and need to insert the new node,
        # we will hit a 'None' and that's when we need to add the new node and connect it to the tree
        if current_node == None:
            return Node(value)
        # find the right place to add the node
        # if the value of the new node is less than the current node's, 
        # then the current_node.left will = its next left node (will continuously connect them until we can add the new Node)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_insert(self, value) -> None:
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def r_contains(self, value) -> bool:
        return self.__r_contains(self.root, value)
    
               

my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)


print(f'Root: {my_tree.root.value}')
print(f'Root -> left: {my_tree.root.left.value}')
print(f'Root -> right: {my_tree.root.right.value}')
