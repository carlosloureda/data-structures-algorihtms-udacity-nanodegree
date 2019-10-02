I added the `calc_hash` method to the `Block` class so when creating a new Block it has that method available inside the class.

We have to implement the `BlockChain` class, where I decided to create the methods for `appending`, `searching`, printing (`_str_`) or knowing the size (`_len_`) of a BlockChain.

- append:
  - We add the new element as the tail of the BlockChain. Every time we add a new block, this points to the previous block, so each time we add a new element this new block will be the tail of our blockchain
- search:
  - We move over the block chain from the tail to the begining of the linked_list (this is backwards) until we find the block with the given data, unless we loop over the whole linked list without finding it
- _str_
  - I wanted to have a method to print the content of our BlockChain, so I decided to do this in the `_str_` method. This just creates a String representation of our blockchain.
- _len_
  - It is of help also to know the size of the BlockChain, so I decided to do this in the `_len_` method. I just loop over the linkedlist backwards incrementing the counter to set the final size of the chain.

## Time complexity

For our solution we are using a _linked list_ and has several methods:

### append

Append is **O(1)**

### search

Search is **O(n)**

### **len** (size)

\_len\_ is **O(n)**

### **str** (print)

\_str\_ is **O(n)**

## Space complexity

It depends directly on the number of **nodes** for our BlockChain resulting in **O(n)** where n is the number of nodes.
