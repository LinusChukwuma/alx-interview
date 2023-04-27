#!/usr/bin/env python3

import sys


def is_attack(i, j, board, N):
    # checking if there is a queen in row or column
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # checking diagonals
    for k in range(N):
        for l in range(N):
            if (k+l == i+j) or (k-l == i-j):
                if board[k][l] == 1:
                    return True
    return False


def N_queen(n, board, N):
    # if n is 0, solution found
    if n == 0:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        return [solution]

    solutions = []
    for i in range(N):
        for j in range(N):
            # checking if we can place a queen here or not
            # queen will not be placed if the place is being attacked
            # or already occupied
            if not(is_attack(i, j, board, N)) and board[i][j] == 0:
                board[i][j] = 1
                # recursion
                # whether we can put the next queen with this arrangement or not
                res = N_queen(n-1, board, N)
                if res != []:
                    for sol in res:
                        solutions.append(sol)
                board[i][j] = 0

    return solutions


if __name__ == '__main__':
    # parsing command line arguments
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [[0]*N for _ in range(N)]

    solutions = N_queen(N, board, N)

    for sol in solutions:
        print(sol)
