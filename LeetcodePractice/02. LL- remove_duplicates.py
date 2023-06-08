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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def remove_duplicates(self):
        """
        Remove all duplicate values from the list.
        should not create a new list, but rather modify the existing list in-place, 
        preserving the relative order of the nodes.
        """
        values = set()
        current = self.head
        previous = None

        while current and current.next:
            if current.value in values:
                # then remove node
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next
        



my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    4
    
"""