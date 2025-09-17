# Problem 9
# Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

# You may assume that the second argument is never an empty string.
# The below tests should each print True.

"""
P
input = two strings
output = an integer
explicit = we are returning the number of times the second string occurs in the first. overlapping strings don't count
implicit = 

E

D
strings

A
-return str1.count(str2)

C
"""
def count_substrings(str1, str2):
    return str1.count(str2)

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)