'''
Return the index if the value is in a list, otherwise -1.
'''


def binary_search(a_list, target_value):
    '''

    :param a_list:
    :param target_value:
    :return:
    '''
    upper_ix = len(a_list)
    lower_ix = 0

    while lower_ix < upper_ix:

        midpoint_ix = (upper_ix - lower_ix) // 2

        if a_list[midpoint_ix] == target_value:
            return midpoint_ix

        if a_list[midpoint_ix] < target_value:
            lower_ix = midpoint_ix + 1
        else:
            upper_ix = midpoint_ix - 1

    return -1


# a_list = [1,2,3,4,5,6,7,8,9]
# target_value = 2

a_list = [1,2,3]
target_value = 2
print(binary_search(a_list, target_value))