from src.game import TicTacToe
from src.ai import get_ai_move


def play_game() -> None:
    """
    Runs the main game loop for CLI-based Tic Tac Toe.
    Includes scoreboard and replay option, and optional AI opponent.
    """
    score = {"X": 0, "O": 0}  # Track wins for each player

    print("Welcome to Tic Tac Toe!\n")

    use_ai = input("Do you want to play against AI? (y/n): ").lower() == "y"
    ai_player = None

    if use_ai:
        while True:
            ai_choice = input("Should AI play as 'X' or 'O'? ").upper()
            if ai_choice in ["X", "O"]:
                ai_player = ai_choice
                break
            else:
                print("Please enter 'X' or 'O'.")

    while True:
        game = TicTacToe()

        while True:
            show_board(game)
            print(f"Player {game.player_turn}'s turn.")

            if use_ai and game.player_turn == ai_player:
                # Let AI make a move
                print("AI is thinking...")
                cell = get_ai_move(game.get_empty_cells())
                print(f"AI chooses cell {cell}")
            else:
                try:
                    cell = int(input("Enter a cell number (1-9): "))
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 9.")
                    continue

            if cell in range(1, 10) and game.board[cell] == " ":
                game.fix_spot(cell, game.player_turn)

                if game.has_player_won(game.player_turn):
                    show_board(game)
                    print(f"🎉 Player {game.player_turn} wins!")
                    score[game.player_turn] += 1
                    break

                if game.is_board_filled():
                    show_board(game)
                    print("It's a draw!")
                    break

                game.swap_player_turn()
            else:
                print("Invalid move! Try another cell.")

        # Show score after match ends
        print(f"\nScoreboard: X = {score['X']} | O = {score['O']}")

        # Ask for replay
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


def show_board(game: TicTacToe) -> None:
    """
    Prints the current state of the board in a user-friendly way.

    Args:
        game (TicTacToe): The game instance to access its board
    """
    board = game.board
    print("\n")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted by user. Goodbye!")
