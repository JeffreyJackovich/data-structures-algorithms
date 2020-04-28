from pytest import fixture
from stack_as_linked_list import Stack

@fixture
def stack_ll_obj():
    return Stack()

def test_push(stack_ll_obj):
    stack_ll_obj.push(5)

def test_to_list(stack_ll_obj):
    stack_ll_obj.push(1)
    stack_ll_obj.push(2)
    stack_ll_obj.push(3)
    assert stack_ll_obj.to_list() == [3,2,1]
