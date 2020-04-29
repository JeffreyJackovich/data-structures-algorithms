from pytest import fixture

from queue_as_linked_list import QueueLinkedList

@fixture
def queue_ll_obj():
    return QueueLinkedList()

def test_enqueue(queue_ll_obj):
    queue_ll_obj.enqueue(5)
    queue_ll_obj.enqueue(3)
    queue_ll_obj.enqueue(2)
    assert queue_ll_obj.head.value == 5
    assert queue_ll_obj.tail.value == 2

def test_dequeue(queue_ll_obj):
    queue_ll_obj.enqueue(5)
    queue_ll_obj.enqueue(3)
    queue_ll_obj.enqueue(2)
    result = queue_ll_obj.dequeue()
    assert result == 5