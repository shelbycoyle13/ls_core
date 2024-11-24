# Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on the English word for each number:
#     zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
#                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

# print(alphabetic_number_sort(input_list) == expected_result)
# # Prints True

"""
P
input = a list of integers 0-19
output = a list of integers 0-19, but sorted alphabetically based on their word
explicit = 
implicit = directions don't say we can't return a new list instead of mutating the original

E
see above

D
dictionary / tuple
list

A
-create another list that has the respective word for each number
-use the zip() function to create tuples with the input list and the alpha list
-use a helper function to create a custom sorting key to sort alphabetically
-use tuple unpacking to only return the numbers in a new list
-return the new list

C
"""

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

def alphabetic_number_sort(lst):
    numbers_and_words = list(zip(input_list, words))

    def sort_by_words(pair):
        num, word = pair
        return word, num

    sorted_by_words = sorted(numbers_and_words, key=sort_by_words)

    list_sorted_nums = [num for num, word in sorted_by_words]

    return list_sorted_nums

print(alphabetic_number_sort(input_list) == expected_result) # Prints True