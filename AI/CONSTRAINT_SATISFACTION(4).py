def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_bt_all(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_bt_all(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_n_queens_bb_all(row, n, board, columns, left_diag, right_diag, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if columns[col] or left_diag[row - col] or right_diag[row + col]:
            continue
        board[row][col] = 1
        columns[col] = left_diag[row - col] = right_diag[row + col] = True
        solve_n_queens_bb_all(row + 1, n, board, columns, left_diag, right_diag, solutions)
        board[row][col] = 0
        columns[col] = left_diag[row - col] = right_diag[row + col] = False

def print_solutions(solutions, method_name):
    print(f"\n{method_name} found {len(solutions)} solution(s):")
    for idx, board in enumerate(solutions, start=1):
        print(f"\nSolution {idx}:")
        for row in board:
            print(" ".join("Q" if col == 1 else "." for col in row))

# MAIN PROGRAM
n = int(input("Enter the number of queens (N): "))

# --- Backtracking ---
board_bt = [[0 for _ in range(n)] for _ in range(n)]
solutions_bt = []
solve_n_queens_bt_all(board_bt, 0, n, solutions_bt)
print_solutions(solutions_bt, "Backtracking")

# --- Branch and Bound ---
board_bb = [[0 for _ in range(n)] for _ in range(n)]
solutions_bb = []
columns = [False] * n
left_diag = [False] * (2 * n)
right_diag = [False] * (2 * n)
solve_n_queens_bb_all(0, n, board_bb, columns, left_diag, right_diag, solutions_bb)
print_solutions(solutions_bb, "Branch and Bound")
