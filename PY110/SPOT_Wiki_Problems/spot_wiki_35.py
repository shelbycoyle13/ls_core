# 35. Delete a Digit
# Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

#print(delete_digit(152) == 52)
#print(delete_digit(1001) == 101)
#print(delete_digit(10) == 1)

"""
P
input = an integer
output = an integer
explicit = we want to return the largest number possible when when delete one digit from our current argument
implicit = 

E

D
strings

A
coerce the number into a string
highest_number = 0

iterate through the string, for i, digit in enumerate(string)
    string_copy_minus_one = string.replace(digit, "")
    if int(string_copy_minus_one) > highest_number
        highest_number = int(string_copy_minus_one)


C
"""
def delete_digit(num):
    string = str(num)

    highest_number = 0

    for i, digit in enumerate(string):
        string_copy_minus_one = string.replace(digit, "", 1) #Had to add the count parameter in there because otherwise it replaces all instances of the digit
        if int(string_copy_minus_one) > highest_number:
            highest_number = int(string_copy_minus_one)

    return highest_number

print(delete_digit(152) == 52)
print(delete_digit(1001) == 101)
print(delete_digit(10) == 1)