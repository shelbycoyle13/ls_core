#4. What is the method resolution order and why is it important?

#In general, the method resolution order is the order in which the code is run when it involves inheritance and a hierarchy. Specifically, it is when Python is searching for methods that are called on by objects. It's important because it shows us what eventually runs using what class, and can show us the "trail" of the classes in case we need to know.

#If we wanted to find the MRO, we can use the MRO method. 

# Ex: print(Bulldog.mro())

# [<class '__main__.Bulldog'>, <class '__main__.Dog'>, <class
#'__main__.Pet'>, <class 'object'>]


#If we wanted to make this more readable, we can use a list comprehension:

# print([ cls.__name__ for cls in Bulldog.mro() ])

# ['Bulldog', 'Dog', 'Pet', 'object']

# Note: the MRO method returns a list!