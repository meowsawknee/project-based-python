from game_logic.score_tracker import load_high_score, save_high_score

def main():
    print("🎮 Welcome to the Number Guesser!")

    high_score = load_high_score()
    print(f"🏆 Current High Score: {high_score}")

    
    # TODO: Play the game here
    # TODO: After win, check score and save if needed


if __name__ == "__main__":
    main()