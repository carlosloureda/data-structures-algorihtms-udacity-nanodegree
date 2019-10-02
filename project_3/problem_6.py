"""
Max and Min in a Unsorted Array
===============================

In this problem, we will look for smallest and largest integer from a list of unsorted
integers. The code should run in O(n) time. Do not use Python's inbuilt functions
to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm
(i.e., linear time)?
"""


import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    elif len(ints) == 1:
        return (ints[0], ints[0])
    else:
        _min = ints[0]
        _max = ints[0]
        for number in ints:
            if number > _max:
                _max = number
            if number < _min:
                _min = number

    return (_min, _max)

# Example Test Case of Ten Integers


def test():
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    assert (0, 9) == get_min_max(l)
    print(get_min_max(l))
    # (0, 9)

    l = [i for i in range(1, 51)]  # a list containing 1 - 50
    random.shuffle(l)
    assert (1, 50) == get_min_max(l)
    print(get_min_max(l))
    # (1, 50)

    l = [i for i in range(1, 100)]  # a list containing 1 - 99
    random.shuffle(l)
    assert (1, 99) == get_min_max(l)
    print(get_min_max(l))
    # (1, 99)

    l = [i for i in range(300, 301)]  # a list containing 300
    random.shuffle(l)
    print(get_min_max(l))
    # (300, 300)

    l = []  # an empty list
    print(get_min_max(l))
    # None

    l = [i for i in range(-24, -1)]  # a list containing -24 - -2
    random.shuffle(l)
    print(get_min_max(l))
    # (-24, -2)

    print("--> All tests Passed.")


test()
