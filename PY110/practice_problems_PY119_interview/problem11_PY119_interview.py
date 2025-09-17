# """
# Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k. The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

# You may assume that the string argument consists entirely of lowercase alphabetic letters.
# """

# print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
# print(repeated_substring('xyxy') == ('xy', 2))
# print(repeated_substring('xyz') == ('xyz', 1))
# print(repeated_substring('aaaaaaaa') == ('a', 8))
# print(repeated_substring('superduper') == ('superduper', 1))

"""
P
input = a string
output = a tuple (a string, an integer)
explicit = string =  shortest substring * largest integer
implicit = 

E

D
strings
tuples

A
-We know that no substring can repeat more times than the length of the string, divided by 2, so let's save that value to a variable
-we want to have an integer to use for slicing, so let's iterate through a range starting at 1 and ending at the length of the string, divided by 2, plus 1, since we want that final integer inclusive. This will give us all of the substrings, starting with the first character, always
-we want to utilize that formula given to us in the directions of the problem, so we'll reverse it. if the substring we have * the length of the substring divided by the current index == string and the length of the string divided by the index has 0 remainder, then we want to return that substring, length // i

C
"""

def repeated_substring(string):

    length = len(string)

    for i in range(1, (length // 2) + 1): #We're using this for the stop index of the slicing
        substring = string[:i]

        if substring * (length // i) == string and length % i == 0: #Reversing the logic of the formula given to us
            return (substring, length // i)

    return (string, 1) #If the above doesn't work, return the entire string, repeat count of only 1
        
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

#Second, more recent answer. This may be easier to remember:
def repeated_substring(string):
    string_length = len(string)

    for substring_length in range(1, string_length + 1): #Try all possible substring lengths
        if string_length % substring_length == 0: #We need to be able to find the substring length first, see which is evenly divisible
            substring = string[:substring_length] #Substring_length here also happens to work well as a stop number
            repeat_count = string_length // substring_length 
            if substring * repeat_count == string: #This is the same as the formula given to us
                return (substring, repeat_count)
    
    return (substring, 1)