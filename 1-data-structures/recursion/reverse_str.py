'''
TODO: reverse string recursively
'''

def reverse_str(my_str):
    '''EfficienyO(n*k) '''
    if len(my_str) == 1:
        return my_str[0]
    else:
        return reverse_str(my_str[1:]) + my_str[0]

print(reverse_str('cat'))

print('pass' if ('tac' == reverse_str('cat')) else 'fail')