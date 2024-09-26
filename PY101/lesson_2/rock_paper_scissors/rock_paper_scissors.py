"""This program allows a user to play a game of 
rock-paper-scissors-lizard-spock 
against the computer. 
It announces a winner after either one gets 3 wins."""

import os
import random
import time

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
VALID_CHOICES_LETTER = ["r", "p", "x", "l", "s"]

def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def prompt(message):
    print(f"==> {message}")

def banner():
    print(
        """
*******************************************************
====  Let's play Rock-Paper-Scissors-Lizard-Spock! ==== 
*******************************************************
"""
    )
def prompt_user_choice():
    prompt(
        "Here's how to play:\n"
        "Rock beats Scissors and Lizard\n"
        "Paper beats Rock and Spock\n"
        "Scissors beats Paper and Lizard\n"
        "Lizard beats Paper and Spock\n"
        "Spock beats Rock and Scissors\n"
        f"Choose one: {', '.join(VALID_CHOICES)}.\n"
        "To make your selection, type in the first letter of the word, "
        "except for scissors, please use 'x'.\n"
        "We play until someone wins 3 games. Let's go!"
    )
    choice = input().strip().casefold()

    while (choice not in VALID_CHOICES_LETTER) and (
        choice not in VALID_CHOICES):
        prompt("That's not a valid choice. Please try again!")
        choice = input()
    return match_choice_letter(choice)

def match_choice_letter(letter):
    if letter in (VALID_CHOICES[0], VALID_CHOICES_LETTER[0]):
        return "rock"
    if letter in (VALID_CHOICES[1], VALID_CHOICES_LETTER[1]):
        return "paper"
    if letter in (VALID_CHOICES[2], VALID_CHOICES_LETTER[2]):
        return "scissors"
    if letter in (VALID_CHOICES[3], VALID_CHOICES_LETTER[3]):
        return "lizard"
    if letter in (VALID_CHOICES[4], VALID_CHOICES_LETTER[4]):
        return "spock"
    return "An error occurred"

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def compute_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def display_winner(player, computer):
    prompt(f"You chose: {player} and the computer chose: {computer}")

    if compute_wins(player, computer):
        return "You win!"
    if compute_wins(computer, player):
        return "Computer wins!"
    return "It's a tie!"

def play_again():
    prompt("Do you want to play again? (Type y for yes and n for no)")
    answer = input().lower().strip()

    while answer not in ["y", "n"]:
        prompt("That's not a valid choice. Please try again!")
        answer = input()

    return answer

def play_rps():
    answer = "y"
    player_wins = 0
    computer_wins = 0
    while answer == "y":
        clean_screen()
        banner()

        player_choice = prompt_user_choice()

        computer_choice = random.choice(VALID_CHOICES)

        result = display_winner(player_choice, computer_choice)

        prompt(result)

        if result == "You win!":
            player_wins += 1
        if result == "Computer wins!":
            computer_wins += 1

        prompt(f"The current score is {player_wins} (you)"
            f" to {computer_wins} (computer).")

        time.sleep(3)

        if player_wins == 3:
            prompt("You are the grand winner - congratulations!")
            answer = play_again()
            if answer == "n":
                break
            player_wins = 0
            computer_wins = 0
        elif computer_wins == 3:
            prompt("The computer is the grand winner - "
                "sorry, you'll win next time!")
            answer = play_again()
            if answer == "n":
                break
            player_wins = 0
            computer_wins = 0

        clean_screen()

play_rps()