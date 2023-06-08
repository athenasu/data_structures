"""
    Insertion Sort with Linked List
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

    def insertion_sort(self):
        """
            Insert node into correct place
            Steps:
                1. If length < 2, return 
                2. Isolate first node
                3. Compare current node and the sorted list head, if it's smaller, insert infront of sorted list
                4. Else, loop through sorted list to find the correct position
                5. Reset head and tail
        """
        if self.length < 2:
            return
        
        sorted_head = self.head
        current = self.head.next
        sorted_head.next = None

        while current is not None:
            pointer = current
            current = current.next
            if pointer.value < sorted_head.value:
                pointer.next = sorted_head
                sorted_head = pointer
            else:
                temp = sorted_head
                while temp.next is not None and temp.next.value < pointer.value:
                    temp = temp.next
                pointer.next = temp.next
                temp.next = pointer

        self.head = sorted_head
        temp = sorted_head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
        





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

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

