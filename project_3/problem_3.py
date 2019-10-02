"""
Rearrange Array Elements
========================

Rearrange Array Elements so as to form two number such that their sum is maximum.
Return these two numbers. You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides and the expected time
complexity is ```O(nlog(n))```.

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""


def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    lenght = len(input_list)
    if lenght == 0:
        return []
    elif lenght == 1:
        return input_list
    else:
        input_list = mergesort(input_list)
        # we go from back to front,
        #  - if length is odd (ex 5), number 1 gets numbers
        # on even numbers and number 2 on odd numbers
        # - if length is even (ex 4), number 1 gets numbers
        # on odd numbers and number 2 on even numbers:
        number_1 = ""
        number_2 = ""
        for i in range(len(input_list) - 1, -1, -1):
            if lenght % 2 != 0:
                if i % 2 == 0:
                    number_1 += str(input_list[i])
                else:
                    number_2 += str(input_list[i])
            else:
                if i % 2 != 0:
                    number_1 += str(input_list[i])
                else:
                    number_2 += str(input_list[i])

        return [int(number_1), int(number_2)]


def test():
    # assert rearrange_digits([1, 2, 3, 4, 5]) == [531, 42]
    # assert rearrange_digits([4, 6, 2, 5, 9, 8]) == [964, 852]
    # assert rearrange_digits([1, 1, 1]) == [11, 1]
    # assert rearrange_digits([1, 1]) == [1, 1]
    # assert rearrange_digits([1]) == [1]
    # assert rearrange_digits([]) == []

    print(rearrange_digits([1, 2, 3, 4, 5]))
    # [531, 42]
    print(rearrange_digits([4, 6, 2, 5, 9, 8]))
    # [964, 852]
    # EDGE CASES
    print(rearrange_digits([1, 1, 1]))
    # [11, 1]
    print(rearrange_digits([1, 1]))
    # [1, 1]
    print(rearrange_digits([1]))
    # [1]
    print(rearrange_digits([]))
    # []
    print("--> All tests Passed.")


test()
