# You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.

# def reverse_string(string):
#     for char in string:
#         string = char + string #This line adds the current char in the string and concatenates it with the rest of the string

#     return string

# print(reverse_string("hello") == "olleh")

def reverse_string(string):
    new_string = string[::-1]
    return new_string

reverse_string("hello")
print(reverse_string("hello") == "olleh")