from game.engine import RockPaperScissors
from game.player import get_user_input
from game.computer import get_computer_choice

def main():
    """
    Entry point for the Rock-Paper-Scissors game.
    Runs the game loop untill a player reaches 5 points or quits.
    
    """
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("First to 5 wins. Type 'q' to quit at any time.\n")
    
    game = RockPaperScissors()

    while True:
        user_choice = get_user_input()
        if user_choice == "q":
            print("👋 Thanks for playing!")
            break

        computer_choice = get_computer_choice()
        print(f"💻 Computer chose: {computer_choice}")

        game.play_round(user_choice, computer_choice)

        if game.user_score == 5:
            print("🏆 You won the game!")
            break
        elif game.computer_score == 5:
            print("💀 Computer won the game!")
            break

        print(f"🏆 Final score: You: {game.user_score} | Computer: {game.computer_score}")
        print("-" * 44)

if __name__ == "__main__":
    main()
