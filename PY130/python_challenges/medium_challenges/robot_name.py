import string
import random

class Robot:
    ALPHABET = string.ascii_uppercase
    NUMBERS = string.digits
    _names = set()

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if self._name is None:
            while True:
                potential_name = self._generate_name()
                if potential_name not in Robot._names:
                    break
            self._name = potential_name
            Robot._names.add(self._name)
        return self._name
        
    #Generate a new name
    def _generate_name(self):
        new_name = ""
        two_random_letters = random.choices(Robot.ALPHABET, k=2)
        three_random_digits = random.choices(Robot.NUMBERS, k=3)
        
        return new_name.join(two_random_letters + three_random_digits)

    def reset(self):
        Robot._names.discard(self._name)
        self._name = None