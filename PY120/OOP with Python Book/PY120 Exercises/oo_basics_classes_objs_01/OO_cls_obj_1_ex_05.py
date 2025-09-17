# Hello, Sophie! (Part 1)
# Using the code from the previous exercise, add a parameter to __init__ that provides a name for the Cat object. Use an instance variable to print a greeting with the provided name. (You can remove the code that displays I'm a cat!.)

class Cat:
    def __init__(self, name):
        self.name = name #While this code works without this line, we need this instance variable to access object data across different methods, allowing other objects to interact with yours, and we want to maintain state throughout the object's lifecycle
        print(f"Hello! My name is {self.name}!") #We want to practice using the instance variable in the f-string rather than the parameter (yes, it's the parameter if you just use name! This makes it clearer we're using the object's property and provides consistency, especially if the method becomes more complex later.)

kitty = Cat('Sophie') #Hello! My name is Sophie!