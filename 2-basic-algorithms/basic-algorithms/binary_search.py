'''
Return True if the value is in a list, otherwise False.
'''


def binary_search(a_list, target_value):

    target_found = False
    # TODO: check if odd or even
    # TODO: how to update upper and lower bound?
    # TODO: what condition to end searching

    list_len = len(a_list)
    upper_ix = list_len
    lower_ix = 0

    max_search_num = list_len // 2
    searches = 0
    while searches < max_search_num:

        midpoint_ix = ((upper_ix + 1) - lower_ix) // 2
        # print(midpoint_ix)

        if a_list[midpoint_ix] == target_value:
            target_found = True
            return target_found

        elif a_list[midpoint_ix] > target_value:
            upper_ix = midpoint_ix
            searches += 1
        else:
            lower_ix = midpoint_ix
            searches += 1

    return target_found


# a_list = [1,2,3,4,5,6,7,8,9]
# target_value = 2

a_list = [1,2]
target_value = 2
print(binary_search(a_list, target_value))