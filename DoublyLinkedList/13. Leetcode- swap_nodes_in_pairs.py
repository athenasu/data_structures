class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
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
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return
        # need to keep track of the first one, since it'll be the second and will need to be connected to the next set
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while(self.head and self.head.next):
            first_node = self.head
            second_node = self.head.next
            # head changes to second node
            prev.next = second_node
            # first node will be second, so its next will be the second node's next
            first_node.next = second_node.next
            # completing swap so the second node.next will point to the first node
            second_node.next = first_node

            # set prev nodes
            # second node will point to the head node
            second_node.prev = prev
            # switching first and second nodes
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node
            
            # move the head pointer to where you want to start next
            self.head = first_node.next
            prev = first_node
        self.head = dummy.next


my_dll = DoublyLinkedList(0)
my_dll.append(1)
my_dll.append(2)
my_dll.append(3)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1
    2
    3
    4
    my_dll after swap_pairs:
    2
    1
    4
    3

"""