from src.game import TicTacToe
from src.ai import get_ai_move
from colorama import Fore, Style, init


init(autoreset=True) # Auto-reset colors after each print

def play_game() -> None:
    """
    Runs the main game loop for CLI-based Tic Tac Toe.
    Includes scoreboard and replay option, and optional AI opponent.
    """
    score = {"X": 0, "O": 0}  # Track wins for each player

    print(Fore.MAGENTA + "🎮 Welcome to Tic Tac Toe!\n")

    use_ai = input("Do you want to play against AI? (y/n): ").lower() == "y"
    ai_player = None

    if use_ai:
        while True:
            ai_choice = input("Should AI play as 'X' or 'O'? ").upper()
            if ai_choice in ["X", "O"]:
                ai_player = ai_choice
                break
            else:
                print(Fore.RED + "Please enter 'X' or 'O'.")

    while True:
        game = TicTacToe()

        while True:
            show_board(game)
            print(f"{color_for_player(game.player_turn)}Player {game.player_turn}'s turn.")

            if use_ai and game.player_turn == ai_player:
                # Let AI make a move
                print(Fore.BLUE + "AI is thinking...")
                cell = get_ai_move(game.get_empty_cells())
                print(Fore.BLUE + f"AI chooses cell {cell}")
            else:
                try:
                    cell = int(input("Enter a cell number (1-9): "))
                except ValueError:
                    print(Fore.RED + "Invalid input! Please enter a number between 1 and 9.")
                    continue

            if cell in range(1, 10) and game.board[cell] == " ":
                game.fix_spot(cell, game.player_turn)

                if game.has_player_won(game.player_turn):
                    show_board(game)
                    print(Fore.GREEN + f"🎉 Player {game.player_turn} wins!")
                    score[game.player_turn] += 1
                    break

                if game.is_board_filled():
                    show_board(game)
                    print(Fore.CYAN + "It's a draw!")
                    break

                game.swap_player_turn()
            else:
                print(Fore.RED + "Invalid move! Try another cell.")

        # Show score after match ends
        print(f"\nScoreboard: {Fore.CYAN}X = {score['X']} | {Fore.YELLOW}O = {score['O']}")

        # Ask for replay
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print(Fore.MAGENTA + "Thanks for playing!")
            break
            

def color_for_player(player: str) -> str:
    """
    Returns color for a given player symbol.
    """
    return Fore.CYAN if player == "X" else Fore.YELLOW


def show_board(game: TicTacToe) -> None:
    """
    Prints the current state of the board with color-coded player symbols.

    Args:
        game (TicTacToe): The game instance to access its board
    """
    board = game.board
    print("\n")
    for i in [1, 4, 7]:
        row = (
            f"{color_for_player(board[i])}{board[i]}{Style.RESET_ALL}|"
            f"{color_for_player(board[i+1])}{board[i+1]}{Style.RESET_ALL}|"
            f"{color_for_player(board[i+2])}{board[i+2]}{Style.RESET_ALL}"
        )
        print(row)
        if i != 7:
            print("-----")
    print("\n")



if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted by user. Goodbye!")
