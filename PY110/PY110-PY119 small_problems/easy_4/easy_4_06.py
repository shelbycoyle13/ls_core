# Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.

# # All of these examples should print True
# print(leading_substrings('abc') == ['a', 'ab', 'abc'])
# print(leading_substrings('a') == ['a'])
# print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

"""
P
input = a string
output = a list of substrings
explicit = we're always starting each substring with the first letter of the word
implicit = the last element in the list is the same as the string we are passing in as an argument

E
# print(leading_substrings('wowza') == ['w', 'wo', 'wow', 'wowz', 'wowza'])
# "w" = string[0:1]
# "wo" = string[0:2]
# "wow" = string[0:3]
...
# "wowza" = string[0:5]

D
strings
lists
loops

A
-we want to iterate through the stop number of the slice of the string
-the last stop number should be the length of the string
-for stop_number in range(1, len(string)):
    substring = string[0:stop_number]
    -add these substrings to a new list
-return the list

C
"""
def leading_substrings(string):
    list_of_substrings = []

    for stop_number in range(1, len(string) + 1):
        substring = string[0:stop_number]
        list_of_substrings.append(substring)
    return list_of_substrings

print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
print(leading_substrings('wowza') == ['w', 'wo', 'wow', 'wowz', 'wowza'])