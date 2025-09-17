# Colorful Cat
# Create a class named Cat that prints a greeting when the greet instance method is invoked. The greeting should include the name and color of the cat. Use a class constant to define the color.

class Cat:
    COLOR = "purple"

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a {Cat.COLOR} cat!") #We need to have the class call the class constant. It's preferred to use the class name directly!

kitty1 = Cat("Sophie")

kitty1.greet()

# Hello! My name is Sophie and I'm a purple cat!