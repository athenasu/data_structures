class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
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

    def kth_smallest(self, k):
        """
            Find the kth smallest number
            Steps:
                1. Create a stack to store nodes in the tree, starting from the root
                2. Add the ones on the left to the stack first
                3. Pop items from the stack and decrement k by 1
                4. Check if k == 0, if not, then we move to the right of the node and find the left
        """
        pass
            




bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(10)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(18)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 10


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    10

 """

 # Solution
#  stack = []
# current_node = self.root
# while current_node or stack:
#     while current_node:
#         stack.append(current_node)
#         current_node = current_node.left
        
#     current_node = stack.pop()
#     k -= 1
#     if k == 0:
#         return current_node.value
#     current_node = current_node.right