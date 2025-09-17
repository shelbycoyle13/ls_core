# Problem 2
# Create a function that takes a list of integers as an argument. The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return None.
# The above tests should each print True.

"""
P
input = a list (of integers)
output = an integer (the minimum sum of 5 consecutive numbers in the list)
explicit = if the list length is fewer than 5, the function returns None
implicit = it doesn't matter where the first integer starts, we just have to have 5 consective numbers. return the smallest sum

E

D
lists (nested)

A
- sum_list = []
-for num in range(len(list))
    -for num2 in range(i + 4, len(list2))
        - sum_list.append(sum(num))

- return min(sum_list)

C
"""
def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    current_sum = sum(lst[:5])
    min_sum = current_sum

    for i in range(5, len(lst)):
        current_sum = current_sum - lst[i - 5] + lst[i]
        min_sum = min(current_sum, min_sum)

    return min_sum
        
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

# Second, but more recent answer (I like this one better)

def minimum_sum(lst):
    list_of_sums = []
    if len(lst) < 5:
        return None # We can remember the number we subtract from our length - we want to take the amount of elements we NEED - 1, so 5-1 = 4. Length - "magic number"
    else:
        for i in range(len(lst) - 4): # We want to make sure our start number in the slice stops so we always end up with 5 integers in our sum and not less
            list_of_sums.append(sum(lst[i: i + 5])) # Here is the "sliding" sum. Don't forget we can use sum() with a list!
    
    return min(list_of_sums)
