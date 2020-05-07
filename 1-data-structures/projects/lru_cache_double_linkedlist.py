'''
TODO: Code a Least Recently Used data structure with a dict and double linked list.
'''

class Node:

    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value

class LRU_Cache:

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key):
        '''Checks the cache for a key.
            If the cache:
                returns a key's value
                AND
                move the key to the front of the queue
            If not in cache, return -1

        Efficiency: O(1)'''
        if key in self.cache: # cache hit
            # set the key to the head via prepend()
            # move accesed
            if self.head is None:
                self.head = Node(self.cache[key])
                return

            new_head = Node(self.cache[key])
            new_head.next = self.head
            self.head = new_head
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        '''after oldest item removed: inserts key,value'''
        self.cache[key] = value


    def set(self, key, value):
        '''Set the key if it is not in the cache.'''
        if len(self.cache) < self.capacity:
            if key not in self.cache:
                self.cache[key] = value
                # self.q.appendleft(key)
                if self.head is None:
                    self.head = Node(value)
                    self.tail = self.head
                    return
                self.tail.next = Node(value)
                self.tail.next.previous = self.tail
                self.tail = self.tail.next
                return

        else:  # If the cache is at capacity remove the oldest item.
            print("cache full: removing the oldest item")

            node = self.tail
            self.tail = self.tail.previous
            del self.cache[node.value]  # remove key from the cache
            self.put(key, value)
            return node.value


def main():
    SIZE_OF_CACHE = 5
    our_cache = LRU_Cache(SIZE_OF_CACHE)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    # print("our_cache",our_cache)

    assert (our_cache.get(1) == 1), "Error, should return 1"       # returns 1
    assert (our_cache.get(2) == 2), "Error, should return 2"       # returns 2
    assert (our_cache.get(9) == -1), "Error,get(9) should return -1"     # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print("cache", our_cache.cache)


    assert (our_cache.get(3) == -1), "Error, get(3) should return -1"  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    ##
    # Test
    ##

if __name__ == '__main__':
    main()
