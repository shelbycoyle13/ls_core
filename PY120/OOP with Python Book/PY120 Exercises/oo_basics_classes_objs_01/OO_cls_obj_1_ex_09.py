# Setter
# Using the code snippet provided below, add a setter method named name. Then, rename kitty to 'Luna' and invoke greet again.

class Cat:
    def __init__(self, name):
        self.name = name #We change this back to not using the _ so as to trigger the setter method to use for our initialization process

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name): #Best to use a different parameter name than just "name"
        self._name = new_name

    def greet(self):
        print(f"Hello! My name is {self.name}!") #This calls the getter method (called name)

kitty = Cat('Sophie')
kitty.greet() #Hello! My name is Sophie!
kitty.name = "Luna"
kitty.greet() #Hello! My name is Luna!