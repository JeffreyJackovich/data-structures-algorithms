'''
TODO: power_of_2

Formula:
        Base:
            if n == 0, return 1
        Recurse:
            2 * 2^n-1
Example:

'''

def power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2 * power_of_2(n - 1)

print(power_of_2(5))