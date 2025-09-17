# Let's create a few more methods for our Dog class.

class Pet: #Best to just create a superclass called Pet to sort out the methods appropriately
    def speak(self): #We should put this because all pets speak; we can always override this in our subclasses
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'


class Dog(Pet):
    def speak(self):
        return 'bark!'
    
    def fetch(self):
        return 'fetching!'
    
class Bulldog(Dog):
    def sleep(self):
        return "snoring!"
    
class Cat(Pet):
    def speak(self):
        return 'meow!'

    
# Create a new class called Cat, which can do everything a dog can, except fetch. Assume the methods do the exact same thing. Hint: don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.

pet = Pet()
dave = Dog()
bud = Bulldog()
kitty = Cat()

print(pet.run())              # running!
print(kitty.run())            # running!
print(kitty.speak())          # meow!
try:
    kitty.fetch()
except Exception as exception: #This handles the situation when a method can't be found in a class
    print(exception.__class__.__name__, exception, "\n")
    # AttributeError 'Cat' object has no attribute 'fetch'

print(dave.speak())           # bark!

print(bud.run())              # running!
print(bud.sleep())             # "snoring!"