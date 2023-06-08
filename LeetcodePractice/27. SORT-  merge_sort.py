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

    def merge(self, other_list):
        """
            Merge two LinkedLists into one LinkedList, sorted
            Steps:
                1. Start at both lists' head, can use a pointer to connect the two lists
                2. Compare the two and connect
                3. Move pointer to the next position
                4. Add remaining parts of either list
                5. Reset head & reset tail if needed, add to original length of list
        """
        pointer = Node(0)
        dummy = pointer
        other = other_list.head
        current = self.head

        while other is not None and current is not None:
            if current.value < other.value:
                pointer.next = current
                current = current.next
            else:
                pointer.next = other
                other = other.next
            pointer = pointer.next
        
        if other is not None:
            pointer.next = other
        if current is not None:
            pointer.next = current
        
        self.head = dummy.next
        


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""