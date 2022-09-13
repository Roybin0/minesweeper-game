import random 


def get_difficulty_level():
    """
    Ask the player what difficulty they would like to play
    """

    print("What difficulty would you like to play?")
    print("Type 'E' for easy, 'M' for medium or 'H' for hard")

    level = input("Enter difficulty level here: \n")
 
    validate_level(level)

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


get_difficulty_level()