import time

'''
TODO: optimize the nth fibonacci number recursive function with a cache

Formula: Fn = Fn-1 + Fn-2
    F_0 = 0
    F_1 = 1

n: 0, 1, 2, 3, 4, 5, 6
f: 0, 1, 1, 2, 3, 5, 8

'''
def fib(n, cache):
    '''returns the nth term of the fib. sequence'''
    #if cached the value, return it
    if n in cache:
        return cache[n]

    #compute nth term
    else:
        result = (fib(n-1, cache) + fib(n-2, cache))
        cache[n] = result
        return result



cache = {0:1, 1:1, 2:1}
n = 5
# print(fib(n, cache))


start = time.time()
fib(1000, cache)
stop = time.time()
print("{} seconds".format(stop-start)) #  0.002521991729736328 seconds