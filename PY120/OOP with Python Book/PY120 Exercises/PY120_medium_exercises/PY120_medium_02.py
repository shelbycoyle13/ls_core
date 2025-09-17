# Number Guesser Part 1
# Create an object-oriented number guessing class for numbers in the range 1 to 100, with a limit of 7 guesses per game. The game should play like this:

# game = GuessingGame()
# game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

# game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!

# Note that a game object should start a new game with a new number to guess with each call to play.

#First draft - LS Bot feedback: Your solution demonstrates a solid understanding of the basic requirements! I'd recommend focusing on these key areas:

# Input validation robustness: Wrap your int(input()) calls in try-except blocks to handle non-numeric input, and ensure range validation happens on every guess attempt.

# Game state reset: Consider adding a method to reset the game state (new random number, reset guess count) that gets called at the start of each play() call.

# Method extraction: Break down the play method into smaller helper methods like get_valid_guess(), check_guess(), and display_result(). This will make your code more readable and easier to test.

# Instance variable naming: Consider using more descriptive names like remaining_guesses instead of guesses, and secret_number instead of random.

# import random

# class GuessingGame:
#     def __init__(self):
#         self.guesses = 7
#         self.random = random.randint(1, 100)

#     def play(self):
#         print(f"You have {self.guesses} guesses remaining.")
#         self.user_guess = int(input("Enter a number between 1 and 100: "))

#         while self.user_guess < 1 or self.user_guess > 100:
#             print("Invalid guess.")
#             self.user_guess = int(input("Enter a number between 1 and 100: "))
        
#         while self.user_guess != self.random:
#             if self.user_guess > self.random:
#                 print("Your guess is too high.")
#                 self.guesses -= 1
#                 if self.guesses == 0:
#                     print("You have no more guesses. You lost!")
#                     return
#                 print(f"You have {self.guesses} guesses remaining.")
#                 self.user_guess = int(input("Enter a number between 1 and 100: "))
#             elif self.user_guess < self.random:
#                 print("Your guess is too low.")
#                 self.guesses -= 1
#                 if self.guesses == 0:
#                     print("You have no more guesses. You lost!")
#                     return
#                 print(f"You have {self.guesses} guesses remaining.")
#                 self.user_guess = int(input("Enter a number between 1 and 100: "))

#         print("That's the number!")
#         print("")
#         print("You won!")

# game = GuessingGame()
# game.play()

import random

class GuessingGame:
    def __init__(self):
        self.guesses = 7
        self.random = random.randint(1, 100)

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
        while self.guesses > 0:
            self.show_guesses_remaining()
            self.user_guess = self.validate_guess()
            result = self.check_validated_guess()

            print(self.__class__.GUESSING_MESSAGES[result])

            if result == "match":
                print(self.__class__.END_GAME_MESSAGES["win"])
                return
            
            self.guesses -= 1

        print(self.__class__.END_GAME_MESSAGES["lose"])
    
        
    def reset_game(self):
        self.guesses = 7
        self.random = random.randint(1, 100)
        
    def validate_guess(self):
        while True:
            try:
                guess = int(input("Enter a number between 1 and 100: "))

                if 1 <= guess <= 100:
                     return guess
                else:
                     print("Invalid guess. ", end="")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def show_guesses_remaining(self):
        print(f"You have {self.guesses} guesses remaining.")

    def check_validated_guess(self):
            if self.user_guess > self.random:
                return "high"
            elif self.user_guess < self.random:
                return "low"
            else:
                return "match"
            
game = GuessingGame()
game.play()