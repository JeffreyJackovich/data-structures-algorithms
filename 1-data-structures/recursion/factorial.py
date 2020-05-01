'''
TODO: factorial

Formula:
    n! = n * (n-1)
        Base:

        Recurse:

Example:
    4! = 4 * 3 * 2 * 1 = 24
'''

def get_factorial(n):
    if n == 1:
        return 1
    else:
        return n * get_factorial(n - 1)


print('pass' if (24 == get_factorial(4)) else 'fail')
print('pass' if (120 == get_factorial(5)) else 'fail')
