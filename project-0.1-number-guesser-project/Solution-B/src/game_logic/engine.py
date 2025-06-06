import random
from config import MIN_NUM, MAX_NUM, MAX_SCORE, SCORE_REDUCTION
from .input_handler import get_valid_guess
from .game_flow import ask_play_again

def play_round(player1: str, player2: str) -> int:
    """Play a round with two players taking turns. Returns winner's score or 0."""
    random_number = random.randint(MIN_NUM, MAX_NUM)
    score = MAX_SCORE
    current_player = player1

    print(f"\n🎯 A number has been chosen between {MIN_NUM} and {MAX_NUM}!")

    while True:
        print(f"\n🎲 {current_player}'s turn:")
        guess = get_valid_guess()
        if guess == -1:
            print("❌ Game aborted.")
            return 0

        if guess == random_number:
            print(f"🎉 {current_player} guessed correctly with a score of {score}!")
            return score

        if guess > random_number:
            print("🔻 Too high!")
        else:
            print("🔺 Too low!")

        score = max(score - SCORE_REDUCTION, 0)

        if score == 0:
            print("💀 Game Over! No points left.")
            return 0

        current_player = player2 if current_player == player1 else player1
