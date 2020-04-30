'''
    data structure:
        list()

    methods:
        push()
        pop()
        peak()
        is_empty()
        size()

'''
class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            self.array.pop()

    def size(self):
        return len(self.array)

    def is_empty(self):
        '''returns True if array is empty, else False'''
        return len(self.array) == 0
