from pytest import fixture
from queue_as_stack import Stack
from queue_as_stack import Queue



@fixture
def stack():
    return Stack()

@fixture
def queue():
    return Queue()

def test_pop(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    result = stack.pop()
    assert result == 3


def test_size(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2