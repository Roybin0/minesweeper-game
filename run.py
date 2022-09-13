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
                print("You chose easy! Let's go!")
                return level
            if level == 'm':
                print("You chose medium! Let's go!")
                return level
            if level == 'h':
                print("You chose hard! Let's go!")
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


def draw_board(level):
    """
    Draws the minesweeper game board and places mines in 
    random locations. The number of mines depends on the difficulty
    level chosen. As mines are placed, the value of the immediate surrounding
    spaces is increased by 1. 
    """

    print("Drawing game board...\n")

    if level == 'e':
        size = 5
        mines = 5
    elif level == 'm':
        size = 10
        mines = 20
    elif level == 'h':
        size = 15
        mines = 30

    print(f"The board will be {size} x {size}")
    print(f"You must avoid {mines} mines. Good luck!")

    board = [[0 for row in range(size)] for column in range(size)]

    for mine in range(mines): 
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        board[x][y] = 'X'

    for row in board:
        print(" ".join(str(cell) for cell in row))


difficulty = get_difficulty_level()
draw_board(difficulty)