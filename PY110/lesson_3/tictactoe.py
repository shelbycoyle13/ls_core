import os
import random
import time

INITIAL_MARKER = " "
HUMAN_MARKER = "X"
COMPUTER_MARKER = "O"
WINNING_SCORE = 5
WINNING_LINES = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],  # rows
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],  # columns
    [1, 5, 9],
    [3, 5, 7],  # diagonals
]
FIRST_MOVE = ["player", "computer", "choose"]


def prompt(message):
    print(f"==> {message}")


def display_board(board):
    os.system("cls")

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    prompt("Each win is a point. The first to 5 points wins the match!")
    print("")
    print("     |     |")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print("     |     |")
    print("")


def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}


def join_or(lst, symbol=", ", conjunc="or"):

    final_string = ""

    if len(lst) == 0:
        return final_string
    if len(lst) == 1:
        final_string += str(lst[0])
    elif len(lst) == 2:
        final_string += f"{str(lst[0])} {conjunc} {str(lst[1])}"
    elif len(lst) >= 3:
        for num in lst[:-1]:
            final_string += f"{str(num)}{symbol}"

        final_string = final_string.rstrip(symbol)
        final_string += f" {conjunc} " + str(lst[-1])

    return final_string


def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]


def who_goes_first():

    prompt(
        "Who do you want to go first? "
        "Press 1 for Player, 2 for Computer, 3 for Choose"
    )
    first_move_choice = input().strip()

    while first_move_choice not in ["1", "2", "3"]:
        prompt("Sorry, please pick either 1, 2 or 3.")
        first_move_choice = input().strip()

    if first_move_choice == "1":
        return FIRST_MOVE[0]
    if first_move_choice == "2":
        return FIRST_MOVE[1]
    if first_move_choice == "3":
        return random.choice(FIRST_MOVE[:2])

    return None

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square {join_or(valid_choices)}:")
        square = input().strip()
        if square in valid_choices:
            break
        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER


def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = offensive_computer(board)

    if square is None:
        square = defensive_computer(board)

    if square is None and board[5] == INITIAL_MARKER:
        square = 5

    if square is None:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER
    display_board(board)
    time.sleep(1)


def defensive_computer(board):

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

    if (
        board[sq1] == HUMAN_MARKER
        and board[sq2] == HUMAN_MARKER
        and board[sq3] == INITIAL_MARKER
    ):
        return sq3

    if (
        board[sq1] == HUMAN_MARKER
        and board[sq3] == HUMAN_MARKER
        and board[sq2] == INITIAL_MARKER
    ):
        return sq2

    if (
        board[sq2] == HUMAN_MARKER
        and board[sq3] == HUMAN_MARKER
        and board[sq1] == INITIAL_MARKER
    ):
        return sq1

    return None


def offensive_computer(board):

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

    if (
        board[sq1] == COMPUTER_MARKER
        and board[sq2] == COMPUTER_MARKER
        and board[sq3] == INITIAL_MARKER
    ):
        return sq3

    if (
        board[sq1] == COMPUTER_MARKER
        and board[sq3] == COMPUTER_MARKER
        and board[sq2] == INITIAL_MARKER
    ):
        return sq2

    if (
        board[sq2] == COMPUTER_MARKER
        and board[sq3] == COMPUTER_MARKER
        and board[sq1] == INITIAL_MARKER
    ):
        return sq1

    return None


def choose_square(board, current_player):
    if current_player == "player":
        player_chooses_square(board)
    elif current_player == "computer":
        computer_chooses_square(board)


def alternate_player(current_player):
    if current_player == "player":
        return "computer"
    if current_player == "computer":
        return "player"
    return None


def board_full(board):
    return len(empty_squares(board)) == 0


def detect_winner(board):

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        if (
            board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER
        ):
            return "Player"
        if (
            board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER
        ):
            return "Computer"

    return None


def someone_won(board):
    return bool(detect_winner(board))


def keep_score(winner, player_score, computer_score):

    if winner == "Player":
        player_score += 1
    if winner == "Computer":
        computer_score += 1

    prompt(f"The current score is Player: "
           f"{player_score}, Computer: {computer_score}")

    if player_score == WINNING_SCORE:
        prompt("Player wins the match!")
        return 0, 0
    if computer_score == WINNING_SCORE:
        prompt("Computer wins the match!")
        return 0, 0

    return player_score, computer_score


def play_tic_tac_toe():
    player_score = 0
    computer_score = 0

    while True:
        board = initialize_board()
        first_move_player = who_goes_first()
        current_player = first_move_player
        first_turn = True

        while True:
            display_board(board)

            if current_player == "player":
                if first_turn:
                    prompt("Okay, you will go first.")
                    first_turn = False
            else:
                if first_turn:
                    prompt("Okay, the computer will go first.")
                    time.sleep(2)
                    first_turn = False

            choose_square(board, current_player)

            if someone_won(board) or board_full(board):
                break

            current_player = alternate_player(current_player)

        display_board(board)

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")

        winner = detect_winner(board)
        player_score, computer_score = keep_score(
            winner, player_score, computer_score)

        prompt("Play again? (Y or N)")
        answer = input().lower()

        while answer not in ["y", "Y", "n", "N"]:
            prompt("Sorry, that's not a valid response. "
                   "Please just enter Y or N")
            answer = input().lower()

        if answer not in ["y", "Y"]:
            break

    prompt("Thanks for playing Tic Tac Toe!")


play_tic_tac_toe()