import time

'''
TODO: optimize the nth fibonacci number recursive function with a cache

Formula: Fn = Fn-1 + Fn-2
    F_0 = 0
    F_1 = 1

n: 0, 1, 2, 3, 4, 5, 6
f: 0, 1, 1, 2, 3, 5, 8

'''
def fib(n):
    '''returns the nth fib number'''
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_cache = {1:1, 2:1}


start = time.time()
fib(10)
stop = time.time()
print("{} seconds".format(stop-start)) #  seconds

start = time.time()
fib(20)
stop = time.time()
print("{} seconds".format(stop-start)) #  seconds

start = time.time()
fib(30)
stop = time.time()
print("{} seconds".format(stop-start)) #  seconds

start = time.time()
fib(35)
stop = time.time()
print("{} seconds".format(stop-start)) #  seconds