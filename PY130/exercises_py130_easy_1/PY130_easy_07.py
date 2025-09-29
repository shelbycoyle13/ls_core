# Nested Generator Expressions
# Use nested generator expressions to create a flat list of numbers from a list of lists.

big_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

clean_list = list((num for small_lst in big_list for num in small_lst))

print(clean_list)