Student provides a file explaining their run time analysis (Worst Case Big O Notation) for each solution they produced.

## Task4.py

We don'take into consideration the open texts.csv and calls.csv as they were given to us:

THE TIME COMPLEXITY OF THIS PROGRAM IS **O(n^2)**

```python
def get_callers_phone_numbers(calls):
    phones = set([])
    receiver_phones = [call[1] for call in calls]
    for call in calls:
        if call[0] not in receiver_phones:
            phones.add(call[0])
    return phones
```

- Receives an array, len: n
- Loops over array receiver_phones: O(n)
- 2nd Loop: n times
  - Adding an element to a set has complexity: [O(1)](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
  - So this 2nd loop is _O(n)_

This function is: _O(n)_

```python
def remove_non_text_phones(texts, phones):
    for text in texts:
        number1, number2, _ = text
        if number1 in phones:
            phones.discard(number1)
        if number2 in phones:
            phones.discard(number2)
    phones = list(phones)
    phones.sort()
    return phones
```

- Receives 2 arrays, texts: n and phones: m
- Loops over array texts: O(n)

  - Deleting an item from a set takes constant O(1) time.
  - The ifs are: O(1), as we are sets are implemented as hash tables and we can assume there is no possibility of hash collisions.

  - Inside the loop: O(1)+O(1)+O(1)+O(1) : O(4)

- Create list is O(n)
- Sort the list: O(n log n)

This function is: n * O(4) + O(n) + O(n log n) => O(4*n) + O(n) + O(n log n) => O(n) + O(n) + O(n log n) ==> O(n) + O(n log n): **O(n \* log n)**

```python
def get_possible_marketers_phones(calls, texts):
    phones = get_callers_phone_numbers(calls)
    phones = remove_non_text_phones(texts, phones)
    return phones
```

- Call to get_callers_phone_numbers: O(n)
- Call to remove_non_text_phones: O(n \* log n)

So everything is **O(n \* log n)**
