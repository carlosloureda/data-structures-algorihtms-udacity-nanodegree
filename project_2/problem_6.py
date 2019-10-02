"""
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions.
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that
are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either
the union or intersection, respectively.

Once you have completed the problem you will create your own test cases and perform
your own run time analysis on the code.

We have provided a code template below, you are not required to use it:

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        the_list = []
        current = self.head
        while current:
            the_list.append(current.value)
            current = current.next
        return the_list


def union(llist_1, llist_2):
    list_1 = llist_1.to_list()
    list_2 = llist_2.to_list()

    union_list = set(list_1 + list_2)
    union_llist = LinkedList()

    for element in union_list:
        union_llist.append(element)

    return union_llist


def intersection(llist_1, llist_2):
    set_1 = set(llist_1.to_list())
    set_2 = set(llist_2.to_list())

    intersection_linked_list = LinkedList()

    for element in set_1:
        if element in set_2:
            intersection_linked_list.append(element)

    return intersection_linked_list


def test():
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    res = str(union(linked_list_1, linked_list_2))
    print(res)
    # "32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> "
    assert res == "32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> "

    res = str(intersection(linked_list_1, linked_list_2))
    print(res)
    # "4 -> 6 -> 21 -> "
    assert res == "4 -> 6 -> 21 -> "

    print("--> Case 1 tests passed")

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    res = str(union(linked_list_3, linked_list_4))
    print(res)
    # "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> "
    assert res == "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> "

    res = str(intersection(linked_list_3, linked_list_4))
    print(res)
    # "" (empty string)
    assert res == ""

    print("--> Case 2 tests passed")

    # Test case 3, empty lists
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    # Edge Cases:
    res = str(union(linked_list_5, linked_list_6))
    print(res)
    # "" (empty string)
    assert res == ""

    res = str(intersection(linked_list_5, linked_list_6))
    assert res == ""
    print(res)
    # "" (empty string)
    print("--> Case 3 tests passed")


test()
