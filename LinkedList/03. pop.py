"""_summary_
    the pop method for a LinkedList
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    

    def pop(self):
        if self.length == 0:
            return None
        # find the pointer pointing to the last item (second to last item)
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        # change second to last item to tail
        self.tail = pre
        # remove last item on list
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
my_linked_list.pop()
