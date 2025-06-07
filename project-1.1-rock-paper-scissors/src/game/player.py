def get_user_input() -> str:
    
    """
    Prompt the user to enter their choice and validate the input.
    Only accepts 'rock', 'paper', 'scissors', or 'q' (to quit).
    
    Returns:
        str: The validated user choice.
    """

    valid_choices = ["rock", "paper", "scissors", "q"]

    while True:
        choice = input("Enter your choice (rock/paper/scissors or 'q' to quit): ").lower()

        if choice in valid_choices:
            return choice
        else:
            print("❌ Invalid input. Please type: rock, paper, scissors, or q.")