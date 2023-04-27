#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col] given the current
    state of the board.
    """
    # Check row on left side
    for i in range(col):
        if board[row][i]:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solve_n_queens(n):
    """
    Solve the n queens problem using backtracking.

    Return a list of solutions.
    Each solution is a list of row indices for each column index, e.g.
    [0, 2, 4, 1, 3] represents the board:
    Q _ _ _ _
    _ _ Q _ _
    Q _ _ _ _
    _ Q _ _ _
    _ _ Q _ _
    """
    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []

    def backtrack_n_queens(col):
        """
        Recursively place queens on the board column by column.
        When a solution is found (i.e. we have placed n queens), add it to the
        list of solutions.
        """
        nonlocal board
        if col == n:
            # We have placed n queens (0, 1, ..., n-1) so we have a solution.
            # Don't use board.copy() here since the inner lists are still shared
            # and we'll modify the same list object in subsequent iterations.
            solutions.append([row.index(1) for row in board])
            return

        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack_n_queens(col + 1)
                board[row][col] = 0

    backtrack_n_queens(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)

    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])
