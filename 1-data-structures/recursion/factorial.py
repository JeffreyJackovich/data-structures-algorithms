'''
TODO:

Formula: n! = n * (n-1)

Example:
    4! = 4 * 3 * 2 * 1 = 24
'''

def get_factorial(n):
    if n == 1:
        return 1
    else:
        output = get_factorial(n - 1)
        print("output: {}".format(output))
        return n * output


print(get_factorial(4))
