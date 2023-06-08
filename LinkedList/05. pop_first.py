"""_summary_
    the pop first method for a LinkedList (pop first value of the LinkedList)
"""

from typing import Union


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
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
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

    def pop_first(self):
        # if head and tail point to None, then return None
        if self.length == 0:
            return None
        # temp to store self.head & set new head value
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            # we only need to set tail here because self.head on line 65 could already be None
            self.tail = None
        return temp

    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.prepend(0)
my_linked_list.print_list()
my_linked_list.pop_first()
my_linked_list.print_list()
# my_linked_list = LinkedList(1)
# print(f"popped first item: {my_linked_list.pop_first()}")
# my_linked_list.print_list()
# my_linked_list.pop_first()
# my_linked_list.print_list()
# print(f"head: {my_linked_list.head.value}")
# print(f"tail: {my_linked_list.tail.value}")