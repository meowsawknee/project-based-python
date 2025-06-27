import random
from typing import List


def get_ai_move(empty_cells: List[int]) -> int:
    """
    Chooses a random move for the AI from the list of available empty cells.

    Args:
        empty_cells (List[int]): List of cell indices that are currently empty

    Returns:
        int: The cell number chosen by the AI
    """
    return random.choice(empty_cells)
