# Method Resolution Path (Part 2)
# Using the code below, determine the method resolution order (MRO) when accessing cat1.color. Only list the classes and mix-ins Python will check when searching for the color method. Do not use the mro method.

class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
cat1.color #I would say the MRO = Cat, Animal, object, but it looks like the last line of code is missing (), so this would raise an error.