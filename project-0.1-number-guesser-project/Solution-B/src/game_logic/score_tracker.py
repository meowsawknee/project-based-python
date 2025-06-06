import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
HIGH_SCORE_FILE = os.path.join(DATA_DIR, "high_score.txt")

def load_high_score() -> int:
    """Load the highest score from the file. Returns 0 if file doesn't exist or is invalid."""
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except ValueError:
        return 0

def save_high_score(score: int) -> None:
    """Save the new high score to the file. Creates the directory if it doesn't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))
