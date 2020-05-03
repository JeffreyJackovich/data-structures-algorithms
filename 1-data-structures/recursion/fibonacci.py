import time

'''
TODO: output the nth fibonacci number recursively

Formula: Fn = Fn-1 + Fn-2
    F_0 = 0
    F_1 = 1

n: 0, 1, 2, 3, 4, 5, 6
f: 0, 1, 1, 2, 3, 5, 8

'''
def fib(n):
    '''returns the nth fib number'''
    if n < 2:
        return n
    else:
        return (fib(n-1) + fib(n-2))

print(fib(3))

#
# start = time.time()
# fib(10)
# stop = time.time()
# print("{} seconds".format(stop-start)) # 2.384185791015625e-05 seconds
#
# start = time.time()
# fib(20)
# stop = time.time()
# print("{} seconds".format(stop-start)) # 0.0026519298553466797 seconds
#
# start = time.time()
# fib(30)
# stop = time.time()
# print("{} seconds".format(stop-start)) # 0.33413100242614746 seconds
#
# start = time.time()
# fib(35)
# stop = time.time()
# print("{} seconds".format(stop-start)) # 3.716248035430908 seconds