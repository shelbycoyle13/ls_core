# Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

def short_long_short(str1, str2):
    if len(str1) < len(str2):
        short = str1
        long = str2
    else:
        short = str2
        long = str1

    return short+long+short

# print(short_long_short("hi", "hello"))
# print(short_long_short("blah", "ha"))
# print(short_long_short("", "jello"))

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")