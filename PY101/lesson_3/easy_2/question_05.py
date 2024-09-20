# How would you verify whether the data structures assigned to the variables numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# This answer is good, but this can cause potential issues if there are custom classes involved. If there are, then it wouldn't be considered a plain list anymore.
print(type(numbers))
print(type(table))

# This is preferred.
print(isinstance(numbers, list))
print(isinstance(table, list))