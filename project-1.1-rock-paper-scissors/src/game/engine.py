from game.computer import get_computer_choice
from game.player import get_user_input


class RockPaperScissors:
    """
    Main game engine for Rock-Paper-Scissors.

    Attributes:
        user_score (int): Score of the user.
        computer_score (int): Score of the computer.
    """

    def __init__(self):
        """Initialize scores for user and computer."""
        self.user_score = 0
        self.computer_score = 0

    def determine_winner(self, user_choice: str, computer_choice: str) -> str:
        """
        Determine the winner of a single round.

        Args:
            user_choice (str): User's move.
            computer_choice (str): Computer's move.

        Returns:
            str: 'user', 'computer', or 'tie'

        """
        win_conditions = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if user_choice == computer_choice:
            return "tie"
        elif win_conditions[user_choice] == computer_choice:
            return "user"
        else:
            return "computer"
        
    def play_round(self, user_choice: str, computer_choice: str) -> str:
        """
        Play a single round and update scores.

        Args:
            user_choice (str): User's move
            computer_choice (str): Computer's move.

        Returns:
            str: The outcome of the round.
        """
        winner = self.determine_winner(user_choice, computer_choice)

        if winner == "user":
            self.user_score += 1
            print("✅ You win this round!")
        elif winner == "computer":
            self.computer_score += 1
            print("💻 Computer wins this round!")
        else:
            print("🤝 It's a tie!")

        print(f"Score → You: {self.user_score} | Computer: {self.computer_score}")
        return winner