'''
TODO: Create a HashMap with separate chaining implemented for collision handling
'''
class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:

    def __init__(self, initial_items=10):
        self.bucket_array = [None for _ in range(initial_items)]
        self.p = 37
        self.num_entries = 0

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is in the map, and update it's value
        while head is not None:
            if head.key == key:
                return
            head = head.next

        #key not found in chain --> create new entry and place it at the head
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None


    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        """returns a hash code for key input"""
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for a_char in key:
            hash_code += ord(a_char) * current_coefficient
            hash_code = hash_code % num_buckets             # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets

        return hash_code % num_buckets

    def size(self):
        return self.num_entries
