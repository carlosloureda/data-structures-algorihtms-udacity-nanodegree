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

There are three different kinds of telephone numbers, each with a different format:

Fixed lines start with an area code enclosed in brackets.
  The area codes vary in length but always begin with 0. Example: "(022)40840621".
Mobile numbers have no parentheses, but have a space in the middle of the number to help readability.
  The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
Telemarketers' numbers have no parentheses or space,
  but start with the code 140. Example: "1402316533".

TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Filters for callers which have one area code (this is fixed lines starting with ...)
"""


def filter_callers_by_area_code(code, calls):
    return [call for call in calls if code in call[0]]


def get_area_code(phone):
    area_code = None
    if phone[0] == "(":  # mobile phone
        area_code = phone[0: phone.find(")") + 1]
    elif phone.startswith("140"):
        area_code = 140
    elif phone[0] in ["7", "8", "9"]:
        area_code = phone[0: phone.find(" ")-1]
    return area_code


def get_receivers_area_codes(calls):
    list_of_codes = []
    for call in calls:
        area_code = get_area_code(call[1])
        if area_code not in list_of_codes:
            list_of_codes.append(area_code)
    list_of_codes.sort()
    return list_of_codes


bangalore_callers = filter_callers_by_area_code("(080)", calls)
list_of_codes = get_receivers_area_codes(bangalore_callers)
print("The numbers called by people in Bangalore have codes: ",
      "\n".join(list_of_codes))

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits

Task 3 - The script correctly prints the telephone codes called by fixed-line numbers
in Bangalore and the percentage of calls from fixed lines in Bangalore that are to fixed lines in Bangalore.
"""


def get_percentage_calls_to_bangalore(list_of_codes):
    total_calls = len(list_of_codes)
    total_calls_to_bagalore_fixed_line = len([
        code for code in list_of_codes if code == "(080)"])

    return round(total_calls_to_bagalore_fixed_line * 100/total_calls, 2)


percentage = get_percentage_calls_to_bangalore(list_of_codes)
print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
