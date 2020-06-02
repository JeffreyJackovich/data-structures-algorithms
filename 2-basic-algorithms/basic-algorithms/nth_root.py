'''
Root of Number
Many times, we need to re-implement basic functions without using any standard
library functions already implemented.
For example, when designing a chip that requires very little memory space.

In this question we’ll implement a function root that calculates the n’th root of a number.
The function takes a nonnegative number a and a positive integer n, and returns the positive n’th root of a
within an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(a,n)| and must satisfy
 |y-root(a,n)| < 0.001).

Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior
knowledge in numerical analysis (some of them are mentioned here), there is also an elementary method which
doesn’t require more than guessing-and-checking. Try to think more in terms of the latter.

Make sure your algorithm is efficient, and analyze its time and space complexities.

Examples:
input:  a = 7, n = 3
output: 1.913

input:  a = 9, n = 2
output: 3

Constraints:

[time limit] 5000ms

[input] float a 0 ≤ a
[input] integer n 0 < n
[output] float

Math explanation:
 2√9 = 3.
 3 * 3 = 9 OR 3^2 = 9 OR 9 ^ (1/2)

The principal nth root of a is:
    n√a = a^(1/n)
'''

import math

def root(a, n):
    '''returns the actual nth root via python's built-in'''
    # x = a ** (1/n)
    x = math.pow(a, (1 / n))

    return x

# a = 7; n = 3
# output: 1.913
#
# a = 9; n = 2
# print(root(a, n))
#
def nth_root(a, n):
    '''

    :param a:
    :param n:
    :return:
    '''
    upper = a
    lower = 0
    # the actual root
    y = root(a, n)
    midpoint = (upper + lower) / 2
    while upper >= lower:

        if abs(y - midpoint) < 0.001:
            return midpoint

        if midpoint > y:
            upper = midpoint - 1
        else:
            lower = midpoint + 1

    return midpoint

print(nth_root(7, 3))