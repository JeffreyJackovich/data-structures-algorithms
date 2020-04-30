'''
    Single Linked List
'''

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "Node obj: value={}".format(self.value)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "SLL obj: head={}".format(self.head)

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return

    def is_empty(self):
        '''return True if empty, else False'''
        if self.head is None:
            return True
        else:
            return False

    def prepend(self, value):
        ''' Prepend a value to the beginning of the Linked List'''
        new_node = Node(value)
        if self.is_empty():
            return None
        else:
            self.head.next = new_node
            self.head = new_node
        return


    def size(self):
        return len(self.to_list())

    def search(self, value):
        pass

    def remove(self, value):
        ''' Removes the first node that has the value'''
        pass

    def to_list(self):
        node = self.head
        output = []
        while node:
            output.append(node.value)
            node = node.next
        return output
