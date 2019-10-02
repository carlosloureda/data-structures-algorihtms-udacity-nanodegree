# we go from back to front,

        #  - if length is odd (ex 5), number 1 gets numbers
        # on even numbers and number 2 on odd numbers
        # - if length is even (ex 4), number 1 gets numbers
        # on odd numbers and number 2 on even numbers:

We are required to solve this problem with a _time complexity_ of **O(n\*log(n))**,
In my approach I need to sort the array first so I used the **merge sort** algorithm
that we know it has O(n\*log(n)) time complexity.

Now what I want to do is a single traverse (always O(n), which is smaller than O(n\*log(n)))
and over that traverse I do some tricks:

- I go from the end to the start of the sorted array on a loop
- If the length of the array is an odd number we do:
  - Append the number to first number to be returned (number_1) if it is even number the element we are looping
  - Append the number to second number to be returned (number_2) if it is odd number the element we are looping
- If the length of the array is an even number we do:
  - Append the number to first number to be returned (number_1) if it is odd number the element we are looping
  - Append the number to second number to be returned (number_2) if it is even number the element we are looping

We get this way always a combination that satisfies the condition.

## Time complexity

As the base of the algorithm is the **merge sort**, having a time complexity of **O(n\*log(n))**, and on the loop we do a **(O(n))** so the final result is **O(n\*log(n))**

## Space complexity

The space complexity for mergesort is O(n) and over the loop we are just storing 2 strings so
we keep the space complexity equal to **(O(n))**.
