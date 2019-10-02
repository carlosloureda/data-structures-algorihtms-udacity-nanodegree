<!-- For the **union and intersection** problem, the approach has been to transform the _linked lists_, a format which is
harder to work with, on something much **simpler** as is a list. Once the transformation has been done, the combination
with the handy _object_ **sets**, has done all the work. -->

## Time complexity

On our LinkedList implementation we added 4 methods, where their time complexity is:

- append: **O(n)**. Iterates over all the blocks in the chain.
- size: **O(n)**. Iterates over all the blocks in the chain.
- to_list: It takes **O(n)** as it needs to loop over all the nodes in the blockchain on the worst case scenario (where the element is not found)

We had to create 2 new functions for solving the problem:

- _Union_:
    - We have to pass the linked lists to lists, this is _2*O(n)_
    - We create a set adding both lists, this is converting a list to a set, so iterating over the list is _O(n)_ and adding each element to the hash set is _O(1)_, so the total operation is _O(n)_
    - We iterate over the lists elements to create the new linked list: _O(n)_

    We have a final time complexity of **O(n)**.

- _Intersection_:
    - We have to pass the linked lists to lists, this is _2*O(n)_
    - We create a set adding both lists, this is converting a list to a set, so iterating over the list is _O(n)_ and adding each element to the hash set is _O(1)_, so the total operation is _O(n)_
    - We iterate over the lists elements to create the new linked list: _O(n)_

    We have a final time complexity of **O(n)**


## Space complexity

For these cases, we are generating for both _union_ and _intersection_ functions 3 lists to solve the problem, being the space complexity of those: _O(3n)_, resulting in **O(n)** .
