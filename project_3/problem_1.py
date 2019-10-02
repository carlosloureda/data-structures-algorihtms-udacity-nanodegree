"""
Finding the Square Root of an Integer
=====================================

Find the square root of the integer without using any Python library. You have to find
the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(27) = 5.196 whose floor
value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return "No real square root exists for this input!"
    elif number == 0 or number == 1:
        return number

    start = 0
    end = number // 2

    while start <= end:
        middle = (end + start) // 2
        middle_pow = middle * middle

        if middle_pow == number:
            return middle
        elif middle_pow < number:
            start = middle + 1
            result = middle
        else:
            end = middle - 1

    return result


def test():
    print(sqrt(0))
    # 0
    assert 0 == sqrt(0)

    print(sqrt(1))
    # 1
    assert 1 == sqrt(1)

    print(sqrt(2))
    # 1
    assert 1 == sqrt(2)

    print(sqrt(9))
    # 3
    assert 3 == sqrt(9)

    print(sqrt(16))
    # 4
    assert 4 == sqrt(16)

    print(sqrt(27))
    # 5
    assert 5 == sqrt(27)

    print(sqrt(121))
    # 11
    assert 11 == sqrt(121)
    print("--> All tests passed")

    print(sqrt(-1))
    # "No real square root exists for this input!"
    assert "No real square root exists for this input!" == sqrt(-1)

    print(sqrt(134548324234))
    # 366808
    assert 366808 == sqrt(134548324234)
    print("--> All edge cases tests passed")


test()
