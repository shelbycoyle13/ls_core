# 46. Triple double
# Write a function triple_double(num1, num2) which takes numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2. If this isn't the case, return 0

#print(triple_double(12345, 12345) == 0)
#print(triple_double(666789, 12345667) == 1) # 3 straight 6's in num1, 2 straight 6's in num2

"""
P
input = two numbers
output = an integer
explicit = we have two integer arguments. in order for us to return 1, there has to be triple digits of a number in num1 AND straight double of a digit in num2. Otherwise, return 0. The numbers of triple and double have to be the SAME
implicit = 

E

D
list

A
first, we want to coerce num1 and num2 into strings so we can iterate over them

then, iterate over the set of the first string to only count unique numbers
    if digit * 3 is in string1 and the SAME digit * 2 is in string 2
        return 1
    else
        return 0

C
"""

def triple_double(num1, num2):
    string_num1 = str(num1)
    string_num2 = str(num2)

    for digit in set(string_num1):
        if digit * 3 in string_num1 and digit * 2 in string_num2: #Since digit is a string, we can also multiply it to get consecutive "numbers"
            return 1
        else:
            return 0

print(triple_double(12345, 12345) == 0)
print(triple_double(666789, 12345667) == 1)