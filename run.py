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
            if level == 'm':
                print("You chose medium! Let's go!")
            if level == 'h':
                print("You chose hard! Let's go!")
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


get_difficulty_level()