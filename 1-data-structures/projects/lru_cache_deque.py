from collections import deque

'''
TODO: Code a Least Recently Used data structure with a dict and queue.
    - enqueue() at head and dequeue at the tail
    - get() when key is accessed, move corresponding node to the front of the queue
'''
class LRU_Cache:

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.q = deque([])

    def get(self, key):
        '''Checks the cache for a key.
            If the cache:
                returns a key's value
                AND
                move the key to the front of the queue
            If not in cache, return -1

        Efficiency: O(1)'''
        if key in self.cache: # cache hit
            value = self.cache[key]
            self.q.remove((key, value))
            self.q.append((key, value)) # move accesed key to the head the the queue
            return value
        else:
            return -1

    def put(self, key, value):
        '''after oldest item removed: inserts key,value'''
        self.cache[key] = value
        self.q.append((key,value))

    def set(self, key, value):
        '''Set the key if it is not in the cache.'''
        if key is None or value is None:
            print("error: key or value is None type")
            exit()
        elif type(key) is str or type(value) is str:
            print("error: key or value is str type")
            exit()
        else:
            if len(self.cache) < self.capacity:
                if key not in self.cache:
                    self.cache[key] = value #add new value to the dict
                    self.q.append((key, value)) #add new value to the queue

            else:  # If the cache is at capacity remove the oldest item.
                print("cache full: removing the oldest item")
                oldest_key, oldest_value = self.q.popleft() # remove oldest item from the queue
                del self.cache[oldest_key]  # remove key from the cache
                self.put(key, value)


    def __repr__(self):
        '''Returns a string representation of the queue'''
        if len(self.q) > 0:
            s = "<enqueue here>\n_________\n"
            s += "\n____________\n".join([str(item) for item in self.q])
            s += "\n____________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

def main():
    SIZE_OF_CACHE = 5
    our_cache = LRU_Cache(SIZE_OF_CACHE)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    # print("our_cache",our_cache)

    assert (our_cache.get(1) == 1), "Error, should return 1"       # returns 1
    assert (our_cache.get(2) == 2), "Error, should return 2"       # returns 2
    assert (our_cache.get(9) == -1), "Error,get(9) should return -1"     # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print("cache", our_cache.cache)
    assert (our_cache.get(3) == -1), "Error, get(3) should return -1"  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    ######################
    # Test 1 - None type
    #####################
    # cache_test = LRU_Cache(SIZE_OF_CACHE)
    # cache_test.set(None, None) # error: key or value is None
    #
    ###################
    # Test 2 - str type
    ###################
    cache_test_2 = LRU_Cache(SIZE_OF_CACHE)
    cache_test_2.set("1","1")  #error: key or value is str type
    ###################
    # Test 3 -
    ###################


if __name__ == '__main__':
    main()
