from queue import Queue
from pytest import fixture

@fixture
def queue_obj():
    return Queue()


def test_enqueue(queue_obj):
    queue_obj.enqueue(1)
    queue_obj.enqueue(2)
    queue_obj.enqueue(3)
    assert queue_obj.array == [3,2,1]

def test_dequque(queue_obj):
    queue_obj.enqueue(1)
    queue_obj.enqueue(2)
    queue_obj.enqueue(3)
    result = queue_obj.dequeue()
    assert queue_obj.array == [3, 2]
    assert result == 1

def test_peak(queue_obj):
    queue_obj.enqueue(1)
    queue_obj.enqueue(2)
    result = queue_obj.peek()
    assert result == 1, "Tail item not displayed"
    assert queue_obj.array == [2,1]

def test_is_empty(queue_obj):
    assert queue_obj.is_empty() == True


# def test_print(queue_obj):
