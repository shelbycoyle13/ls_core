# Animals
# Given the following Animal class, create two more classes, Cat and Dog, that inherit from it:

class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")
    

class Cat(Animal):
    def __init__(self, name, age, status): #Parameters accepted for cats only
        super().__init__(name, age, 4, "cat", status) #We need to make this match the Animal's parameters, "cat" needs to be a string

    def introduce(self):
        return super().introduce() + " "+ "Meow meow!"

class Dog(Animal):
    def __init__(self, name, age, status, owner): #Parameters accepted for dogs only
        super().__init__(name, age, 4, "dog", status) #We need to make this match the Animal's parameters, "dog" needs to be a string, no reason to add the owner parameter here since Animal doesn't use it
        self.owner = owner # However, we do add self.owner here in the Dog initializer because it's the only class that uses it

    def introduce(self):
        return super().introduce() + " "+ "Woof! Woof!"
    
    def greet_owner(self):
        return f"Hi {self.owner}! Woof! Woof!"
    

# The Cat initializer should accept 3 parameters: name, age, and status. Cats should always have a leg count of 4 and a species of "cat". The introduce method for the Cat class should return a string identical to the base class with an added Meow meow! at the end. For example:

cat = Cat("Pepe", 4, "happy")
expected = ("Hello, my name is Pepe and I am 4 years old "
            "and happy. Meow meow!")
print(cat.introduce() == expected)      # True

# The Dog initializer should accept 4 parameters: name, age, status, and owner. Dogs should always have a leg count of 4 and a species of "dog". In addition to the methods inherited from Animal, the Dog class should have a greet_owner method that returns a greeting to its owner followed by Woof! Woof!. The introduce method for the Dog class should return a string identical to the base class with an added Woof! Woof! at the end.

dog = Dog("Bobo", 9, "hungry", "Daddy")
expected = ("Hello, my name is Bobo and I am 9 years old "
            "and hungry. Woof! Woof!")
print(dog.introduce() == expected)                  # True
print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True