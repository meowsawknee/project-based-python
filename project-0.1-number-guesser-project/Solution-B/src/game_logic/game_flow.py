def ask_play_again() -> bool:
    """Ask player if they want to continue playing."""
    choice = input("Do you want to play again? (y/n): ").lower()
    return choice == 'y' 
