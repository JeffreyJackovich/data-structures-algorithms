from stack import Stack
from pytest import fixture

@fixture
def stack_obj():
    return Stack()

def test_push(stack_obj):
    stack_obj.push(5)

def test_pop(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.pop()
    assert len(stack_obj.array) == 1

def test_is_empty(stack_obj):
    stack_obj.push(2)
    assert not stack_obj.is_empty()

def test_pop_empty_array(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.pop()
    stack_obj.pop()
    result = stack_obj.pop()
    assert result == None
