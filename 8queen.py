N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_nqueens(board, col):
    if col >= N:
        return True  # All queens are placed

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack

    return False

# Initialize an 8x8 board with the first queen placed
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1  # First queen placed at (0, 0)

if solve_nqueens(board, 1):  # Start solving from the second column
    print("Final 8-Queens Matrix:")
    print_board(board)
else:
    print("No solution exists")
