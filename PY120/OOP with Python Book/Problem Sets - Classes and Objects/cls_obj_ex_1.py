# Given the following code, create the Person class needed to make the code work as shown:

class Person:
    def __init__(self, name):
        self.name = name

    ###Should add the properties - the getter and setter. Properties become important for implementing features such as validation or computed attributes

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert