# Create a function that takes two integers as arguments. The first argument is a count, and the second is the starting number of a sequence that your function will create. The function should return a list containing the same number of elements as the count argument. The value of each element should be a multiple of the starting number.

# You may assume that count will always be an integer greater than or equal to 0. The starting number can be any integer. If the count is 0, the function should return an empty list.

# print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
# print(sequence(4, -7) == [-7, -14, -21, -28])     # True
# print(sequence(3, 0) == [0, 0, 0])                # True
# print(sequence(0, 1000000) == [])                 # True

"""
P
input = two integers
output = list
explicit = the first argument is the number of numbers in the list. the second argument is the starting number and step. if count is 0, return an empty list.
implicit = if the step is 0, all the numbers in the list will be 0 too

E
 # print(sequence(5, -2) == [-2, -4, -6, -8, -10])

D
possible loop
-> possible list comprehension

A
-first argument = count. count also happens to be the same value as the len(final_list)
-second argument = step
-last number = count * step
- final list = []
- if count == 0
    return []
- for num in range(step, last number + 1, step):
    append num to the final list

C
"""

def sequence(count, step):
    last_number = count * step
    
    if count == 0:
        return []
    
    if step == 0:
        final_list = [0 for i in range(count)]
    elif step < 0:
        final_list = [num for num in range(step, last_number - 1, step)]
    else:
        final_list = [num for num in range(step, last_number + 1, step)]
    
    return final_list

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
print(sequence(5, -2) == [-2, -4, -6, -8, -10])   # True