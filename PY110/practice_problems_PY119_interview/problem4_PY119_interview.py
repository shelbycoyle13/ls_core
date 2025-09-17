# Problem 4
# Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

# The below tests should each print True.

"""
P
input = a list (of integers)
output = a tuple (of two integers that are closest together in value)
explicit = if there are multiple pairs that are equally close, return the pair that occurs first in the list
implicit = 

E

D
lists
tuple

A
-high level: compare each number in the list against other numbers in the list. record the (absolute) difference. whichever pair of numbers has the smallest difference, return the (first) pair.

-for every number in the list
    -min difference = 100
    -for i in range(1, length of list)
        -subtract with the next number list[i], and the next one...get difference. abs(num - list[i]) = difference
        -if difference < min-difference:
            -difference = min-difference
            -pair1 = num
            -pair2 = list[i]
    
-return (pair1, pair2)

C
"""

def closest_numbers(lst):
    min_difference = float("inf") #This is best to use when you need the biggest number possible
    pair1, pair2 = None, None #Best to initialize pair variables to None; this makes it clear they don't hold value yet. If a list has less than 2 numbers, this also can prevent an error down the line

    for i, num in enumerate(lst):
        for j in range(i + 1, len(lst)): #Using i + 1 makes it so we don't revist pairs we already calculated the difference for
            current_difference = abs(num - lst[j])
            if current_difference < min_difference:
                min_difference = current_difference
                pair1, pair2 = num, lst[j]

    return (pair1, pair2)

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# Second more recent but similar answer (a little cleaner than the above):

def closest_numbers(lst):
    min_diff = float("inf")
    
    for i in range(len(lst)): #Using slicing to get the first number
        for j in range(i + 1, len(lst)): #Using slicing to get the second number we want to compare with
            diff = abs(lst[i] - lst[j]) #Here's the difference between the two numbers

            if diff < min_diff: #If the current difference is less than the difference variable, which is the biggest number, currently,
                min_diff = diff #Then reset the min_diff to the value of the current diff
                pair = (lst[i], lst[j]) #The pair / tuple that we need is the same as those current elements that fit our conditional

    return pair