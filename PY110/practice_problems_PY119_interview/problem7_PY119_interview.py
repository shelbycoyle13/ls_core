# Problem 7
# Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

# If the list is empty or contains exactly one value, return 0.

# If a certain number occurs more than twice, count each complete pair once. For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

# The below tests should each print True.

"""
P
input = a list (of integers)
output = an integer (that represents the number of pairs)
explicit = for an empty list or if there's only one value / integer, return 0
implicit = numbers cannot overlap, once a number has been counted in a pair, we cant use it again

E

D
list

A
-initialize empty dict
-iterate over list, for num in list
    -if num not in dict
        -dict[num] = 1
    -else
        -dict[num] += 1
    
    


C
"""

def pairs(lst):
    numbers_dict = {}
    pairs_count = 0

    for num in lst:
        if num not in numbers_dict:
            numbers_dict[num] = 1
        else:
            numbers_dict[num] += 1
    
    for value in numbers_dict.values():
        pairs_count += value // 2 # Divide the total value of the count by 2, using floor division and add this to the count
    
    return pairs_count
        

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

#Second, more recent answer, which I think I like better:

def pairs(lst):
    if len(lst) <= 1:
        return 0
    
    pairs_count = 0

    for num in set(lst):
        pairs_count += lst.count(num) // 2

    return pairs_count

# Third, probably the easiest and most succinct answer (almost the same as second, even cleaner):

def pairs(lst):
    pair_count = 0

    for num in set(lst):
        pair_count += lst.count(num) // 2
    
    return pair_count