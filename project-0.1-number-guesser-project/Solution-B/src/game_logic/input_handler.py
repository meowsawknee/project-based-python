from config import MIN_NUM, MAX_NUM

def validate_input(input_str: str) -> bool:
    if not input_str.isdigit():
        print("Invalid input. Please enter a number.")
        return False
    num = int(input_str)
    if num < MIN_NUM or num > MAX_NUM:
        print(f"Invalid input. Please enter a number between {MIN_NUM} and {MAX_NUM}.")
        return False
    return True

def get_valid_guess() -> int:
    while True:
        guess = input(f"Enter your guess between {MIN_NUM} and {MAX_NUM} (or 'q' to quit): ")
        if guess.lower() == 'q':
            return -1
        if validate_input(guess):
            return int(guess)
