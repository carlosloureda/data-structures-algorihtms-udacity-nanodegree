We are asked to solve this problem with a **single transverse** to properly order the array.
I used 2 pointers: next_pos_2 and the front_index (also used next_pos_0,) we can order it
in one traverse.

The basis of the pointers in the loop `while front_index <= next_pos_2:` is that
we begin from the beginning (front_index) and the end of the array would be the
`next_post_2` where we would add the first number 2 if we find it. We are traversing
the array with these pointers and also a next_pos_0 to save the positions of the 0 numbers.
While we are moving 0s to the start and the 2s to the end, we move the front_index ahead
when we encounter 0 or 1, and we move next_pos_2 down whenever we find a 0, so once our
front_index reaches the next_pos_2 we should have the array sorted and end the loop.

## Time complexity

In this case the _time complexity_ is precisely, **O(n)**.

## Space complexity

Analyzing the _space complexity_, it is of order **O(1)** (excluding the input space).
