# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

def stringy(integer):
    new_string = ""
    for i in range(0, integer):
        if i % 2 == 0:
            new_string += "1"
        elif i % 2 == 1:
            new_string += "0"
        else:
            return "You did not enter a positive integer."
    return new_string


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True