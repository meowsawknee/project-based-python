def create_players() -> tuple[str, str]:
    """Prompt players to enter their names and return them as a tuple."""
    print("\n🧑‍🤝‍🧑 Multiplayer Mode Activated!")
    player1 = input("Enter name for Player 1: ").strip()
    player2 = input("Enter name for Player 2: ").strip()
    return player1 or "Player 1", player2 or "Player 2"
