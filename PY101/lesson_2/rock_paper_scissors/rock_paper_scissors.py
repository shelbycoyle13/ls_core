"""This program allows a user to play a game of 
rock-paper-scissors-lizard-spock 
against the computer. 
It announces a winner after either one gets 3 wins."""

import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
VALID_CHOICES_LETTER = ["r", "p", "x", "l", "s"]

def prompt(message):
    print(f"==> {message}")


def match_choice_letter(letter):
    if letter == "r":
        return "rock"
    if letter == "p":
        return "paper"
    if letter == "x":
        return "scissors"
    if letter == "l":
        return "lizard"
    if letter == "s":
        return "spock"
    return "An error occurred"

def player_wins(player, computer):
    return (
        (player == "rock" and computer in ("scissors", "lizard"))
        or (player == "paper" and computer in ("rock", "spock"))
        or (player == "scissors" and computer in ("paper", "lizard"))
        or (player == "lizard" and computer in ("paper", "spock"))
        or (player == "spock" and computer in ("scissors", "rock"))
    )

def computer_wins(player, computer):
    return (
        (player == "rock" and computer in ("paper", "spock"))
        or (player == "paper" and computer in ("scissors", "lizard"))
        or (player == "scissors" and computer in ("rock", "spock"))
        or (player == "lizard" and computer in ("rock", "scissors"))
        or (player == "spock" and computer in ("lizard", "paper"))
    )

def display_winner(player, computer):
    prompt(f"You chose: {player} and the computer chose: {computer}")

    if player_wins(player, computer):
        return "You win!"
    if computer_wins(player, computer):
        return "Computer wins!"
    return "It's a tie!"

ANSWER = "y"

PLAYER_WINS = 0
COMPUTER_WINS = 0

while ANSWER == "y":
    prompt(
        f"Choose one: {', '.join(VALID_CHOICES)}. "
        "To make your selection, type in the first letter of the word, "
        "except for scissors, please use 'x'."
    )
    choice = input().strip()

    while choice not in VALID_CHOICES_LETTER:
        prompt("That's not a valid choice. Please try again!")
        choice = input()

    PLAYER_CHOICE = match_choice_letter(choice)

    computer_choice = random.choice(VALID_CHOICES)

    RESULT = display_winner(PLAYER_CHOICE, computer_choice)

    prompt(RESULT)

    if RESULT == "You win!":
        PLAYER_WINS += 1
    if RESULT == "Computer wins!":
        COMPUTER_WINS += 1

    prompt(f"The current score is {PLAYER_WINS} (you)"
           f" to {COMPUTER_WINS} (computer).")

    if PLAYER_WINS == 3:
        prompt("You are the grand winner - congratulations!")
        PLAYER_WINS = 0
        COMPUTER_WINS = 0
    elif COMPUTER_WINS == 3:
        prompt("The computer is the grand winner - "
               "sorry, you'll win next time!")
        PLAYER_WINS = 0
        COMPUTER_WINS = 0

    prompt("Do you want to play again? (Type y for yes and n for no)")
    ANSWER = input().lower().strip()

    while ANSWER not in ["y", "n"]:
        prompt("That's not a valid choice. Please try again!")
        ANSWER = input()
