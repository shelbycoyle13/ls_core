# Complete the Program - Cats!
# Consider the following program.

class Pet:
    def __init__(self, name, age, colors):
        self._name = name
        self._age = age
        self._colors = colors

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @property
    def colors(self):
        return self._colors

class Cat(Pet):
    
    @property
    def info(self):
        return f"My cat {self._name} is {self._age} years old and has {self._colors} fur."

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

# Update this code so you see the following output when you run the code:

# My cat Cocoa is 3 years old and has black fur.
# My cat Cheddar is 4 years old and has yellow and white fur.