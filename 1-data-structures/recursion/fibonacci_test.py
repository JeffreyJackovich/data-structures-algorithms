'''
TODO: Test fibonacci recursive function
'''
from fibonacci import fib

def test_fib():
    '''tests the first 6 fib nummbers'''

    fib_dict = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8}
    for n in fib_dict:
        result = fib(n)
    assert result == fib_dict[n]

