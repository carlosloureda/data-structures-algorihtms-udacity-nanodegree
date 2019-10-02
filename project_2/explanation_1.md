We need to use a data structure that has constant time for put/set so we can use
dictionaries, but for sorting that dictionary with 'access priorities' we need to
keep the dictnioary order, in this case Python 3 has a special data structure: _OrderedDicts_
that remembers the order of insertion on a dictionary.

We can add the elements to the dictionary so the first dictionary element would be the
least recently used, and if we access and get the an element on the dictionary, we can
remove it and set it again on the dictionary so it remains the last element and would be
further away from the lru element.

## Time complexity

We had some limiations for this approach, I discarded the idea of _hashing_ because we have the risk of a collision. So I decided this approach which is **O(1)**.

## Space complexity

This structure requires the usage of **c**, being the desired _LRU_Cache_ capacity; being it in the end assimilable to **O(n)**.
