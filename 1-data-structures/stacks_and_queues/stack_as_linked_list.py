'''
    Single Linked List:
        Node

    Stack:
        push()
'''

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        '''returns head at top-of-stack and tail at bottom-of-stack'''
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out