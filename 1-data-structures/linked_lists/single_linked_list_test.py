from pytest import fixture

from single_linked_list import LinkedList


@fixture
def linked_list_obj():
    return LinkedList()

def test_add(linked_list_obj):
    linked_list_obj.add(3)

def test_to_list(linked_list_obj):
    linked_list_obj.add(1)
    linked_list_obj.add(2)
    assert len(linked_list_obj.to_list()) == 2