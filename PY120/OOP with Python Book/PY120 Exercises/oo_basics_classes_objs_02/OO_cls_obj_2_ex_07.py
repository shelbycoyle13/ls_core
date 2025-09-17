# Identify Yourself (Part 2)
# Update the following code so that it prints I'm Sophie! when it invokes print(kitty).

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name #getter looks the same
    
    def __str__(self): #We can override the string method for any class to produce the desired output.
        return f"I'm {self.name}!"

# Comments show expected output
kitty = Cat('Sophie')
print(kitty)        # I'm Sophie! #When print runs, it calls the string method on the object passed through to get a string representation of the object.