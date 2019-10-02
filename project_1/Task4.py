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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

Task 4 - The script correctly prints the list of numbers that could be telemarketers.
"""

# find numbers that do outgoing calls

# remove from that set
# 1. Phones who dont send texts
# 2. Phones who dont receive texts
# 3. Phones who dont receive calls


def get_callers_phone_numbers(calls):
    phones = set([])
    receiver_phones = [call[1] for call in calls]
    for call in calls:
        if call[0] not in receiver_phones:
            phones.add(call[0])
    return phones


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


def get_possible_marketers_phones(calls, texts):
    phones = get_callers_phone_numbers(calls)
    phones = remove_non_text_phones(texts, phones)
    return phones


phones = get_possible_marketers_phones(calls, texts)

print("These numbers could be telemarketers:\n",
      "\n".join(phones))
