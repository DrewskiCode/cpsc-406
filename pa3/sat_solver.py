"""PA3 SAT solver (from PA2).

Clauses are lists of integer literals. Assignments map variable numbers to booleans.
"""

from __future__ import annotations

import ast
import sys


def literal_variable(literal):
    """Return the variable number appearing in a literal."""
    return abs(literal)


def literal_required_value(literal):
    """Return the value that makes a literal true."""
    return literal > 0


def evaluate_literal(literal, assignment):
    """Evaluate one literal under a partial assignment."""
    variable = literal_variable(literal)
    if variable not in assignment:
        return None
    return assignment[variable] == literal_required_value(literal)


def simplify(clauses, assignment):
    """Simplify clauses under a partial assignment."""
    simplified = []
    for clause in clauses:
        new_clause = []
        clause_satisfied = False

        for literal in clause:
            value = evaluate_literal(literal, assignment)
            if value is True:
                clause_satisfied = True
                break
            if value is None:
                new_clause.append(literal)

        if clause_satisfied:
            continue
        if len(new_clause) == 0:
            return None
        simplified.append(new_clause)

    return simplified


def unit_propagate(clauses, assignment):
    """Repeatedly apply unit clauses until none remain."""
    while True:
        simplified = simplify(clauses, assignment)
        if simplified is None:
            return None
        clauses = simplified

        unit_clause = next((clause for clause in clauses if len(clause) == 1), None)
        if unit_clause is None:
            return clauses

        literal = unit_clause[0]
        variable = literal_variable(literal)
        value = literal_required_value(literal)
        assignment[variable] = value


def choose_variable(clauses, assignment):
    """Choose an unassigned variable to branch on."""
    for clause in clauses:
        for literal in clause:
            variable = literal_variable(literal)
            if variable not in assignment:
                return variable
    return None


def sat_solve(clauses, assignment):
    """Return a satisfying assignment for clauses, or None if unsatisfiable."""
    assignment = dict(assignment)
    clauses = unit_propagate(clauses, assignment)
    if clauses is None:
        return None
    if not clauses:
        return assignment

    variable = choose_variable(clauses, assignment)
    if variable is None:
        return assignment

    for value in (True, False):
        branch_assignment = dict(assignment)
        branch_assignment[variable] = value
        result = sat_solve(clauses, branch_assignment)
        if result is not None:
            return result

    return None


def print_result(assignment):
    """Print the SAT result using the assignment handout format."""
    print(f'satisfiable: {str(assignment is not None).lower()}')
    print(f'assignment: {assignment}')


def main():
    """Run the solver from the command line on a CNF formula."""
    raw = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    clauses = ast.literal_eval(raw)
    print_result(sat_solve(clauses, {}))


if __name__ == '__main__':
    main()
