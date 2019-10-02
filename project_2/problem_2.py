""""
Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

Here is some code for the function to get you started:

"""

"""
c
# ['t1.c', 'a.c', 'a.c', 'b.c']
h
# ['t1.h', 'a.h', 'a.h', 'b.h']
z
# []
"""




import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == '':
        return []

    files = []
    this_level_files = os.listdir(path)
    for file in this_level_files:
        new_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            # folders_to_explore.append(new_path)
            files.extend(find_files(suffix, new_path))
        elif os.path.isfile(new_path) and file.endswith(suffix):
            files.append(file)

    # print(this_level_files)
    # print(files)

    return files

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python


path = os.getcwd() + '/testdir'


def test():
    files = find_files("c", path)
    print(files)
    # ['a.c', 'a.c', 't1.c', 'b.c']

    files = find_files("h", path)
    print(files)
    # ['a.h', 'a.h', 'b.h', 't1.h']

    # Edge Cases:
    files = find_files("z", path)
    print(files)
    # []

    files = find_files(".gitkeep", path)
    print(files)
    # ['.gitkeep', '.gitkeep']

    files = find_files("", path)
    print(files)
    # []


test()
