Student provides a file explaining their run time analysis (Worst Case Big O Notation) for each solution they produced.

## Task3.py

We don'take into consideration the open texts.csv and calls.csv as they were given to us:

THE TIME COMPLEXITY OF THIS PROGRAM:

    - PART A IS **O(n^2)**  #TODO: Check the O(n) on startswith
    - PART B IS **O(n)**

```python
def filter_callers_by_area_code(code, calls):
    return [call for call in calls if code in call[0]]
```

- Creates an array
- Loops over array: O(n)
  - Access the index inside the aray in every loop, O(1)

O(n)

```python
def get_area_code(phone):
    area_code = None
    if phone[0] == "(":  # mobile phone
        area_code = phone[0: phone.find(")") + 1]
    elif phone.startswith("140"):
        area_code = 140
    elif phone[0] in ["7", "8", "9"]:
        area_code = phone[0: phone.find(" ") -1 ]
    return area_code
```

The time complexity of startswith is just constant O(1) because it simply compares the starting digits of the number which are not more than 3 digits everytime and hence constant.

Worst case scenario is the array splitting which is O(k) being k the size of the split, this would be 4-5 which is also constant

`get_area_code` is **O(1)**

```python
def get_receivers_area_codes(calls):
    list_of_codes = []
    for call in calls:
        area_code = get_area_code(call[1])
        if area_code not in list_of_codes:
            list_of_codes.append(area_code)
    list_of_codes.sort()
    return list_of_codes
```

- Receives a list, so input size is n
- For loop is O(n)
  - Append list is O(1) : [Info](https://wiki.python.org/moin/TimeComplexity/#list)
- Sorting the array using the Python sort algorithm: _O(n log n)_

So this function is now **O(n log n)**

```python
def get_receivers_area_codes_no_reps(calls):
    list_of_codes = []
    for call in calls:
        if call[1] not in list_of_codes:
            list_of_codes.append(get_area_code(call[1]))
    return list_of_codes

```

- Receives a list, so input size is n
- For loop is O(n)
  - On worst case, we append all items:
    - get*area_code : \_O(n)* # TODO: check this
    - Append list: is O(1) : [Info](https://wiki.python.org/moin/TimeComplexity/#list)

So this function is O(n\*n): _O(n^2)_

```python
def get_percentage_calls_to_bangalore(list_of_codes):
    total_calls = len(list_of_codes)
    total_calls_to_bagalore_fixed_line = len([
        code for code in list_of_codes if code == "(080)"])

    return round(total_calls_to_bagalore_fixed_line * 100/total_calls, 2)

```

- Receives a list, so input size is n
- For loop is O(n)

So this function is O(n): _O(n)_
