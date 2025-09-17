# Problem 1
# Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

# When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

# The below tests should each print True.

"""
P
input = a list (of numbers)
output = a list (of numbers)
explicit = for each number in the list, figure out how many numbers in the list are smaller than that number. We should only count unique values of numbers, no repeats. 
implicit = if a list has one unique number, the returning list won't have any other numbers smaller than it, so the returned list would have a list with 0

E

D
list
set

A
-if the list has only a length of 1, return a list with 0
-else
    -coerce a copy of the list into a set
    -coerce the set back into a list
    -sort the list in ascending order

    -final list = []
    -for num in original list
        -count = 0
        -for num2 in copied list
            -if num > num2:
                count += 1
        -append count to list
    -return final list

C
"""
import copy

def smaller_numbers_than_current(lst):
    if len(lst) == 0:
        return [0]
    else:
        copy_of_lst = copy.copy(lst)
        lst_to_set = set(copy_of_lst)
        unique_list = list(lst_to_set)

        final_list = []

        for num in lst:
            count = 0
            for num2 in unique_list:
                if num > num2:
                    count += 1
            final_list.append(count)
        return final_list

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

# Second, more recent answer I had
def smaller_numbers_than_current(lst):
    final_list = []
    list_as_set = set(lst)
    
    for num in lst:
        count = 0
        for unique in list_as_set:
            if num > unique:
                count += 1
        final_list.append(count)
    
    return final_list

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)