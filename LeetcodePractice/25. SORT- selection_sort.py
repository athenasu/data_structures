"""
    Selection Sort using a Linked List
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def selection_sort(self):
        """
            sort list using Linked List
            Steps:
                1. If length is < 2, return
                2. Find the node that has the smallest value
                3. If the current node is not the smallest value node, swap
                4. Advance current node
        """
        if self.length < 2:
            return
        
        current = self.head
        # find smallest value
        while current.next is not None:
            smallest_node = current
            temp = current.next
            while temp is not None:
                if temp.value < smallest_node.value:
                    smallest_node = temp
                temp = temp.next
            if smallest_node != current:
                current.value, smallest_node.value = smallest_node.value, current.value
            current = current.next




my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

