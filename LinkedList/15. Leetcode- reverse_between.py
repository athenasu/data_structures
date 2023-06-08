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
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def reverse_between(self, start:int, end:int):
        ##### solution 2 #####
        # check if there is anything in the list
        if not self.head:
            return None
 
        # create a dummy node and connect it to the head. Create previous node to = dummy
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        # move prev to the node at one node before starting position.
        for _ in range(start):
            prev = prev.next
            
        # set current to the next node of prev.
        current = prev.next

        # Reverse the linked list from position m to n.
        for _ in range(end - start):
            after = current.next
            current.next = after.next
            after.next = prev.next
            prev.next = after
        # update the head of the linked list with the next node of the dummy.
        self.head = dummy.next
        ##### solution 1 #####
        """
        if self.length == 0:
            return None
            
        # get first and last node
        start_node = self.get(start)
        end_node = self.get(end)
        
        
        for _ in range(end-start):
            prev_end_node = self.get(end-1)
            
            # switch positions
            temp = start_node.value
            start_node.value = end_node.value
            end_node.value = temp
            
            # move one step closer to each other
            start_node = start_node.next
            end_node = prev_end_node
            end -= 1
            # repeat until they are next to each other or on the same node
            if start_node is end_node:
                return True
        """

    



linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(1)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
