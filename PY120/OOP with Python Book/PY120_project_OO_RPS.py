# Project: OO Rock Paper Scissors
import random

class Move:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Rock(Move):
    def __init__(self):
        super().__init__('rock')
    
    def wins_against(self, other_move):
        return isinstance(other_move, (Scissors, Lizard))

class Paper(Move):
    def __init__(self):
        super().__init__('paper')

    def wins_against(self, other_move):
        return isinstance(other_move, (Rock, Spock))

class Scissors(Move):
    def __init__(self):
        super().__init__('scissors')

    def wins_against(self, other_move):
        return isinstance(other_move, (Paper, Lizard))

class Lizard(Move):
    def __init__(self):
        super().__init__('lizard')

    def wins_against(self, other_move):
        return isinstance(other_move, (Paper, Spock))

class Spock(Move):
    def __init__(self):
        super().__init__('spock')

    def wins_against(self, other_move):
        return isinstance(other_move, (Rock, Scissors))
    
class Player:
    CHOICES = {
        'rock' : Rock,
        'paper' : Paper,
        'scissors' : Scissors,
        "lizard" : Lizard,
        "spock" : Spock
    }

    def __init__(self):
        self.move = None
        self.score = 0
        self.history = []

    def _update_move(self, move_object):
        self.move = move_object
        self.history.append(self.move)

class Computer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def _select_move_object(self, human_player):
        choice_name = random.choice(list(Player.CHOICES.keys()))
        return Player.CHOICES[choice_name]()

    def choose(self, human_player):
        move_object = self._select_move_object(human_player)
        self._update_move(move_object)

class R2D2(Computer):
    def __init__(self):
        super().__init__('R2D2')

    def _select_move_object(self, human_player):
        return Player.CHOICES["rock"]()

class HAL(Computer):
    def __init__(self):
        super().__init__('HAL')

    def _select_move_object(self, human_player):
        probabilities = {
            "rock" : 1,
            "paper" : 1,
            "scissors" : 5,
            "lizard" : 1,
            "spock" : 1
        }

        list_of_moves = list(probabilities.keys())
        list_of_probabilities = list(probabilities.values())

        move_name = random.choices(list_of_moves, weights=list_of_probabilities)[0]
        return Player.CHOICES[move_name]()

class Daneel(Computer):
    def __init__(self):
        super().__init__('Daneel')

    def _select_move_object(self, human_player):
        if not human_player.history:
            return super()._select_move_object(human_player)
        
        previous_human_move_name = str(human_player.history[-1])

        move_object = Player.CHOICES[previous_human_move_name]()
        return move_object

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, scissors, lizard, or spock: '

        while True:
            choice_str = input(prompt).lower()
            if choice_str.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice_str} is not valid')

        move_object = Player.CHOICES[choice_str]()
        self._update_move(move_object)

class RPSGame:
    WINNING_SCORE = 5
    OPPONENTS = {
        "1" : HAL,
        "2" : R2D2,
        "3" : Daneel
    }

    def __init__(self):
        self._human = Human()
        self._computer = None

    def _display_welcome_message(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock! You will play against the computer. Whoever wins 5 rounds wins the entire game!")

    def _select_opponent(self):
        prompt = ("Choose your opponent:\n"
            "Press 1 for HAL\n"
            "Press 2 for R2D2\n"
            "Press 3 for Daneel\n")
        
        while True:
            choice = input(prompt)
            if choice in RPSGame.OPPONENTS:
                break
            else:
                print("Sorry, please choose a valid opponent.")

        self._computer = RPSGame.OPPONENTS[choice]()
        print(f"You have selected {self._computer.name} as your opponent. Good luck!")


    def _display_goodbye_message(self):
        print("Thanks for playing Rock, Paper, Scissors, Lizard, Spock! Bye for now!")

    def _human_wins(self):
        return self._human.move.wins_against(self._computer.move)

    def _computer_wins(self):
        return self._computer.move.wins_against(self._human.move)

    def _display_round_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win the round!')
        elif self._computer_wins():
            print('Computer wins the round!')
        else:
            print("This round is a tie!")

    def _update_scores(self):
        if self._human_wins():
            self._human.score += 1
        elif self._computer_wins():
            self._computer.score += 1

    def _display_round_score(self):
        print(f"Your score is currently: {self._human.score}")
        print(f"The computer's score is currently: {self._computer.score}")

    def _display_history(self):
        print(f"Your move history is: {[str(move) for move in self._human.history]}")
        print(f"The computer's move history is: {[str(move) for move in self._computer.history]}")

    def _display_game_winner(self):
        if self._human.score == RPSGame.WINNING_SCORE:
            print("Congratulations, you won the game!!!")
        else:
            print("The computer has won the game! Better luck next time!")

    def play(self):
        self._display_welcome_message()

        while True:
            self._play_match()
            if not self._play_again():
                break

        self._display_goodbye_message()

    def _play_match(self):
        self._human = Human()
        self._select_opponent()

        while self._human.score < RPSGame.WINNING_SCORE and self._computer.score < RPSGame.WINNING_SCORE:
            self._computer.choose(self._human)
            self._human.choose()
            self._update_scores()
            self._display_round_winner()
            self._display_round_score()
            self._display_history()                
            
        self._display_game_winner()

    def _play_again(self):
        while True:
            answer = input('Would you like to play again? Please type Y or N: ').lower()
            if answer in ["y", "n"]:
                break

            print("Sorry, that's not a valid response. Please type Y or N: ")

        return answer == "y"

RPSGame().play()