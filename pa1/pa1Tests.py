import unittest

from pa1 import format_result, parse_horn_clause_string, solve_horn


class TestPA1(unittest.TestCase):
    def tearDown(self):
        outcome = getattr(self, "_outcome", None)
        result = getattr(outcome, "result", None)

        failed_or_errored = False
        if result is not None:
            all_problem_tests = list(result.failures) + list(result.errors)
            failed_or_errored = any(test_case.id() == self.id() for test_case, _ in all_problem_tests)

        status = "FAILED" if failed_or_errored else "PASSED"
        print(f"{self._testMethodName}: {status}")

    def test_parse_horn_clause_string(self):
        formula = parse_horn_clause_string("[[-a,-b,c],[-c,-d,e],[a]]")

        print("parse_horn_clause_string result:", formula)

        self.assertEqual(formula["variables"], ["a", "b", "c", "d", "e"])
        self.assertEqual(formula["facts"], ["a"])
        self.assertEqual(formula["rules"], [
            {"body": ["a", "b"], "head": "c"},
            {"body": ["c", "d"], "head": "e"},
        ])

    def test_solve_horn_with_fact_only_formula(self):
        formula = {
            "facts": ["a"],
            "rules": [],
        }

        result = solve_horn(formula)

        print("solve_horn result:", result)

        self.assertTrue(result["satisfiable"])
        self.assertEqual(result["true_vars"], {"a"})

    def test_solve_horn_chains_rules(self):
        formula = {
            "facts": ["a"],
            "rules": [
                {"body": ["a"], "head": "b"},
                {"body": ["b"], "head": "c"},
            ],
        }

        result = solve_horn(formula)

        print("solve_horn chained result:", result)

        self.assertTrue(result["satisfiable"])
        self.assertEqual(result["true_vars"], {"a", "b", "c"})

    def test_solve_horn_detects_unsat_constraint(self):
        formula = {
            "facts": ["a"],
            "rules": [
                {"body": ["a"], "head": None},
            ],
        }

        result = solve_horn(formula)

        print("solve_horn unsat result:", result)

        self.assertFalse(result["satisfiable"])

    def test_parse_rejects_non_horn_clause(self):
        with self.assertRaises(ValueError):
            parse_horn_clause_string("[[a,b]]")

    def test_format_result_for_satisfiable_formula(self):
        result = {
            "satisfiable": True,
            "true_vars": {"b", "a"},
        }

        print("format_result input:", result)
        print("format_result output:", format_result(result))

        self.assertEqual(format_result(result), "satisfiable: true\ntrue_vars: a b")


if __name__ == "__main__":
    unittest.main(verbosity=2)
