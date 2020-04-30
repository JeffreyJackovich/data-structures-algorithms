'''
TODO: Build a queue using a stack
'''

class Stack:
    '''LIFO'''
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        '''returns True if empty, else False'''
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)


class Queue:
    '''FIFO
    enqueue at the tail and dequeue from the head'''
    def __init__(self):
        self.in_storage = Stack()
        self.out_storage = Stack()

    def size(self):
        return self.in_storage.size() + self.out_storage.size()

    def enqueue(self, item):
        '''add item to the tail'''
        self.in_storage.push(item)

    def dequeue(self):
        '''remove item from the head'''
        if not self.out_storage.items:
            while self.in_storage.items:
                self.out_storage.push(self.in_storage.pop())
        return self.out_storage.pop()



