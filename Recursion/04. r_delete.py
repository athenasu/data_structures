"""
    Write a delete method using recursion for a BinaryTree
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
        if current_node == None:
            return Node(value)
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

    def __r_delete(self, current_node, value):
        # means we can't find the value in the tree
        if current_node == None:
            return None
        # same as the insert method, where we need to still connect the values
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        # if the current_node.value == value
        else:
            # if the node is a leaf (so nothing on the right or left),
            # then we can just return None (because the previous call asked for a connection)
            # and will remove the node
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            # else, if there are leaves or a sub tree on both sides
            else:
                # get the min value from the right side
                # (only the right because the min value on the right will be bigger than the original left
                # and will be smaller than the original right)
                sub_tree_min_value = self.min_value(current_node.right)
                # set the current node value to the min value
                current_node.value = sub_tree_min_value
                # delete the node with the sub_tree_min_value
                current_node.right = self.__r_delete(current_node.right, sub_tree_min_value)
        return current_node

    def r_insert(self, value) -> None:
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def r_contains(self, value) -> bool:
        return self.__r_contains(self.root, value)
    
    def r_delete(self, value) -> None:
        self.root = self.__r_delete(self.root, value)

    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value
               

my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)


print(f'Root: {my_tree.root.value}')
print(f'Root -> left: {my_tree.root.left.value}')
print(f'Root -> right: {my_tree.root.right.value}')


my_tree.r_delete(2)
print(f'Root: {my_tree.root.value}')
print(f'root.left: {my_tree.root.left.value}')
print(f'root.right: {my_tree.root.right}')
