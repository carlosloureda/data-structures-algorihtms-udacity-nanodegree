"""
Dutch National Flag Problem
===========================

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the
array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1
    return input_list


def test():
    assert sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) == sorted(
        [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    assert sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) == sorted(
        [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    assert sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == [
        0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

    # EDGE CASES
    assert sort_012([0, 0, 0]) == [0, 0, 0]
    assert sort_012([0, 0]) == [0, 0]
    assert sort_012([0]) == [0]
    assert sort_012([1, 1]) == [1, 1]
    assert sort_012([1]) == [1]
    assert sort_012([2, 2]) == [2, 2]
    assert sort_012([2]) == [2]

    assert sort_012([]) == []

    print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
    # [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
    print(sort_012([]))
    # []
    print(sort_012([1, 1]))
    # [1,1]

    print("--> All tests Passed.")


test()
