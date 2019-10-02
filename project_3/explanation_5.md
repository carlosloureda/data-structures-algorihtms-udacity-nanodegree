We are asked to build a **trie** to solve this problem, with some changes.

# find()

Method for **Trie** class. This method receives a prefix and loops over the nodes
in the tree trying to find the the last node that hast the last character in the prefix.
On every step of the loop we seach for the children of a node and check if the char in the
prefix is on the children, if not present we return False as we didn't find the prefix,
if present, we move to next node having that char.

# insert()

Method for **Trie** class. We iterate the same way as on find, we iterate over the
characters of a word and for every character we do: - if there is a node with that char we move next - if there isn't a node with that char we add a new TrieNode with that character
content.

    - For both cases, if we are at the end of the word (last character) we set the
    is_word parameter to True

# suffixes()

Method for **TrieNode** class. We kkep an array to get all the suffixes found for that suffix:

- If we get into a `is_word` node in the trie and we passed a suffix, we append the
  suffix to the results arrays.
- We want to check the children for the current **TrieNode** , if no children we just end
  the recursion here (return the suffixes array), if there are children, what we do is
  try to find the suffixes for a new suffix, which is the previous suffix appended with the
  char in the current TrieNode, on the result of this recursion we extend the results (\_suffixes)
  array with the new suffixes.

## Time complexity

In a **trie** time complexity of **searching and inserting** depends on the length
of the word (**a**) that’s being searched for, inserted, and the number of total words, **n**,making the runtime of these operations **O(a\*n**).

## Space complexity

For our **trie**, the worst case,is when we have a word with no common characters between them, this is, a node for each letter. Resulting in a _space complexity_ of **O(n)**.
