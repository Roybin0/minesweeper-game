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
                print("You chose easy. Let's go!")
                return level
            if level == 'm':
                print("You chose medium. Let's go!")
                return level
            if level == 'h':
                print("You chose hard. Let's go!")
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
    level chosen. As mines are placed, the value of the immediate surrounding
    spaces is increased by 1. 
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


def find_surrounding_mines(board, size):
    """
    Checks the surrounding spaces for the number of mines, if any. 
    """

    for row in range(size):
        for col in range(size): 
            continue
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
            
        elif (row >= 1 and row <= size - 2) and (col >= 1 and col <= size - 2):
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


difficulty = get_difficulty_level()
new_game = create_board(difficulty)
find_surrounding_mines(new_game, 5)
