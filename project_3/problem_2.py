"""
Search in a Rotated Sorted Array
================================

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime
complexity must be in the order of ```O(log n)```.

Example:

Input: ```nums = [4,5,6,7,0,1,2], target = 0, Output: 4```

Here is some boilerplate code and test cases to start with:
"""


def binary_search_recursive(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index

    index_left_side = binary_search_recursive(
        array, target, start_index, mid_index - 1)
    index_right_side = binary_search_recursive(
        array, target, mid_index + 1, end_index)

    return max(index_left_side, index_right_side)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search_recursive(input_list, number, 0, len(input_list) - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]

    index = rotated_array_search(input_list, number)
    # assert linear_search(in
    assert linear_search(input_list, number) == index


def test():

    input_list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
    number = 6
    index = rotated_array_search(input_list, number)
    print(index)
    # 0
    assert linear_search(input_list, number) == index

    input_list = [6, 7, 8, 9, 10, 1, 2, 3, 4]
    number = 1
    index = rotated_array_search(input_list, number)
    print(index)
    # 5
    assert linear_search(input_list, number) == index

    input_list = [6, 7, 8, 1, 2, 3, 4]
    number = 8
    index = rotated_array_search(input_list, number)
    print(index)
    # 2
    assert linear_search(input_list, number) == index

    input_list = [6, 7, 8, 1, 2, 3, 4]
    number = 10
    index = rotated_array_search(input_list, number)
    print(index)
    # -1
    assert linear_search(input_list, number) == index

    print("--> All tests Passed.")

    input_list = []
    number = 2
    index = rotated_array_search(input_list, number)
    print(index)
    # -1
    assert linear_search(input_list, number) == index

    input_list = [1]
    number = 0
    index = rotated_array_search(input_list, number)
    print(index)
    # -1
    assert linear_search(input_list, number) == index

    #  searching in the unsorted part of a rotated array
    input_list = [6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
    number = 1
    index = rotated_array_search(input_list, number)
    print(index)
    # 7
    assert linear_search(input_list, number) == index

    print("--> All EDGE tests Passed.")


test()
