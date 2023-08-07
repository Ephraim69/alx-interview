#!/usr/bin/python3

"""
Solution for N-Queens problem
"""

import sys

def valid_position(chessboard, x, y, size):
    """
    Check if a queen can be placed at (x, y) without being attacked.
    """
    for i in range(x):
        if (chessboard[i] == y or 
            chessboard[i] - i == y - x or 
            chessboard[i] + i == y + x):
            return False
    return True

def solve(chessboard, x, size):
    """
    Recursively attempt to place a queen in a valid spot.
    """
    if x == size:
        print([[i, chessboard[i]] for i in range(size)])
        return

    for y in range(size):
        if valid_position(chessboard, x, y, size):
            chessboard[x] = y
            solve(chessboard, x + 1, size)

def main(size):
    """
    Main function to kick off the solution.
    """
    if size < 4:
        print("Size should be 4 or more.")
        sys.exit(1)
    
    chessboard = [-1 for _ in range(size)]
    solve(chessboard, 0, size)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Correct usage: script_name <board size>")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the board size.")
        sys.exit(1)
    main(board_size)
