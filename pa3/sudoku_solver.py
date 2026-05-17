"""PA3 starter: solve Sudoku puzzles using SAT."""

from __future__ import annotations

import ast
import sys

from sat_solver import sat_solve


def varnum(row, col, digit):
    """Encode (row, col, digit) as one positive SAT variable.

    row, col, and digit are all 1-based numbers in {1, ..., 9}.
    """
    return 100 * row + 10 * col + digit


def exactly_one(literals):
    """Return CNF clauses expressing that exactly one literal is true."""
    clauses = [list(literals)]

    # At most one: for every pair, not both can be true.
    for i in range(len(literals)):
        for j in range(i + 1, len(literals)):
            clauses.append([-literals[i], -literals[j]])

    return clauses


def sudoku_encode(grid):
    """Encode a 9 x 9 Sudoku grid as CNF.

    A 0 in the grid means an empty cell.
    """
    clauses = []

    for row in range(1, 10):
        for col in range(1, 10):
            cell_vars = [varnum(row, col, digit) for digit in range(1, 10)]
            clauses.extend(exactly_one(cell_vars))

            given = grid[row - 1][col - 1]
            if given != 0:
                clauses.append([varnum(row, col, given)])

    for row in range(1, 10):
        for digit in range(1, 10):
            row_vars = [varnum(row, col, digit) for col in range(1, 10)]
            clauses.extend(exactly_one(row_vars))

    for col in range(1, 10):
        for digit in range(1, 10):
            col_vars = [varnum(row, col, digit) for row in range(1, 10)]
            clauses.extend(exactly_one(col_vars))

    for box_row in range(3):
        for box_col in range(3):
            for digit in range(1, 10):
                box_vars = [
                    varnum(r, c, digit)
                    for r in range(3 * box_row + 1, 3 * box_row + 4)
                    for c in range(3 * box_col + 1, 3 * box_col + 4)
                ]
                clauses.extend(exactly_one(box_vars))

    return clauses


def decode_solution(assignment):
    """Convert a satisfying SAT assignment back into a Sudoku grid."""
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for row in range(1, 10):
        for col in range(1, 10):
            for digit in range(1, 10):
                if assignment.get(varnum(row, col, digit)) is True:
                    grid[row - 1][col - 1] = digit
                    break
    return grid


def solve(grid):
    """Return a solved Sudoku grid, or None if the puzzle is unsolvable."""
    assignment = sat_solve(sudoku_encode(grid), {})
    if assignment is None:
        return None
    return decode_solution(assignment)


def print_result(solution):
    """Print the Sudoku result using the assignment handout format."""
    print(f'solvable: {str(solution is not None).lower()}')
    if solution is None:
        print('solution: None')
        return

    print('solution:')
    for row in solution:
        print(row)


def main():
    """Run the Sudoku solver from the command line on one grid."""
    raw = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    grid = ast.literal_eval(raw)
    print_result(solve(grid))


if __name__ == '__main__':
    main()
