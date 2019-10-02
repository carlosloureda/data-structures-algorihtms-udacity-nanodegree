I just decided to use a recursion approach as we can set the logic for the current level, but next levels will be a repetition of the previous level, so using the recursive approach.

On each visit for a folder, we keep the files that match de pattern and later we go deeper the folder structure using recursion.

I used the `os.path.isdir` and `os.path.isfile` methods from `os` module to diff between if a file is a file or a folder.

## Time complexity

We need to go through the depth of the directory structure. It is difficult to know the depth of the structure (numnber of levels) of the width of the folder (number of elements in that folder).
So we can say that we are looping over those elements and our complexity is dependant on _depth_ (d) and _width_ (w), resulting on a **O(d\*w)** time complexity.

## Space complexity

In this case, it is directly dependent on the number of returns the function does, hence, the number of found files _f_, _O(f)_ which is **O(n)**.
