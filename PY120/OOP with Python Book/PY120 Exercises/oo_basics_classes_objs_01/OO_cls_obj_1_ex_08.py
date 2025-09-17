# Getter
# Using the code snippet provided below, add a getter method named name and invoke it in place of self._name in greet.

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!") #The property method allows us to access the method like an attribute, without calling it like a method with ()


kitty = Cat('Sophie')
kitty.greet() #Hello! My name is Sophie!