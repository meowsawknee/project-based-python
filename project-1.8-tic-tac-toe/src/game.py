import random
from typing import List


class TicTacToe:
    """
    A class to represent a Tic Tac Toe game board and its logic.
    """

    def __init__(self) -> None:
        """
        Initializes the game with an empty board and a random starting player.
        """
        self.board: List[str] = [" "] * 10 # index 0 is unused
        self.player_turn: str = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        """
        Randomly selects the first player to start the game.

        Returns:
            str: "X" or "O"
        """
        return random.choice(["X", "O"])
    
    def fix_spot(self, cell: int, player: str) -> None:
        """
        Marks the specified cell on the board with the player's symbol.

        Args:
            cell (int): The board cell number (1 to 9)
            player (str): The player's symbol ("X" or "O")
        """
        self.board[cell] = player

    def is_board_filled(self) -> bool:
        """
        Checks if the game board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return " " not in self.board[1:]
    
    def has_player_won(self, player: str) -> bool:
        """
        Checks if the given player has won the game.

        Args:
            player (str): The player's symbol

        Returns:
            bool: True if the player has a winning combination, False otherwise.
        """
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
            [1, 5, 9], [3, 5, 7]             # diagonals
        ]
        for combination in win_combinations:
            if all(self.board[cell] == player for cell in combination):
                return True
        return False
    
    def swap_player_turn(self) -> None:
        """
        Switches the current player to the other player.
        """
        self.player_turn = "X" if self.player_turn == "O" else "O"

    def reset_board(self) -> None:
        """
        Resets the game board and selects a new random first player.
        """
        self.board = [" "] * 10
        self.player_turn = self.get_random_first_player()

    def get_empty_cells(self) -> list[int]:
        """
        Returns a list of empty cells (used later by AI or GUI)

        Retruns:
            List[int]: List of cell indexes that are empty
        """
        return [i for i in range(1, 10) if self.board[i] == " "]
