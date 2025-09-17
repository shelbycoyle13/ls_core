# Modify the class definition from above to facilitate the following methods. Note that there is no name= setter method now.

class Person:
    # def __init__(self, first_name="", last_name=""):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #While my solution works, here is LS' better one:

    def __init__(self, name):
        words = name.split()
        self.first_name = words[0]
        self.last_name = ""

        if len(words) > 1:
            self.last_name = words[1]

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip() #We have this incase of any whitespace entered by user
    
    ### Yes, even though you get the correct answers with just the above code, you still need to put getters and setters for the first and last name.
    
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


bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

# Hint: let first_name and last_name be "states" and create a property that uses those states.