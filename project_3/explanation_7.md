It is similar to **problem 5**, except for the "root handler", and working with a **paths** instead of strings.

This problem is focused on the development of a **trie** a data structure derived from a _tree_, suited for a good ratio between _time and space_ complexity.

## insert()

Method of class **RouteTrie**, **RouteTrieNode**.

- RouteTrieNode: We check if the path block passed is not in the Node children and if that is the case we insert a new RouteTrieNode with the new path block
- RouteTrie: We want to add nodes to our trie, for every block in the path (element in the array) we insert a new RouteTrieNode (using the RouteTrieNode method insert) and move to the next node. For the last element we also add the handler which will manage the path.

## add_handler()

Method of class **Router**. We want to split the path passed as an string into an array of
block paths and add the handler for that path.

## split_path()

Method of class **Router**. As mentioned above, we want to split the path string into a path array, splitted by "/".

## find()

Method of class **RouteTrie**. We iterate over the Route checking over the children of a node (beginning at the root Node) meanwhile the block content appears on the nodes, so if it doesn't appears we just return False and if it apperas it returns the current node where we are at.

## lookup()

Method of class **Router**. We want to lookup for the path and return the associated handler for that path. First we split the path, if we are at the root path we return the router handler, in the other cases we just find over the router the block for that path, if found we return it, if not I return the non_found_handler that I decided to implement.

### Time complexity

From previous exercises we saw that the time complexity of **searching and inserting** is **O(n)**, being n the lenght of the path we are searching for.

### Space complexity

Looking into the space complexity of a **trie**, the worst case, would be when we have a path with no common folders between them. Resulting in a _space complexity_ of **O(n)**.
