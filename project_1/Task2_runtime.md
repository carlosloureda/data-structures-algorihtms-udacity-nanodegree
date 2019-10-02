Student provides a file explaining their run time analysis (Worst Case Big O Notation) for each solution they produced.

## Task2.py

We don'take into consideration the open texts.csv and calls.csv as they were given to us:

THE TIME COMPLEXITY OF THIS PROGRAM IS **O(n²)**

```python
def get_phone_number_statistics(calls):
    phone_numbers = {}
    for line in calls:
        phone_number_1, phone_number_2, time, seconds = line
        seconds = int(seconds)
        if phone_number_1 not in phone_numbers:
            phone_numbers[phone_number_1] = [phone_number_1, seconds, time]
        else:
            phone_numbers[phone_number_1][1] = int(
                phone_numbers[phone_number_1][1]) + seconds
        if phone_number_2 not in phone_numbers:
            phone_numbers[phone_number_2] = [phone_number_2, seconds, time]
        else:
            phone_numbers[phone_number_2][1] = int(
                phone_numbers[phone_number_2][1]) + seconds
    return phone_numbers
```

The loop will run len(arr) times, so being arr n, would run n times the lines: - add elements to a dictionary: O(n) - update element in a dictionary: O(n)

Adding an element to a set has complexity: [O(1)](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

So my solution is O(n) because inside a loop we do 2 operations that take O(1),
this is O(2*1) and repeated n times: O(n*2), that simplifies to O(n)

```python
    def biggest_seconds(phone_number_info): #dictionary
        biggest = (0, 0, None)  # phone, seconds, timestamp
        for key in phone_number_info:
            # print("phone_number_info[key]: ", phone_number_info[key])
            if int(phone_number_info[key][1]) > int(biggest[1]):
                time = datetime.datetime.strptime(
                    phone_number_info[key][2], "%m-%d-%Y %H:%M:%S").strftime("%B %Y")
                biggest = (
                    phone_number_info[key][0], phone_number_info[key][1], time)
        return biggest

```

Since dictionaries are implemented as hash tables and here we can assume that there is no possibility of hash collisions in out hash functions. So this would make the time complexity of accessing an array in dictionary to be constant O(1).

So this function is O(n) as it loops over the length of the phone_number_info and spends O(1) on the
inner steps.

```python
    def get_max_user_info(calls):
        phone_statistics = get_phone_number_statistics(calls)
        return biggest_seconds(phone_statistics)
```

It makes a call to a function with O(n) and another call O(n^: O(2\*n) which
simplifies to **O(n)**
