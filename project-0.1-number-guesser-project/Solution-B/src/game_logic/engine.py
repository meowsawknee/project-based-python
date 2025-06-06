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