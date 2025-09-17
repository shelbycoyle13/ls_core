# 4. Using the class definition from problem 3, let's create some more people (Person objects):

# bob = Person('Robert Smith')
# rob = Person('Robert Smith')

# Without adding any code to the Person class, we want to compare bob and rob to see whether they both have the same name. How can we make this comparison?

class Person:
    def __init__(self, name):
        self.name = name

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

bob = Person('Robert Smith')
rob = Person('Robert Smith')
print(bob.name == rob.name) # We have to use the name property here to directly compare their names and not the objects themselves. We know name is a property because we're invoking the getter method that has the property decorator