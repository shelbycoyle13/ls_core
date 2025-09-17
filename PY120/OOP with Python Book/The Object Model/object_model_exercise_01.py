# How do we create a class and an object in Python?

# To create a class, we use similar syntax as if we were defining a function. It looks like:
class Greet:
    pass

# We would need to use the __init__ method in order to initialize an object.
# Once we call a class constructor, the class will use __init__ to then create an object. For example:

spanish = Greet()

# Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

# What class you create doesn't matter, provided it satisfies the above requirements.

class Greet:
    
    def __init__(self, language):
        self.language = language
        print(f"Constructor for {self.language}")

spanish = Greet("Spanish")
japanese = Greet("Japanese")
