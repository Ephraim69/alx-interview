#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n, solutions):
    if col >= n:
        solutions.append([row[:] for row in board])  # deep copy of the board
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0  # backtrack

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

def format_solutions(solutions):
    formatted_solutions = []
    for solution in solutions:
        current_solution = []
        for i in range(len(solution)):
            for j in range(len(solution[i])):
                if solution[i][j] == 1:
                    current_solution.append([i, j])
        formatted_solutions.append(current_solution)
    return formatted_solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_nqueens(N)
    formatted_solutions = format_solutions(solutions)
    for solution in formatted_solutions:
        print(solution)
