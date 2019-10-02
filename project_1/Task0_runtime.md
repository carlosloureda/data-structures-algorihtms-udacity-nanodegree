Student provides a file explaining their run time analysis (Worst Case Big O Notation) for each solution they produced.

## Task0.py

We don'take into consideration the open texts.csv and calls.csv as they were given to us:

```python
first_record_of_texts = texts[0]
```

Over the first line, we just are accesing an array by it's index: this is constant: O(1)

```python
last_record_of_calls = calls[-1]
```

Over the second line, we just are accesing an array by it's index: this is constant: O(1)

```python
print(
    f"First record of texts, {first_record_of_texts[0]} texts {first_record_of_texts[1]} at time {first_record_of_texts[2]}")
print(
    f"Last record of calls, {last_record_of_calls[0]} calls {last_record_of_calls[1]} at time {last_record_of_calls[2]}, lasting {last_record_of_calls[3]} seconds")
```

On the print statements we are also accesing arrays by their indexes

THE TIME COMPLEXITY OF THIS PROGRAM IS O(1)
