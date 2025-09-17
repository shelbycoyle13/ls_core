# 5. Continuing with our Person class definition, what do you think the following code prints?

# bob = Person('Robert Smith')
# print(f"The person's name is: {bob}")

# It prints out The person's name is: <__main__.Person object at 0x100385f90>

# Python calls the str function on the expression between the {} . Every object in Python responds to the str function, which, by default, is inherited from the object class. The output represents the object's place in memory.

# We need to override the str function's behavior, or we would need to use bob.name instead.

# Now, let's override the str function for Person objects by defining a magic method, __str__, in the Person class:

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()
    
    @name.setter
    def name(self, name):
        self._name = name
        words = name.split()
        self.first_name = words[0]
        self.last_name = ""

        if len(words) > 1:
            self.last_name = words[1]
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

# Now, what does the below output?

bob = Person('Robert Smith')
print(f"The person's name is: {bob}") #The person's name is: Robert Smith