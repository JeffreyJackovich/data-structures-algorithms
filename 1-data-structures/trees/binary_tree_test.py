from binary_tree import Node
from binary_tree import Tree
from pytest import fixture

@fixture
def node():
    return Node()

@fixture
def tree():
    return Tree()


def test_node(node):
    node1 = node
    node1.set_value("apple")


def test_set_left_child(node):
    node0 = Node("apple")
    node1 = Node("orange")
    node2 = Node("pear")
    node0.set_left_child(node1)
    node0.set_left_child(node2)
    assert node0.has_left_child()

