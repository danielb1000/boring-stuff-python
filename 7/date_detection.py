"""
Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years;
it will accept nonexistent dates like 31/02/2020 or 31/04/2021. 
Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. 
April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. 
Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. 
Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
"""

import re
# 3 groups (day) (month) (year)
date_pattern = r'^(\d{2})/(\d{2})/(\d{4})$'

# Sample input strings
date_strings = [
    "31/12/2020",
    "01/01/1999",
    "15/03/2500",
    "31/02/2020",  # invalid
    "30/04/2021",
    "30/4/2021"    # invalid
]

def is_valid_date(day:int, month:int, year:int):
    # month:days_in_month
    # values are ints, because the function receives ints
    # 
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # leap year for February
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29

    # validate month and day
    if month in days_in_month and 1 <= day <= days_in_month[month]:
        return True
    return False

# process each date string
for date_string in date_strings:
    match = re.match(date_pattern, date_string)
    # if string fits the pattern, match returns a re.Match object like :
    # Date: 31/12/2020, Match: <re.Match object; span=(0, 10), match='31/12/2020'>
    
    # otherwise, match returns None    
    if match:
        # ignore this::::::::::::::::: day, month, year = map(int, match.groups()) 
        # convert strings to ints
        # "01" will become 1, etc. necessary for the is_valid_date function
        # match.groups() returns stuff like ->>> ('31', '12', '2020')
        day = int(match.groups()[0])
        month = int(match.groups()[1])
        year = int(match.groups()[2])

        if is_valid_date(day, month, year):
            print(f"{date_string} is a valid date.")
        else:
            print(f"{date_string} is not a valid date.")
    else:
        print(f"{date_string} does not match the date format.")
