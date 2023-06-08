"""_summary_
    the prepend method for a LinkedList
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
    
    def prepend(self, value) -> bool:
        # add a value to beginning of list
        new_node = Node(value)
        # if self.length == 0, self.head = new_node, self.tail = new_node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # reset head and the rest will be correct values
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
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


# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.print_list()
# my_linked_list.prepend(0)
# my_linked_list.print_list()
my_linked_list = LinkedList(1)
print(f"popped: {my_linked_list.pop()}")
my_linked_list.print_list()
my_linked_list.prepend(0)
my_linked_list.print_list()
print(f"head: {my_linked_list.head.value}")
print(f"tail: {my_linked_list.tail.value}")