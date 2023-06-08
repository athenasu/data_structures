"""
Create a Doubly LinkedList class and constructor
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


my_doubly_linkedlist = DoublyLinkedList(7)

my_doubly_linkedlist.print_list()