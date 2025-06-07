import random

def get_computer_choice() -> str:

    """
    Randomly select one of the three options: 'rock', 'paper', or 'scissors'

    Returns:
        str: The computer's choice
    """
    
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
