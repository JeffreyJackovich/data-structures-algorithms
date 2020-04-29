'''
TODO: Implement a queue using a linked list.
        dequeue at the head and enqueue at the tail.

        example:
        HEAD [5]->[3]->[2]->None TAIL
'''
class Node:

    def __init__(self, value):
        self.next = None
        self.value = value


class QueueLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        '''Inserts value at the tail'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1
        return

    def dequeue(self):
        '''returns value at the head and resets head to the next element'''
        if self.head is None: # no elements
            return None
        else:
            temp_node = self.head.value
            self.head = self.head.next

        self.num_elements -= 1
        return temp_node

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0