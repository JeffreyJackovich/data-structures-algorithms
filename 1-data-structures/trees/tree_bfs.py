from collections import deque #double ended queue
'''
TODO:
1. Create a binary tree
2. Use a Queue to keep track of nodes.
3. Traverse via breadth-first-search (*used later wih graph structures with shortest path).

Efficiency:
'''
class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node={}".format(self.get_value())

    def __str__(self):
        return "Node={}".format(self.get_value())

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

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


class Queue:

    def __init__(self):
        self.q = deque()

    def enq(self, value):
        '''inserts value'''
        self.q.appendleft(value)

    def deq(self):
        '''removes oldest value'''
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________\n"
            s += "\n____________\n".join([str(item) for item in self.q])
            s += "\n____________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

#
# q = Queue()
# q.enq("apple")
# q.enq("banana")
# q.enq("cherry")
# print(q)


visit_order = list()
#start at root
q = Queue()
node = tree.get_root()
q.enq(node)
visit_order.append(node)
# check left then right node
if node.has_left_child():
    q.enq(node.get_left_child())
    # visit_order.append(root)

if node.has_right_child():
    q.enq(node.get_right_child())

# print(q)