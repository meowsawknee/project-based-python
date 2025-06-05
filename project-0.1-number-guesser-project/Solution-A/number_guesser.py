"""
🎯 Project: Number Guesser Game

This is a beginner-friendly Python project originally based on the version provided in the Pytopia course.
In this version, we've enhanced modularity, added documentation, and applied clean coding principles.
It also includes a proper "Game Over" state when the score reaches zero.

Features:
- Random number generation between 1 and 100
- Input validation
- Hint system (higher/lower)
- Scoring system (starts from 100 and reduces by 10)
- Ends automatically if score hits 0 (Game Over)
- Option to quit anytime
- Option to play multiple rounds

Structure:
This version follows Solution A - all logic is in a single Python file.
While it lacks modularity, it's perfect for learning core concepts like:
- Input handling
- Functions
- Control flow
- Simple game loop design

Author: Hossein Mehrabi
        
"""

import random


# 🆕 Constants defined for configurability and cleaner logic
MIN_NUM = 1
MAX_NUM = 100
MAX_SCORE = 100
SCORE_REDUCTION = 10


def validate_input(input_str: str) -> bool:
    """Validate if the input is a digit and within tha valid range."""
    # 🔁 Logic is based on the original Pytopia version,  with added type hints and docstring
    if not input_str.isdigit():
        print("Invalid input. Please enter a number.")
        return False
    
    num = int(input_str)
    if num < MIN_NUM or num > MAX_NUM:
        print(f"Invalid input. Please enter a number between {MIN_NUM} and {MAX_NUM}.")
        return False
    
    
    return True

def get_valid_guess() -> int:
    """Prompt the user untill a valid guess is provided or 'q' is entered."""
    # 🆕 Extracted from the main loop to improve modularity and testability
    while True:
        guess = input(f"Enter your guess between {MIN_NUM} and {MAX_NUM} (or 'q' to quit): ")
        if guess == 'q':
            return -1 # Sentinel value for quitting
        
        if validate_input(guess):
            return int(guess)

def play_round() -> bool:
    """Play a single round of the guessing game."""
    # 🆕 Game loop extracted from the main function for clarity and reusability
    random_number = random.randint(MIN_NUM, MAX_NUM)
    score = MAX_SCORE

    while True:
        guess = get_valid_guess()
        if guess == -1:
            print("Goodbye!")
            return False

        if guess == random_number:
            print(f"You guessed correctly! Your score is: {score}")
            return ask_play_again()
        
        if guess > random_number:
            print("You guessed too high!")
        else:
            print("You guessed too low!")
        
        # 🧠 Prevents score from going negative - not handled in the Pytopia version
        score = max(score - SCORE_REDUCTION, 0)

        if score == 0:
            print("💀 Game Over! You've run out of points.")
            return ask_play_again()    
        
def ask_play_again() -> bool:
    """Ask the user whether they want to play another round."""
    # 🆕 Extracted from game loop to separate concerns
    choice = input("Do you want to play again? (y/n): ").lower()
    return choice == 'y' # more pythonic
#   if choice == 'y':
#       return True
#   else:
#       return False

def main():
    """Main entry point of the game."""
    # 🆕 Added a main() wrapper to structure execution more cleanly
    print("🎮 Welcome to Number Guesser!")
    while play_round():
        pass

if __name__ == "__main__":
    # Standard guard to allow safe import without auto-execution
    main()
