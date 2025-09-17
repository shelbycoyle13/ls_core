# Problem 15
# Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

# The below tests should each print True.

# print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
# print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
# print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
# print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

"""
P
input = a string
output = an integer
explicit = we want to compute the greatest product of 4 consecutive digits in the string
implicit = 

E

D
strings

A
-i always want to get a slice of the string at length 4, slices do not have to start at the first index
-initialize list of substrings
-for i in range(length(string))
    -for j in range(i + 4, length(string) + 1)
    -append these slices to list


-for substring in list
    -for digit in substring
        -product = digit
        -product *= digit
        -max_product = product
        -if product > max_product
            -max_product = product
        -return max_product

C
"""

def greatest_product(string):
    substrings = []

    for i in range(len(string)):
        for j in range(i + 4, len(string) + 1):
            if len(string[i:j]) == 4:
                substrings.append(string[i:j])

    max_product = 1 # We want this max product to not reset, so it needs to stay outside of the loop completely
    for substring in substrings:
        product = 1 # This resets since it's starting over for every slice of 4 numbers
        for digit in substring:
            product *= int(digit)
        if product > max_product:
            max_product = product
            
    return max_product

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

#Second answer, almost the same, possibly easier to remember with creating the substrings:
def greatest_product(string):
    substrings = []

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 4:
                substrings.append(substring)

    greatest_product = 1

    for substring in substrings:
        current_product = 1
        for digit in substring:
            current_product *= int(digit)

        if current_product > greatest_product:
            greatest_product = current_product

    return greatest_product
