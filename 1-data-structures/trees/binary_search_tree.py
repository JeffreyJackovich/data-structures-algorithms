from collections import deque
'''
TODO:
1. Create a binary search tree
2. Use a Queue to keep track of nodes.
3. Traverse via 


         5
(4<5) 4     6 (6>5)
   2 


Efficiency: log(n)
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


class Tree:

    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


    def __repr__(self):
        level = 0
        q = Queue
        visit_list = list()
        node = self.get_root()
        q.enq( (node, level))
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_list.append(("<empty>", level))
                continue
            visit_list.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))


    def compare(self, node, new_node):
        '''

        :param node:
        :param new_node:
        :return:
            1 if new_node > node
            -1 if new_node < node
            0 if new_node == node
        '''
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert_with_loop(self, new_value):
        #compare root to new_value
        #new_value > root
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return

        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                #override with new node's value
                node.set_value(new_node.get_value())
                break
            elif comparison == -1:
                #go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break # inserted node, so stop
            else: #comparison == 1
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break




tree = Tree()
tree.set_root(5)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(6)
print(tree)
