import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest
from game.engine import RockPaperScissors


class TestRockPaperScissors(unittest.TestCase):
    """Unit tests for the RockPaperScissors game logic"""

    def setUp(self):
        """Create a new game instance before each test."""
        self.game = RockPaperScissors()

    def test_user_wins(self):
        """
        Test all scenarios where the user should win.
        - Rock beats Scissors
        - Scissors beats Paper
        - Paper beats Rock
        """
        self.assertEqual(self.game.determine_winner("rock", "scissors"), "user")
        self.assertEqual(self.game.determine_winner("scissors", "paper"), "user")
        self.assertEqual(self.game.determine_winner("paper", "rock"), "user")

    def test_computer_wins(self):
        """
        Test all scenarios where the computer should win.
        - Rock loses to paper
        - Paper loses to Scissors
        - Scissors loses to Rock
        """
        self.assertEqual(self.game.determine_winner("scissors", "rock"), "computer")
        self.assertEqual(self.game.determine_winner("paper", "scissors"), "computer")
        self.assertEqual(self.game.determine_winner("rock", "paper"), "computer")
    
    def test_tie(self):
        """
        Test all tie scenarios where both user and computer make the same choice.
        """
        self.assertEqual(self.game.determine_winner("rock", "rock"), "tie")
        self.assertEqual(self.game.determine_winner("paper", "paper"), "tie")
        self.assertEqual(self.game.determine_winner("scissors", "scissors"), "tie")

if __name__ == "__main__":
    unittest.main()
