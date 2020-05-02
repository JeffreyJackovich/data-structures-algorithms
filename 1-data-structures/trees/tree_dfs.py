'''
TODO:
1. Create a binary tree
2. Use a Stack to keep track of nodes.
3. Traverse via depth-first-search

Efficiency:
'''
class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "node={}".format(self.get_value())

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def get_left_child(self):
        return self.left

    def set_right_child(self, node):
        self.right = node

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

class Tree:

    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


class Stack:
    '''Define a stack to keep track of tree nodes'''
    def __init__(self):
        self.items = list()

    def __repr__(self):
        if len(self.items) > 0:
            s = "<top of stack>\n________\n"
            s += "\n__________\n".join([str(item) for item in self.items[::-1]])
            s += "\n__________\n<bottom of stack>"
            return s
        else:
            return "<stack is empty>"

    def push(self, value):
        return self.items.append(value)

    def pop(self):
        self.items.pop()

    def top(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

# s = Stack()
# s.push('apple')
# s.push('banana')
# s.push('orange')
# print("\n")
# print(s)
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
print(tree.root)