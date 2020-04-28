'''
    Single Linked List
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return

    def to_list(self):
        node = self.head
        output = []
        while node:
            output.append(node.value)
            node = node.next
        return output


