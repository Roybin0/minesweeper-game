import random


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

                elif (row >= 1 and row <= size-2) and col == 0:
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

                elif row == size - 1 and (col >= 1 and col <= size - 2):
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
                            
                elif (row >= 1 and row <= size - 2) and col == size - 1:
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

                elif row == 0 and (col >= 1 and col <= size - 2):
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

    for row in board:
        print(" ".join(str(cell) for cell in row))

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


def play_game(players_board, game_board):
    """
    Asks the player to choose a row and column number and checks if
    a mine is at that location. Returns an updated game board.
    """
    while True:
        size = len(game_board[0])

        play_row = input(f"Choose a row number (1 - {size}): \n")

        while True:
            if validate_data(play_row, size):
                break

        play_col = input(f"Choose a column number (1 - {size}): \n")
        
        while True:
            if validate_data(play_col, size):
                break

        play_row = int(play_row) - 1
        play_col = int(play_col) - 1

        if game_board[play_row][play_col] == 'X':
            print("Game over!")
            print_game_board(game_board)
            return False  # Create function for end_game? Continue? 

        players_board[play_row][play_col] = game_board[play_row][play_col]
        print_game_board(players_board)
        return True

    return True


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


difficulty = get_difficulty_level()
new_game = create_board(difficulty)

find_surrounding_mines(new_game)
player_board = create_starting_board(difficulty)
print_game_board(player_board)
play_game(player_board, new_game)
