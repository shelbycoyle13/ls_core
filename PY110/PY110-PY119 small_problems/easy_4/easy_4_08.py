# Write a function that returns a list of all palindromic substrings of a string. That is, each substring must consist of a sequence of characters that reads the same forward and backward. The substrings in the returned list should be sorted by their order of appearance in the input string. Duplicate substrings should be included multiple times.

# You may (and should) use the substrings function you wrote in the previous exercise.

# For the purpose of this exercise, you should consider all characters and pay attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.

# print(palindromes('abcd') == [])                  # True
# print(palindromes('madam') == ['madam', 'ada'])   # True

# print(palindromes('hello-madam-did-madam-goodbye') ==
#                   [
#                       'll', '-madam-', '-madam-did-madam-',
#                       'madam', 'madam-did-madam', 'ada',
#                       'adam-did-mada', 'dam-did-mad',
#                       'am-did-ma', 'm-did-m', '-did-',
#                       'did', '-madam-', 'madam', 'ada', 'oo',
#                   ])    # True

# print(palindromes('knitting cassettes') ==
#                   [
#                       'nittin', 'itti', 'tt', 'ss',
#                       'settes', 'ette', 'tt',
#                   ])    # True

"""
P
input = string
output = list of substrings
explicit = duplicate substrings are allowed. case matters. single characters are not palindromes.
implicit = if a string has no palindromes, we return an empty list. made up words / substrings are considered palindromes.

E
# print(palindromes('racecar') == ['racecar', 'aceca', 'cec'])   # True

D
strings
lists

A
-we are allowed to use our substring function from the previous exercise. this being said:
-first, we want to have a function that checks to make sure that a word is more than one character AND the string is the same forwards and backwards. We'll check using len() and with a slice of a string returned in reverse
-we can use another function to return the list comprehension. for this we will iterate through all of the substrings that are returned through the substrings function. If the substrings are truthy after passing through the check if they're a palindrome, we will return them.

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


def is_palindrome(string):
    return len(string) > 1 and string == string[::-1]

def palindromes(s):
    return [substring 
            for substring in substrings(s)
            if is_palindrome(substring)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

print(palindromes('racecar') == ['racecar', 'aceca', 'cec'])   # True