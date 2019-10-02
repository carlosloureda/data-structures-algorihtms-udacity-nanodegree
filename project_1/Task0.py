"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"

Task 0 - The script correctly prints out the information of first record of texts and last record of calls.
"""

first_record_of_texts = texts[0]
last_record_of_calls = calls[-1]
print(
    f"First record of texts, {first_record_of_texts[0]} texts {first_record_of_texts[1]} at time {first_record_of_texts[2]}")
print(
    f"Last record of calls, {last_record_of_calls[0]} calls {last_record_of_calls[1]} at time {last_record_of_calls[2]}, lasting {last_record_of_calls[3]} seconds")
