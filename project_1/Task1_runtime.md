Student provides a file explaining their run time analysis (Worst Case Big O Notation) for each solution they produced.

## Task1.py

We don'take into consideration the open texts.csv and calls.csv as they were given to us:

THE TIME COMPLEXITY OF THIS PROGRAM IS **O(n)**

```python
def getTelephonesInArray(phoneSet, arr):
    for elem in arr:
        phoneSet.add(elem[0])
        phoneSet.add(elem[1])
    return phoneSet
```

The loop will run len(arr) times, so being arr n, would run n times the lines:
elm[0] and elm[1] are just accesing arrays by indexes.

Adding an element to a set has complexity: [O(1)](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

So my solution is O(n^2) because inside a loop we do 2 operations that take O(1),
this is O(1) and repeated n times: O(n\*1), that simplifies to O(n)

```python
phoneSet = set([])
phoneSet = getTelephonesInArray(phoneSet, texts)
phoneSet = getTelephonesInArray(phoneSet, calls)
```

2 calls for O(n²) keeps the algorithm on O(n²)
