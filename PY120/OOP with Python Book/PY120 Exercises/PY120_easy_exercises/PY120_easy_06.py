# Pet Shelter
# Consider the following code:

class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def intro(self):
        return f"a {self.species} named {self.name}"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_collection = [] #We're going to initialize an empty list here. Makes sense - new owner, empty list

    def add_pet(self, pet): #Does this pet parameter come from the adopt method? Where does the value originate? LS Bot: Yes, the pet parameter in add_pet comes from the adopt method call. The value originates from the pet objects created in the test code (like cocoa, cheddar, etc.)
        self.pet_collection.append(pet)

    def number_of_pets(self):
        return len(self.pet_collection)
    
    def print_pet_collection(self):
        for pet in self.pet_collection:
            print(pet.intro())

class Shelter:
    def __init__(self):
        self.owners = {} #Empty dictionary to keep track of owners. Owners will never be duplicated using a dictionary.

    def adopt(self, owner, pet): #Here we just put general parameter names like normal that represent the objects that will be used as arguments. LS Bot: Your understanding of how parameters work is correct - they're just placeholders that receive the actual objects when methods are called
        owner.add_pet(pet)
        if owner.name not in self.owners:
            self.owners[owner.name] = owner #Key = owner name, value = object variable name

    def print_adoptions(self):
        for name, owner in self.owners.items():
            print(f"{name} has adopted the following pets:")
            owner.print_pet_collection()
            print("")

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

# Write the classes and methods that will be necessary to make this code run, and log the following output:

# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.

# The order of the output does not matter, so long as all of the information is presented.