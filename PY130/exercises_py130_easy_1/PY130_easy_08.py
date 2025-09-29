# Reverse String
# Use a generator expression to yield each character of a string in reverse order.

string1 = "apple"

backwards = (letter for letter in string1[::-1])

for letter in backwards:
    print(letter)

#LS Solution:
# string = "Hello"

# reverse_generator = (string[i] for i in range(len(string) - 1, -1, -1))

# for char in reverse_generator:
#     print(char)

# Discussion
# In this exercise the generator expression (string[i] for i in range(len(string) - 1, -1, -1)) is used to iterate over each character of a given string in reverse order.

# As we've learned, the range function can take up to three arguments, start, stop and step:

# start = len(string) - 1: This is the index of the last character in the string.
# stop = -1: This is the point where the range stops. In Python, the range includes values up to, but not including, the stop value. By setting stop to -1, we ensure that the range includes the index 0, which is the first character of the string.
# step = -1: This indicates the increment (or in this case, decrement) between each number in the range. A step of -1 means that the range will decrease by 1 with each step, effectively counting backwards.