# 24. Generate Hashtags
# Write a function `generate_hashtag(s)` that generates a hashtag from the given string `s`.

# Rules:
# - The hashtag must start with a '#' symbol.
# - All words in the hashtag must start with a capital letter.
# - If the resulting hashtag is longer than 140 characters, the function should return `False`.
# - If the input string or the resulting hashtag is an empty string, the function should return `False`.

# Examples:
# generate_hashtag("")                       # should return `False`
# generate_hashtag(" " * 200)                # should return `False`
# generate_hashtag("Do We have A Hashtag")   # should return "#DoWeHaveAHashtag"
# generate_hashtag("Nice To Meet You")       # should return "#NiceToMeetYou"
# generate_hashtag("this is a test")         # should return "#ThisIsATest"
# generate_hashtag("this is a very long string" + " " * 140 + "end")  # should return "#ThisIsAVeryLongStringEnd"
# generate_hashtag("a" * 139)                # should return "#A" + "a" * 138
# generate_hashtag("a" * 140)                # should return `False`


"""
P
input = a string
output = a string or a Boolean
explicit = we want to turn the string into a Hashtag - starts with #, all words are capitalized for the first letter. If the hashtag > 140 char in length, return Fakse. Empty string arguments return False as well.
implicit = For any arguments that include strings * an integer, only the first letter has to be capitalized + lowercase letter * remaining integers left

E

D
strings

A
if len(string) == 0:
    return False
else
    words = string.split()

final_string = "#" + .join(words)

return final_string

C
"""
def generate_hashtag(string):
    stripped_string = string.strip() #We want to get rid of leading and trailing whitespace - this turns a string that's entirely whitespace into an empty string

    if not stripped_string: #If this string is falsy, i.e. if it's empty:
        return False
    else:
        words = string.split()

    capitalized_first_letter = [word.title() for word in words]

    final_string = "#" + ''.join(capitalized_first_letter)

    if len(final_string) > 140:
        return False

    return final_string  

print(generate_hashtag("") == False)                  # should return `False`
print(generate_hashtag(" " * 200) == False)                # should return `False`
print(generate_hashtag("Do We have A Hashtag") == "#DoWeHaveAHashtag")   # should return "#DoWeHaveAHashtag"
print(generate_hashtag("Nice To Meet You") == "#NiceToMeetYou")       # should return "#NiceToMeetYou"
print(generate_hashtag("this is a test") == "#ThisIsATest")         # should return "#ThisIsATest"
print(generate_hashtag("this is a very long string" + " " * 140 + "end") == "#ThisIsAVeryLongStringEnd")  # should return "#ThisIsAVeryLongStringEnd"
print(generate_hashtag("a" * 139) == "#A" + "a" * 138)                # should return "#A" + "a" * 138
print(generate_hashtag("a" * 140) == False)                # should return `False`