#!/usr/bin/python3
"""
N queens
"""
import sys


def is_safe(board, row, col, n):
    return not any(
        board[i] == col or abs(board[i] - col) == abs(i - row)
        for i in range(row)
    )


def n_queens_util(board, row, n):
    # Recursive utility function to find all solutions to the N queens problem
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            n_queens_util(board, row + 1, n)


def n_queens(n):
    # Wrapper function to find all solutions to the N queens problem
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    n_queens_util(board, 0, n)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    n_queens(n)
