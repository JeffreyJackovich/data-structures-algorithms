'''
TODO:
'''

def is_palindrome(my_str):
    '''return True if palindroe, else False'''
    if len(my_str) == 1:
        return True
    else:
        return (my_str[0] == my_str[-1]) and is_palindrome(my_str[1:-1])


print('pass' if (True == is_palindrome('kayak')) else 'fail')
print('pass' if (False == is_palindrome('cat')) else 'fail')