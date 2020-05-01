'''
TODO: calculate the sum of all integers from 1 to n recursivlely

Formula:
    if n == 1 --> return 1
    n+(n-1)

Ex:
    n=3
    3+2+1

'''
def sum_int(n):
    if n == 1:
        return 1
    else:
        return n + sum_int(n-1)

print(sum_int(3))