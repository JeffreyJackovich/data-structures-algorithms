'''
    TODO: Implement a Queue with an array.
    Remove from the end of the list (pop()) and add (insert()) at the front of the list.
'''

class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, value):
        '''Adds a value to the 0th index of the list.

        Runtime O(n), linear time, since adding at 0th index
        forces all elements to shift to the right.'''
        self.array.insert(0, value)

    def dequeue(self):
        '''Removes and returns last element.
        Runtime O(1) or constant time.'''
        if self.array:
            return self.array.pop()
        else:
            return None

    def peek(self):
        '''Returns diplays the tail element
        Runtime O(1)'''
        if self.array:
            return self.array[-1]
        else:
            return None

    def is_empty(self):
        '''Returns True if empty.  False if not'''
        return len(self.array) == 0
