# 17. Expanded Form of Number

# You will be given a number, and you need to return it as a string in
# expanded form. For example:

# expanded_form(12) # should return '10 + 2'
# expanded_form(42) # should return '40 + 2'
# expanded_form(70304) # should return '70000 + 300 + 4'

# Note: All numbers will be whole numbers greater than 0.

"""
P
input = a number
output = a string
explicit = we need to return the number in its "expanded form" - so if a number is not 0, return that number in its place, plus the appropriate amount of 0s
implicit = 

E

D
strings

A
-coerce the number to a string first
-initialize final string
-iterate through the string, for i, digit in enumerate(string)
    -if digit != "0"
        - final string += digit
        - zeros = len(string) - i
        - for j in range(zeroes)
            - final string += "0"
        -final_string += "+ "
    else:
        continue
        
    return final_string[:-2]
    
C
"""

def expanded_form(num):
    num_to_string = str(num)
    final_string = ""
    
    for i, digit in enumerate(num_to_string):
        if digit != "0":
            final_string += digit
            zeros = len(num_to_string) - i
            for j in range(zeros - 1):
                final_string += "0"
            final_string += " + "
        else:
            continue
        
    return final_string[:-3]

print(expanded_form(12) ==  '10 + 2') # should return '10 + 2'
print(expanded_form(42) == '40 + 2') # should return '40 + 2'
print(expanded_form(70304) == '70000 + 300 + 4') # should return '70000 + 300 + 4'

# Second answer:

# def expanded_form(number):
    
#     num_to_string = str(number)

#     final_string = ""

#     for i, char in enumerate(num_to_string):
#         digit = int(char)
#         if digit > 0:
#             num_of_zeros = (len(num_to_string) - 1) - i
#             final_string += char + (num_of_zeros * '0') + " " + "+" + " "

#     return final_string.strip(" +")