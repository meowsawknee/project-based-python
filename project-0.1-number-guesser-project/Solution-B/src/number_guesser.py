from game_logic.engine import play_round
from game_logic.score_tracker import load_high_score, save_high_score
from game_logic.player_manager import create_players
from game_logic.game_flow import ask_play_again
from config import *

def main():
    print("🎮 Welcome to the Number Guesser!")
    high_score = load_high_score()
    print(f"🏆 Current High Score: {high_score}")

    player1, player2 = create_players()

    while True:
        score = play_round(player1, player2)

        if score > high_score:
            print("🔥 New High Score!")
            save_high_score(score)
            high_score = score

        if not ask_play_again():
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
