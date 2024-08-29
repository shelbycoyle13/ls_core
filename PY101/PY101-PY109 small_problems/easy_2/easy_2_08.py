# Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

def oddities(lst):
    odd_list = []
    for index in range(len(lst)):
        if index % 2 == 0:
            odd_list.append(lst[index])
    return odd_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

# Bonus question: Try to solve the problem using list slicing.

def oddities(lst):
    return lst[::2]

# Further Exploration
# Write a companion function that returns the 2nd, 4th, 6th, and so on elements of a list.

# Try to solve this differently from the exercise described above.

# def even_elements(lst):
#     return lst[1::2]

def even_elements(lst):
    even_list = []
    i = 1
    while i < len(lst):
        if i % 2 == 1:
            even_list.append(lst[i])
        i += 1
    return even_list

print(even_elements([2, 3, 4, 5, 6]))