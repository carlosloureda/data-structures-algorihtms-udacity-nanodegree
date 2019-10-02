This problem is based on a pseudo ordered array, and as we pursue a O(log n)
time complexity we will seek the _Divide & Conquer Approach_.

So I copied the code from the lessons for the _binary search recursive_ and just used it
to search in the array as a helper function

## Time complexity

The time complexity being an algorithm based on binary search is **O(log(n))**.

## Space complexity

We have to take into consideration the space of the recursion call stack of the binary search,which is **O(log(n))**

This O(log(n)) space is the auxiliary space complexity, if we think about al the space
complexity too, the space occupied by the input is also considered, so it will be **O(n)**
where 'n' is the number of elements in the input list.
