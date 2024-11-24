# Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True

"""
P
input = integer
output = integer
explicit = all integers are positive. integers will be reversed.
implicit = if we have any leading integers that are 0, return the final number without them

E
# print(reverse_number(23000) == 32)      # True

D
possibly a for loop

A
- convert the integer to a string
- reverse the string
- initialize an empty final string
- for every char in string
    - if string starts with 0
        - skip it
    - concatenate to final string
- return the remaining string as an integer
C
"""

def reverse_number(num):
    reverse_string = "".join(reversed(str(num)))

    final_string = ""
    for char in reverse_string:
        if char == "0":
            continue
        final_string += char
    return int(final_string)


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True