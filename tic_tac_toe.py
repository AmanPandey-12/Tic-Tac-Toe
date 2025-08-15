# Tic Tac Toe Game in Python

def print_board(board):
    print("\n")
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

def is_draw(board):
    return all(cell != " " for cell in board)

def play_game():
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != " ":
                print("Cell already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
