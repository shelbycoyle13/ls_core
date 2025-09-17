# Poker
# In the previous two exercises, you developed a Card class and a Deck class. You are now going to use those classes to create and evaluate poker hands. Create a class, PokerHand, that takes 5 cards from a Deck of Cards and evaluates those cards as a poker hand.

# If you are unfamiliar with Poker, please see this description of the various hand types. Since we won't actually be playing a game of Poker, it isn't necessary to know how to play.

# You should build your class using the following code skeleton:

# Include Card and Deck classes from the last two exercises.

# class PokerHand:
#     def __init__(self, deck):
#         pass

#     def print(self):
#        pass

#     def evaluate(self):
#         if self._is_royal_flush():
#             return "Royal flush"
#         elif self._is_straight_flush():
#             return "Straight flush"
#         elif self._is_four_of_a_kind():
#             return "Four of a kind"
#         elif self._is_full_house():
#             return "Full house"
#         elif self._is_flush():
#             return "Flush"
#         elif self._is_straight():
#             return "Straight"
#         elif self._is_three_of_a_kind():
#             return "Three of a kind"
#         elif self._is_two_pair():
#             return "Two pair"
#         elif self._is_pair():
#             return "Pair"
#         else:
#           return "High card"

#     def _is_royal_flush(self):
#         pass

#     def _is_straight_flush(self):
#         pass

#     def _is_four_of_a_kind(self):
#         pass

#     def _is_full_house(self):
#         pass

#     def _is_flush(self):
#         pass

#     def _is_straight(self):
#         pass

#     def _is_three_of_a_kind(self):
#         pass

#     def _is_two_pair(self):
#         pass

#     def _is_pair(self):
#         pass

# Testing your class:

# hand = PokerHand(Deck())
# hand.print()
# print(hand.evaluate())
# print()

# Adding TestDeck class for testing purposes

# class TestDeck(Deck):
#     def __init__(self, cards):
#         self._deck = cards

# All of these tests should return True

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Ace", "Hearts"),
#             Card("Queen", "Hearts"),
#             Card("King", "Hearts"),
#             Card("Jack", "Hearts"),
#             Card(10, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Royal flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Clubs"),
#             Card("Queen", "Clubs"),
#             Card(10, "Clubs"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Four of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Full house")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(10, "Hearts"),
#             Card("Ace", "Hearts"),
#             Card(2, "Hearts"),
#             Card("King", "Hearts"),
#             Card(3, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Diamonds"),
#             Card(10, "Clubs"),
#             Card(7, "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Queen", "Clubs"),
#             Card("King", "Diamonds"),
#             Card(10, "Clubs"),
#             Card("Ace", "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(6, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Three of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(9, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(8, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Two pair")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Pair")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card("King", "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "High card")

# 5 of Clubs
# 7 of Diamonds
# Ace of Hearts
# 7 of Clubs
# 5 of Spades
# Two pair

# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true
# true

# The exact cards and the type of hand for the first test will vary with each run, so don't expect the same output we show for the first 6 lines.

# Some variants of Poker allow both Ace-high (A, K, Q, J, 10) and Ace-low (A, 2, 3, 4, 5) straights. For simplicity, your code only needs to recognize Ace-high straights.

# Include Card and Deck classes from the last two exercises.

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    CARD_RANKINGS = {
        2 : 2,
        3 : 3,
        4 : 4,
        5 : 5,
        6 : 6,
        7 : 7,
        8 : 8,
        9 : 9,
        10 : 10,
        "Jack" : 11,
        "Queen" : 12,
        "King" : 13,
        "Ace" : 14
    }

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.CARD_RANKINGS[self.rank] < self.CARD_RANKINGS[other.rank]
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.CARD_RANKINGS[self.rank] == self.CARD_RANKINGS[other.rank] and self.suit == other.suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._reset()

    def _reset(self):
        self._deck = [Card(rank, suit) for suit in Deck.SUITS
                    for rank in Deck.RANKS]
        self.shuffle()

    def draw(self):
        if not self._deck:
            self._reset()
        
        return self._deck.pop()

    def shuffle(self):
        random.shuffle(self._deck)

class PokerHand:
    def __init__(self, deck):
        self.hand = [deck.draw() for num in range(5)]

    def print(self):
       for card in self.hand:
           print(card) #This is a Card object because we actually define and update the string method in the Card class

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        if all(card.suit == self.hand[0].suit for card in self.hand) and all(card.rank in [10, 'Jack', 'Queen', 'King', 'Ace'] for card in self.hand):
            return True
        return False

    def _is_straight_flush(self):
        sorted_card_values = sorted([Card.CARD_RANKINGS[card.rank] for card in self.hand])
        consecutive_range = [sorted_card_values[0], sorted_card_values[0] + 1, sorted_card_values[0] + 2, sorted_card_values[0] + 3, sorted_card_values[0] + 4]

        if sorted_card_values == consecutive_range and all(card.suit == self.hand[0].suit for card in self.hand):
            return True
        return False

    def _is_four_of_a_kind(self):
        ranks_list = [card.rank for card in self.hand]
        for rank in ranks_list:
            if ranks_list.count(rank) == 4:
                return True
        return False

    def _is_full_house(self):
        ranks_list = [card.rank for card in self.hand]
        rank_counts = {rank : ranks_list.count(rank) for rank in set(ranks_list)}
        
        if list(rank_counts.values()).count(3) == 1 and list(rank_counts.values()).count(2) == 1:
            return True
        return False

    def _is_flush(self):
        # if PokerHand._is_straight_flush(self): #Unecessary check since the program checks for the types of hands in order
        #     return False
        return all(card.suit == self.hand[0].suit for card in self.hand)

    def _is_straight(self):
        # if PokerHand._is_straight_flush(self): #Unecessary check since the program checks for the types of hands in order
        #     return False
        
        sorted_card_values = sorted([Card.CARD_RANKINGS[card.rank] for card in self.hand])
        consecutive_range = [sorted_card_values[0], sorted_card_values[0] + 1, sorted_card_values[0] + 2, sorted_card_values[0] + 3, sorted_card_values[0] + 4]

        if sorted_card_values == consecutive_range:
            return True
        return False

    def _is_three_of_a_kind(self):
        ranks_list = [card.rank for card in self.hand]
        rank_counts = {rank : ranks_list.count(rank) for rank in set(ranks_list)}
        
        if list(rank_counts.values()).count(3) == 1 and list(rank_counts.values()).count(1) == 2:
            return True
        return False


    def _is_two_pair(self):
        ranks_list = [card.rank for card in self.hand]
        rank_counts = {rank : ranks_list.count(rank) for rank in set(ranks_list)}
        
        if list(rank_counts.values()).count(2) == 2 and list(rank_counts.values()).count(1) == 1:
            return True
        return False

    def _is_pair(self):
        ranks_list = [card.rank for card in self.hand]
        rank_counts = {rank : ranks_list.count(rank) for rank in set(ranks_list)}
        
        if list(rank_counts.values()).count(2) == 1 and list(rank_counts.values()).count(1) == 3:
            return True
        return False

hand = PokerHand(Deck())
hand.print() #Note this is a method called on by Pokerhand - notice it's .print(); it's different than the built-in print()!
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")