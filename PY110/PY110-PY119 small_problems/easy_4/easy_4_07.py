# Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

# You may (and should) use the leading_substrings function you wrote in the previous exercise:

# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]

# print(substrings('abcde') == expected_result)  # True

"""
P
inputs = a string
outputs = a list of all substrings
explicit = order of the returned list goes in order by the starting index substrings
implicit = we can use the previous exercise's answer to solve this one

E
# print(substrings('jam') == expected_result)  # True
# expected_result = ["j", "ja", "jam", "a", "am", "m"]

"a" = string[1:2]
"am" = string[1:3 = length of the string]
"m" = string[2:3 = length of the string]

# print(substrings('jam') == expected_result)

D
strings
lists
loops

A
-now we are iterating through the start number as well as the stop number when doing slices
-we can make a nested list comprehension that first iterates through the starting numbers as the outer loop
    -the inner loop iterates through the substrings from the outer loop (it uses the previous function to accomplish this)
-we want to return the substrings in this nested list comprehension
-return this nested list comprehension

C
"""

def leading_substrings(string):
    list_of_substrings = []

    for stop_number in range(1, len(string) + 1):
        substring = string[0:stop_number]
        list_of_substrings.append(substring)
    return list_of_substrings


def substrings(string):
    list_of_substrings = [substring for start_number in range(len(string))
                                    for substring in leading_substrings(string[start_number:])
                            ]
    return list_of_substrings


# expected_result = [
#     "a", "ab", "abc", "abcd", "abcde",
#     "b", "bc", "bcd", "bcde",
#     "c", "cd", "cde",
#     "d", "de",
#     "e",
# ]

# print(substrings('abcde') == expected_result)  # True


# expected_result = ["j", "ja", "jam", "a", "am", "m"]
# print(substrings('jam') == expected_result)  # True
