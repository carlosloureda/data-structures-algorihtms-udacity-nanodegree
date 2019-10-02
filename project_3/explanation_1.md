In this exerice we are asked to conduct a solution with O(log(n)).
I thought about a variance of the _binary search_ algorithm but in our example
we have a number and not an array (sorted), so I decided to go through the natural
order of the numbers.

I thought that as the square of a number is less than the half of that number, so
I decided to traverse the 'natural numbers' until the half of the original number.

The version of this algorithm will check against the mid point number on each
iteraction, so we compare if it is bigger or smaller .

## Time complexity:

As I mentioned above, the time complexity is **O(log(n))**, I am using a 'binary search approach'.

## Space complexity:

It is **independent of the input**, so it is **O(1)**.
