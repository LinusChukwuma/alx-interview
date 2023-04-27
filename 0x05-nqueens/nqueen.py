#!/usr/bin/env python3
import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(error):
    print(error)
    sys.exit(1)


if len(sys.argv) != 2:
    print_usage_and_exit()

try:
    N = int(sys.argv[1])
except ValueError:
    print_error_and_exit("N must be a number")

if N < 4:
    print_error_and_exit("N must be at least 4")

board = [[0] * N for _ in range(N)]


def is_attack(i, j):
    # checking if there is a queen in row or column
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # checking diagonals
    for k in range(N):
        for l in range(N):
            if k + l == i + j or k - l == i - j:
                if board[k][l] == 1:
                    return True
    return False


def solve_n_queens(n, solutions):
    # if n is 0, solution found
    if n == 0:
        solutions.append([board[i][:] for i in range(N)])
        return
    for i in range(N):
        for j in range(N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if not is_attack(i, j) and board[i][j] != 1:
                board[i][j] = 1
                # recursion
                # wether we can put the next queen with this arrangment or not
                solve_n_queens(n - 1, solutions)
                board[i][j] = 0


solutions = []
solve_n_queens(N, solutions)
for solution in solutions:
    print(solution)
