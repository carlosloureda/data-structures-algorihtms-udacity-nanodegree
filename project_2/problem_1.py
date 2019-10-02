"""
Least Recently Used Cache
== == == == == == == == == == == == =

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation(i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used(LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
"""


"""
Explanation
-----------

We need to use a data structure that has constant time for put/set so we can use
dictionaries, but for sorting that dictionary with 'access priorities' we need to
keep the dictnioary order, in this case Python 3 has a special data structure: OrderedDicts
that remembers the order of insertion on a dictionary.


We can add the elements to the dictionary so the first dictionary element would be the
least recently used, and if we access and get the an element on the dictionary, we can
remove it and set it again on the dictionary so it remains the last element and would be
further away from the lru element.

"""




from collections import OrderedDict
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.lru_cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # get element value and remove it from the dictionary

        try:
            element = self.lru_cache.pop(key)
        except KeyError:

            # whenever we want to get or pop a non existent key a KeyError expection
            # is raised

            return -1

        # add the element to the dictionary again to update the priority
        self.lru_cache[key] = element

        # return the element
        return element

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.

        if self.capacity == 0:
            print("Can't add elements on 0 capacity cache")
            return

        if self.lru_cache.get(key) == value:
            return -1
        else:
            # check for max capacity
            if len(self.lru_cache) == self.capacity:
                # remove first element of the ordered dictionary, as it should be
                # the least used
                # True removes last, False removes first
                self.lru_cache.popitem(False)

            self.lru_cache[key] = value


def test():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))
    # 1
    assert our_cache.get(1) == 1

    print(our_cache.get(2))
    # 2
    assert our_cache.get(2) == 2

    print(our_cache.get(9))
    # -1, because 9 is not present in the cache
    assert our_cache.get(9) == -1

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # recently used entry
    print(our_cache.get(3))
    # returns -1 because the cache reached it's capacity and 3 was the least
    # assert our_cache.get(3) == -1

    # EDGE CASES

    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)
    # Can't add elements on 0 capacity cache

    print(our_cache.get(1))
    # -1

    print("All test passed")


test()
