# Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

# print(friday_the_13ths(1986) == 1)      # True
# print(friday_the_13ths(2015) == 3)      # True
# print(friday_the_13ths(2017) == 2)      # True

# Use the datetime.date function to determine whether the 13th of a given month falls on a Friday.

"""
P
input = integer (year)
output = integer (number of Friday the 13ths in that year)
explicit = the year is greater than 1752
implicit = 

E

D
looping

A
-initialize count of 0
-iterate over all of the months in a given year
-for each month, get the day that lands on the 13th
-if it's a friday, add to the count
-return the count

C
"""
import datetime 
# datetime.date

def friday_the_13ths(year_int):
    count = 0

    thirteens = [datetime.date(year_int, month, 13) for month in range(1, 13)]

    for day in thirteens:
        if day.isoweekday() == 5:
            count += 1

    return count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True