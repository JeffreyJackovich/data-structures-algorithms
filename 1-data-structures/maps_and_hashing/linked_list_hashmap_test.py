from linked_list_hashmap import HashMap
from pytest import fixture

@fixture
def hash_map():
    return HashMap()

def test_get_hash_code(hash_map):
    result = hash_map.get_bucket_index("abcd")
    assert result == 5204554

def test_get(hash_map):
    pass