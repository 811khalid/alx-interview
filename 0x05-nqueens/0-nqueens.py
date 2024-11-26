#!/usr/bin/python3
'''N Queens Challenge'''

import sys


def solve_nqueens(n):

    solutions = []
    placed_queens = []

    def backtrack(row):
        if row == n:
            solutions.append(placed_queens[:])
            return

        for col in range(n):
            if is_safe(row, col):
                placed_queens.append([row, col])
                backtrack(row + 1)
                placed_queens.pop()

    def is_safe(row, col):
        for r, c in placed_queens:
            if c == col or r - c == row - col or r + c == row + col:
                return False
        return True

    backtrack(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
