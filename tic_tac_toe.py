# Simple Tic Tac Toe

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Initialize empty board
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
    print_board(board)
    row = int(input(f"Player {current_player}, enter row (0-2): "))
    col = int(input(f"Player {current_player}, enter col (0-2): "))

    if board[row][col] != " ":
        print("Spot taken, try again.")
        continue

    board[row][col] = current_player

    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break

    if is_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"