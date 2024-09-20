# How would you verify whether the data structures assigned to the variables numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(isinstance(numbers, list))
print(isinstance(table, list))

#Using type() is ok, but not the best answer. This is because type() checks for custom subclasses, which may have methods that would make the object no just a list anymore.