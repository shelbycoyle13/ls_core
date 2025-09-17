# Method Resolution Path (Part 3)
# Using the code below, determine the method resolution order used when invoking bird1.color. Only list the classes or mix-ins that Python will check when searching for the color method. Do not use the mro method.

class FlyingMixin:
    def fly(self):
        return "I'm flying!"

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(FlyingMixin, Animal):
    pass

bird1 = Bird('Red')
print(bird1.color) # MRO = Bird, FlyingMixin, Animal, object