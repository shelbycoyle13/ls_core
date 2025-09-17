# Problem 10
# Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

# If a substring occurs more than once, you should count each occurrence as a separate substring.

# The below tests should each print True.

"""
P
input = a string
output = an integer
explicit = we want to get the amount of substrings that are "even numbers" (but they're strings)
implicit = 

E

D
strings

A
high-level:
    1) get all possible substrings and put them in a list
    2) for each substring in list, coerce to a number
    2.5) initialize empty numbers list
    3) if number is even, add to a separate list
    4) return the length of the list

-initialize empty substring list
-for i in range(len(string))
    -for j in range(i + 1, len(string) + 1)
        append substring to substring list

-for substring in substring list
    -int(substring)
    -append to numbers list

-for number in numbers list
    -if number is even
        -append to even numbers list

-return length of even numbers list


C
"""
def even_substrings(string):
    substrings = []
    numbers = []
    even_numbers = []

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])

    for substring in substrings:
        numbers.append(int(substring))
    
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    
    return len(even_numbers)

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

#Second, more recent answer, that is cleaner:
def even_substrings(string):
    substrings = []
    for i in range(len(string)): #start
        for j in range(i + 1, len(string) + 1): #stop
            substrings.append(string[i:j])

    count = 0

    for substring in substrings:
        if int(substring) % 2 == 0:
            count += 1

    return count

#Third answer, probably the cleanest
def even_substrings(string):

    all_substrings = []
    
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            all_substrings.append(substring)

    all_numbers = [int(substring) for substring in all_substrings]

    even_numbers = [num for num in all_numbers if num % 2 == 0]

    return len(even_numbers)