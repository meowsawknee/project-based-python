import os

HIGH_SCORE_FILE = "data/high_score.txt"

def load_high_score() -> int:
    """Load the highest score from file. Return 0 if file doesn't exist."""
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except:
        return 0
    

def save_high_score(score: int) -> None:
    """Save the new high score to file."""
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))
