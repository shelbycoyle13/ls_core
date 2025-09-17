# Number Guesser Part 2
# In the previous exercise, you wrote a number guessing game that determines a secret number between 1 and 100, and gives the user 7 opportunities to guess the number.

# Update your solution to accept a low and high value when you create a GuessingGame object, and use those values to compute a secret number for the game. You should also change the number of guesses allowed so the user can always win if she uses a good strategy. You can compute the number of guesses with:

# import math
# number_of_guesses = int(math.log2(high - low + 1)) + 1
# # "high" is the highest number in the range
# # "low" is the lowest number in the range

# game = GuessingGame(501, 1500)
# game.play()

# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 104
# Invalid guess. Enter a number between 501 and 1500: 1000
# Your guess is too low.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 1250
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 1375
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 80
# Invalid guess. Enter a number between 501 and 1500: 1312
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 1343
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 1359
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 1351
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 1355
# That's the number!

# You won!

# game.play
# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 1000
# Your guess is too high.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 750
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 875
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 812
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 843
# Your guess is too high.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 820
# Your guess is too low.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 830
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 835
# Your guess is too low.

# You have 2 guesses remaining.
# Enter a number between 501 and 1500: 836
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 501 and 1500: 837
# Your guess is too low.

# You have no more guesses. You lost!

# Note that a game object should start a new game with a new number to guess with each call to play.

import math
import random

class GuessingGame:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.random = random.randint(self.low, self.high)
        self.number_of_guesses = int(math.log2(self.high - self.low + 1)) + 1
        # "high" is the highest number in the range
        # "low" is the lowest number in the range

    GUESSING_MESSAGES = {
            "high" : "Your guess is too high.",
            "low" : "Your guess is too low.",
            "match" : "That's the number!"
        }
    
    END_GAME_MESSAGES = {
         "win" : "You won!",
         "lose" : "You have no more guesses. You lost!"
    }

    def play(self):

        self.reset_game()
        self.play_rounds()

    def play_rounds(self):
        while self.number_of_guesses > 0:
            self.show_guesses_remaining()
            user_guess = self.validate_guess() #Why do we now take the self prefix away?
            result = self.check_validated_guess(user_guess)
            
            if self.handle_guess_result(result): #We have to put self as a prefix here, why?
                return #If user wins, the program ends
            
            self.number_of_guesses -= 1

        print(self.__class__.END_GAME_MESSAGES["lose"])
    
        
    def reset_game(self):
        self.random = random.randint(self.low, self.high)
        self.number_of_guesses = int(math.log2(self.high - self.low + 1)) + 1
        
    def validate_guess(self):
        while True:
            try:
                guess = int(input(f"Enter a number between {self.low} and {self.high}: "))

                if self.low <= guess <= self.high:
                     return guess
                else:
                     print("Invalid guess. ", end="")
            except ValueError:
                print("Invalid input! Please enter a valid integer that is within the range.")

    def show_guesses_remaining(self):
        if self.number_of_guesses > 1:
            print(f"You have {self.number_of_guesses} guesses remaining.")
        else:
            print(f"You have {self.number_of_guesses} guess remaining.")

    def check_validated_guess(self, user_guess):
            if user_guess > self.random:
                return "high"
            elif user_guess < self.random:
                return "low"
            else:
                return "match"
            
    def handle_guess_result(self, result):
        print(self.__class__.GUESSING_MESSAGES[result]) #This syntax is the only way to access that dictionary right? And dictionaries used in general in classes?

        if result == "match":
                print(self.__class__.END_GAME_MESSAGES["win"])
                return True
        
        return False

            
game = GuessingGame(501, 1500)
game.play()
