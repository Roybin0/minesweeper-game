import random 

def get_difficulty_level():
    """
    Ask the user what difficulty they would like to play
    """

    print("What difficulty would you like to play?")
    print("Type 'E' for easy, 'M' for medium or 'H' for hard")

    level = input("Enter difficulty level here: \n")

    print(f"You entered {level}")

get_difficulty_level()

