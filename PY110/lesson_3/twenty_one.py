"""
This program plays a simpler version of Blackjack called 21.
"""

import os
import random

DECK = []

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
VALUES = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
    "Ace",
]

GOAL_NUMBER = 21
DEALER_MIN_NUMBER = 17

for suit in SUITS:
    for value in VALUES:
        card = [value, suit]
        DECK.append(card)


def prompt(message):
    print(f"--> {message}")


def initialize_game():
    os.system("cls")

    prompt(f"Welcome to the game {GOAL_NUMBER}!")
    prompt(
        "Each game is a round and a win is worth 1 point. "
        "First to 3 points wins the match!"
    )
    prompt(
        "We are going to shuffle the deck "
        "and deal you and the dealer two cards each."
    )


def shuffle_deck(deck):
    random.shuffle(deck)


def deal_cards(deck):
    hand = [deck.pop(0) for i in range(2)]
    return hand


def total(cards):
    values = [card[0] for card in cards]

    sum_values = 0

    for val in values:
        if val == "Ace":
            sum_values += 11
        elif val in ["Jack", "Queen", "King"]:
            sum_values += 10
        else:
            sum_values += int(val)

    aces = values.count("Ace")

    while sum_values > GOAL_NUMBER and aces:
        sum_values -= 10
        aces -= 1

    return sum_values


def busted(cards):
    if total(cards) > GOAL_NUMBER:
        prompt(f"Uh oh! The sum of these cards is "
               f"{total(cards)}, so this is a bust!")
        return True
    return False


def hit(cards):
    new_card = DECK.pop(0)
    cards.append(new_card)
    return cards


def players_turn(cards):
    while True:
        if busted(cards):
            prompt("The player has busted!")
            return "busted"

        answer = input("Would you like to hit or stay? Use H or S: ").lower()
        if answer not in ["H", "h", "S", "s"]:
            prompt("Sorry, that's not a valid response. "
                   "Please just enter H or S: ")
            answer = input("Would you like to hit or stay? "
                           "Use H or S: ").lower()

        if answer == "s":
            break
        if answer == "h":
            prompt("You chose to hit!")
            hit(cards)
            player_total = total(cards)
            prompt(f"Your current hand is {cards}.")
            prompt(f"The current total of your hand is {player_total}.")

    prompt("You chose to stay!")
    return cards


def dealers_turn(cards):
    prompt(f"The dealer's current hand is: {cards}")
    dealer_total = total(cards)
    prompt(f"The current total of the dealer's hand is {total(cards)}.")

    while dealer_total < DEALER_MIN_NUMBER:
        prompt("The dealer will hit.")
        hit(cards)
        dealer_total = total(cards)
        prompt(f"The dealer's current hand is: {cards}")
        prompt(f"The current total of the dealer's hand is {dealer_total}.")

        if busted(cards):
            prompt("The dealer has busted!")
            return "busted"

    if DEALER_MIN_NUMBER >= dealer_total <= GOAL_NUMBER:
        prompt("The dealer stays.")

    return cards


def determine_winner(player_total, dealer_total):

    if player_total > GOAL_NUMBER:
        winner = "Dealer"
    elif dealer_total > GOAL_NUMBER:
        winner = "Player"
    elif player_total > dealer_total:
        winner = "Player"
    elif dealer_total > player_total:
        winner = "Dealer"
    else:
        winner = "No one"

    return winner


def display_score(player_wins, dealer_wins):
    prompt(f"The current score is Player: {player_wins}"
           f", Dealer: {dealer_wins}")


def display_winner(winner):
    if winner == "No one":
        prompt(f"It's a tie! {winner} won.")
    prompt(f"And the winner is: {winner}!")


def display_match_winner(player_wins, dealer_wins):
    if player_wins == 3:
        prompt("Congrats, you won the match!")
        return True
    if dealer_wins == 3:
        prompt("The Dealer has won the match!")
        return True
    return False


def ask_play_again():
    prompt("Would you like to play again? (Y or N)")
    answer = input().lower()

    while answer not in ["y", "Y", "n", "N"]:
        prompt("Sorry, that's not a valid response. Please just enter Y or N")
        answer = input().lower()

    if answer == "y":
        return True
    return False


def play_21():
    player_wins = 0
    dealer_wins = 0
    while True:
        initialize_game()

        shuffle_deck(DECK)
        players_hand = deal_cards(DECK)
        dealers_hand = deal_cards(DECK)
        player_total = total(players_hand)
        dealer_total = total(dealers_hand)

        prompt(f"Your cards are: {players_hand}")
        prompt(f"The dealer's cards are: {dealers_hand[0]}"
               f" and an unknown card")
        prompt(f"The total value of your cards are: {player_total}")

        player_result = players_turn(players_hand)

        if player_result == "busted":
            winner = "Dealer"
            dealer_wins += 1
            display_winner(winner)
            display_score(player_wins, dealer_wins)

            if ask_play_again() is False:
                prompt("Thanks for playing - have a nice day!")
                break
            continue

        dealer_result = dealers_turn(dealers_hand)

        if dealer_result == "busted":
            winner = "Player"
            player_wins += 1
        else:
            player_total = total(players_hand)
            dealer_total = total(dealers_hand)
            winner = determine_winner((player_total), (dealer_total))
            if winner == "Player":
                player_wins += 1
            if winner == "Dealer":
                dealer_wins += 1
        display_winner(winner)

        display_score(player_wins, dealer_wins)

        if display_match_winner(player_wins, dealer_wins):
            player_wins = 0
            dealer_wins = 0

        if ask_play_again() is False:
            prompt("Thanks for playing - have a nice day!")
            break


play_21()