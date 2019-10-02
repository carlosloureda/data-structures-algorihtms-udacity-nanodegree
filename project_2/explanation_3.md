## Project 3

For this approach using the information on the [wikipedia ](https://en.wikipedia.org/wiki/Huffman_coding) I decided to create a class for the Huffman encoder and 2 other auxiliar classes:

    - A Tree class
    - A Queue class, which also uses a Node class

### Queue:

We first want to be able to create the queue as an array, where each element is a Node element with: the `char` element that represents, the `freq` of the appearence the char in the string and of course a way to point to its children (`left` and `right`)

So when we create a new Queue, we get the string and we create a new array with the information for the `char` and the `freq`.

Now we need to sort the array with increased frequency. So we create a inner method `sort`for this Queue object

---

The compresing algorithm has shown, for the tested example a reduction of almost 50% of its size.

## Tree

Once we have our Queue with the letters and their prioities on it we pass this queue to the Tree class.

When creating our tree we set the root of our tree as the first element of the queue.
But for this step if we take a loop to the algorithm pseudocode, we need to fuse the every too nodes on every step, for this we need a `fuse` inside the `Queue` class but also a `fuse` nodes inside the Node auxiliary class.

Once the tree is created we need to pass it into a binaryzed tree, with 1/0 values.

## Huffman

We create this clas, initializes an inner array (from the binaryzed tree).
This inner array is the `encofing_table`, whihch is created recursively with the `create_encoding_table` method.

I also created 2 dictionaries, the `encoding_dict` and the `decoding_dict` where both of them have as `keys` the character and as `values` the frequency of that character.

Now we just need the `encode` and the `decode` methods to call them on the execution of our programm.

## Time complexity

As I read on the article of [reference at Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding#Optimality) being _L_ the maxium lenght of a codeware, the timecomplexity would be of **O(Ln)**.

But for sorting I used the built-in function `sorted` but if I had used my own `sorting algorithm` I would increase the time complexity of this algorithm to **O(n\*log(n))**.

## Space complexity

The _space complexity_ of this algorithm is directly related to the _size of the alphabet used_, represented as _s_, ending up with a complexity of **O(s)**.
