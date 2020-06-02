'''
Return the index if the value is in a list, otherwise -1.
'''


def binary_search(a_list, target_value):
    '''

    :param a_list:
    :param target_value:
    :return:
    '''
    upper_ix = len(a_list) - 1
    lower_ix = 0
    midpoint_ix = 0

    while lower_ix <= upper_ix:
        midpoint_ix = (upper_ix + lower_ix) // 2

        if a_list[midpoint_ix] < target_value:
            lower_ix = midpoint_ix + 1

        elif a_list[midpoint_ix] > target_value:
            upper_ix = midpoint_ix - 1

        else:
            return midpoint_ix

    return -1


# a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target_value = 99
#
# result = binary_search(a_list, target_value)
#
# if result != -1:
#     print("Element present at index", str(result))
# else:
#     print("Element NOT present in array")


def test_binary_search():
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_value = 2
    assert binary_search(a_list, target_value) == 1

    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_value = 99
    assert binary_search(a_list, target_value) == -1

    a_list = [1, 2, 3]
    target_value = 2
    assert binary_search(a_list, target_value) == 1

    a_list = [1, 2, 3]
    target_value = 1
    assert binary_search(a_list, target_value) == 0


test_binary_search()