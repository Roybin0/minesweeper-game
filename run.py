import random
import sys


def get_difficulty_level():
    """
    Ask the player what difficulty they would like to play
    """
    while True:
        print("What difficulty would you like to play?")
        print("Type 'E' for easy, 'M' for medium or 'H' for hard")

        level = input("Enter difficulty level here: \n")

        if validate_level(level):
            level = level.lower()
            if level == 'e':
                print("You chose easy. Let's go!\n")
                return level
            if level == 'm':
                print("You chose medium. Let's go!\n")
                return level
            if level == 'h':
                print("You chose hard. Let's go!\n")
                return level
            break


def validate_level(data):
    """
    Inside the try, converts data input to lowercase.
    Raises ValueError if string does not match a difficulty level.
    """
    try:
        data = data.lower()
        if data != 'e':
            if data != 'm':
                if data != 'h':
                    raise ValueError(
                        f"Expected 'E', 'M', or 'H', you entered {data}"
                    )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False

    return True


def create_board(level):
    """
    Draws the minesweeper game board and places mines in
    random locations. The number of mines depends on the difficulty
    level chosen.
    """

    print("Drawing game board...\n")

    if level == 'e':
        size = 5
        mines = 8
    elif level == 'm':
        size = 10
        mines = 20
    elif level == 'h':
        size = 15
        mines = 30

    print(f"The board will be {size} x {size}.")
    print(f"Rows and columns are numbered 1 - {size}.")
    print("Enter a row number first, then a column number.")
    print(f"You must avoid {mines} mines. Good luck!\n")

    board = [[0 for _ in range(size)] for _ in range(size)]
    hidden_mines = 0
    while hidden_mines < mines:
        row = random.randint(0, size-1)
        col = random.randint(0, size-1)

        if board[row][col] == 'X':
            continue

        board[row][col] = 'X'
        hidden_mines += 1

    return board


def find_surrounding_mines(board):
    """
    Checks each space to see if it contains a mine. If so, increments value
    of immedately surrounding spaces by 1.
    """

    size = len(board[0])

    for row in range(size):
        for col in range(size):
            if board[row][col] == 'X':
                if row == 0 and col == 0:
                    if board[row+1][col] != 'X':
                        board[row+1][col] += 1
                    if board[row][col+1] != 'X':
                        board[row][col+1] += 1
                    if board[row+1][col+1] != 'X':
                        board[row+1][col+1] += 1

                elif (1 <= row <= size-2) and col == 0:
                    if board[row-1][col] != 'X':
                        board[row-1][col] += 1
                    if board[row+1][col] != 'X':
                        board[row+1][col] += 1
                    if board[row-1][col+1] != 'X':
                        board[row-1][col+1] += 1
                    if board[row][col+1] != 'X':
                        board[row][col+1] += 1
                    if board[row+1][col+1] != 'X':
                        board[row+1][col+1] += 1

                elif row == size-1 and col == 0:
                    if board[row-1][col] != 'X':
                        board[row-1][col] += 1
                    if board[row-1][col+1] != 'X':
                        board[row-1][col+1] += 1
                    if board[row][col+1] != 'X':
                        board[row][col+1] += 1

                elif row == size - 1 and (1 <= col <= size - 2):
                    if board[row-1][col-1] != 'X':
                        board[row-1][col-1] += 1
                    if board[row][col-1] != 'X':
                        board[row][col-1] += 1
                    if board[row-1][col] != 'X':
                        board[row-1][col] += 1
                    if board[row-1][col+1] != 'X':
                        board[row-1][col+1] += 1
                    if board[row][col+1] != 'X':
                        board[row][col+1] += 1

                elif row == size - 1 and col == size - 1:
                    if board[row-1][col-1] != 'X':
                        board[row-1][col-1] += 1
                    if board[row][col-1] != 'X':
                        board[row][col-1] += 1
                    if board[row-1][col] != 'X':
                        board[row-1][col] += 1

                elif (1 <= row <= size - 2) and col == size - 1:
                    if board[row-1][col-1] != 'X':
                        board[row-1][col-1] += 1
                    if board[row][col-1] != 'X':
                        board[row][col-1] += 1
                    if board[row+1][col-1] != 'X':
                        board[row+1][col-1] += 1
                    if board[row-1][col] != 'X':
                        board[row-1][col] += 1
                    if board[row+1][col] != 'X':
                        board[row+1][col] += 1

                elif row == 0 and col == size - 1:
                    if board[row][col-1] != 'X':
                        board[row][col-1] += 1
                    if board[row+1][col-1] != 'X':
                        board[row+1][col-1] += 1
                    if board[row+1][col] != 'X':
                        board[row+1][col] += 1

                elif row == 0 and (1 <= col <= size - 2):
                    if board[row][col-1] != 'X':
                        board[row][col-1] += 1
                    if board[row+1][col-1] != 'X':
                        board[row+1][col-1] += 1
                    if board[row+1][col] != 'X':
                        board[row+1][col] += 1
                    if board[row][col+1] != 'X':
                        board[row][col+1] += 1
                    if board[row+1][col+1] != 'X':
                        board[row+1][col+1] += 1

                elif (0 < row < size - 1) and (0 < col < size - 1):
                    if board[row-1][col-1] != 'X':
                        board[row-1][col-1] += 1
                    if board[row][col-1] != 'X':
                        board[row][col-1] += 1
                    if board[row+1][col-1] != 'X':
                        board[row+1][col-1] += 1
                    if board[row-1][col] != 'X':
                        board[row-1][col] += 1
                    if board[row+1][col] != 'X':
                        board[row+1][col] += 1
                    if board[row-1][col+1] != 'X':
                        board[row-1][col+1] += 1
                    if board[row][col+1] != 'X':
                        board[row][col+1] += 1
                    if board[row+1][col+1] != 'X':
                        board[row+1][col+1] += 1

    return board


def create_starting_board(level):
    """
    Draws the players starting minesweeper game board
    """
    if level == 'e':
        size = 5
        board = [["-" for _ in range(size)] for _ in range(size)]
        return board

    if level == 'm':
        size = 10
        board = [["-" for _ in range(size)] for _ in range(size)]
        return board

    if level == 'h':
        size = 15
        board = [["-" for _ in range(size)] for _ in range(size)]
        return board


def print_game_board(board):
    """
    Draws the game board for the player to see. It's repeatedly called to
    update the game board when the player chooses locations to dig.
    """
    for row in board:
        print(" ".join(str(cell) for cell in row))

    return board


def play_game(game_board, players_board):
    """
    Takes the players input and and checks if a mine is at that location.
    Returns an updated game board.
    """

    size = len(players_board)

    while True:
        if board_clear(players_board) is False:

            while True:
                print(" \n")
                row = input(f"Choose a row (1 - {size}): \n")
                if validate_data(row, size):
                    break

            while True:
                col = input(f"Choose a column (1 - {size}): \n")
                print(" \n")
                if validate_data(col, size):
                    break

            row = int(row) - 1
            col = int(col) - 1

            if players_board[row][col] != '-':
                print("You've checked here already!")
                continue
            elif game_board[row][col] == 'X':
                print("Game over!")
                print_game_board(game_board)
                play_again()
            else:
                players_board[row][col] = game_board[row][col]
                print_game_board(players_board)

        else:
            print("Congratulations! You've found all the mines!")
            play_again()
            break


def validate_data(data, size):
    """
    Inside the try, converts data input to integer.
    Raises ValueError if data is outside range.
    """

    try:
        data_int = int(data)
        if data_int > size:
            raise ValueError(
                f"Must be between 1 and {size}. You entered {data}. Try again!"
                )
        if data_int < 1:
            raise ValueError(
                f"Must be between 1 and {size}. You entered {data}. Try again!"
            )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False

    return True


def board_clear(players_board):
    """
    Iterates through all values of the players board to check for
    '-'. If there are none remaining the player has won the game.
    """
    size = len(players_board[0])

    if size == 5:
        mines = 8
    if size == 10:
        mines = 20
    if size == 15:
        mines = 30

    remaining_mines = 0
    for row in range(size):
        for col in range(size):
            if players_board[row][col] == '-':
                remaining_mines += 1

    if remaining_mines > mines:
        return False
    return True


def play_again():
    """
    Asks the player if they would like to play again. Displays if game over
    or player finds all mines.
    """
    while True:
        answer = input("Would you like to play again? Y/N \n")
        if validate_replay(answer):
            break

    if answer.lower() == 'y':
        main()
    else:
        sys.exit()


def validate_replay(data):
    """
    Inside the try, converts data input to lowercase.
    Raises ValueError if string does not match Y or N.
    """
    try:
        data = data.lower()
        if data != 'y':
            if data != 'n':
                raise ValueError(
                    f"Expected 'Y' or 'N', you entered {data}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}")
        return False

    return True


def main():
    """
    Runs all programs functions
    """
    difficulty = get_difficulty_level()
    new_game = create_board(difficulty)
    find_surrounding_mines(new_game)
    player_board = create_starting_board(difficulty)
    print_game_board(player_board)
    play_game(new_game, player_board)


main()
