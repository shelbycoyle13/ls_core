class Person:

    def __init__(self, first, last):
        self._validate_and_set_names(first, last)

    def _validate_and_set_names(self, first, last):
        
        
        if not first:
            raise ValueError("You must enter a first name!")
        if not first.isalpha():
            raise TypeError("First name must consist of letters only.")

        
        if not last:
            raise ValueError("You must enter a last name!")
        if not last.isalpha():
            raise TypeError("Last name must consist of letters only.")
        
        self.first = first
        self.last = last

    @property
    def name(self):
        first = self.first.title()
        last = self.last.title()
        return f"{first} {last}"

    @name.setter
    def name(self, name):
        first, last = name
        self.first = first
        self._validate_and_set_names(first, last)

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.