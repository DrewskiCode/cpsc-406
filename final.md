CPSC-406 — Final Study Guide

This study guide is organized for quick reading and effective review. Focus on the Concept Summary and the Worked Examples sections first, then use the Quick Reference and Practice Problems to test yourself.

1. Core Concepts

- Propositional Logic
  - Formula: built from variables (A, B, C), connectives (¬, ∧, ∨, →, ↔).
  - Truth assignment: maps variables → {True, False}.
  - Satisfiable: there exists an assignment making the formula true. Unsatisfiable: none.

- Conjunctive Normal Form (CNF)
  - CNF is a conjunction (AND) of clauses; a clause is a disjunction (OR) of literals.
  - Literal: variable or its negation (e.g., A or ¬A).
  - Eg: (A ∨ ¬B) ∧ (B ∨ C ∨ ¬D).
  - Conversion: any propositional formula can be converted to CNF (use distributive laws or Tseitin transform for linear size).

- Clauses and Clause Types
  - Unit clause: single literal (e.g., A). Triggers unit propagation.
  - Horn clause: at most one positive literal. Horn-SAT solvable in linear time.
  - Binary clause: exactly two literals (2-SAT is in P).

- Satisfiability (SAT)
  - Decision problem: is a CNF formula satisfiable? NP-complete in general.
  - 2-SAT and Horn-SAT are special polynomial-time cases.

2. SAT Solving Algorithms

- Brute-force search
  - Try all assignments: O(2^n). Use only for tiny n.

- DPLL (Davis–Putnam–Logemann–Loveland)
  - Backtracking search with two core inference rules:
    - Unit propagation (unit clause elimination): assign unit literals to satisfy clauses.
    - Pure literal elimination (optional): assign pure literals to make clauses true.
  - Choose a decision variable, branch on True/False, propagate, backtrack on conflict.
  - Often uses heuristics to pick variables (e.g., choose literal appearing most often).

- Conflict-Driven Clause Learning (CDCL)
  - Modern SAT solvers extend DPLL: when a conflict arises, analyze implication graph, learn a new clause, and backjump.
  - Learning prunes search and makes solvers scale to large instances.
  - Important terms: implication graph, UIP (Unique Implication Point), backjumping, restart, VSIDS heuristic.

- Unit Propagation (Boolean Constraint Propagation)
  - Repeatedly find unit clauses and set their literals true; remove satisfied clauses and remove negated literals from others.
  - Complexity: can be implemented efficiently with watched-literals (amortized linear per propagation sequence).

3. CNF Conversion Tips (Tseitin)

- Naive distribution can blow up formula size. Use Tseitin transformation:
  - Introduce fresh variables for subformulas, add clauses encoding equivalence.
  - Produces CNF linear in the size of the original formula.
  - Useful when encoding circuits and Sudoku constraints.

4. Common Encodings & Examples

- Encoding A → B as CNF: (¬A ∨ B).
- Encoding XOR (A ⊕ B): (A ∨ B) ∧ (¬A ∨ ¬B) is not sufficient for large formulas; use auxiliary variables with Tseitin.
- Sudoku → SAT
  - Variables: X_{r,c,d} true iff cell (r,c) has digit d.
  - Clauses enforce: each cell has at least one digit; at most one digit; row/column/box constraints.
  - Use exactly-one encodings: pairwise mutual exclusion (O(n^2) clauses) or sequential counter encodings for efficiency.

5. Worked Example: Small DPLL Walkthrough

Formula: (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ ¬C) ∧ (A ∨ ¬C)

- No unit clauses initially.
- Decide A = True.
  - Clauses containing A are satisfied: (A ∨ B), (A ∨ ¬C) removed.
  - Remaining: (¬A ∨ C) -> with A=True becomes (C). Unit clause C.
  - Unit propagate C=True.
    - (¬B ∨ ¬C) with C=True becomes (¬B). Unit clause ¬B → B=False.
  - All clauses satisfied → formula is satisfiable with assignment A=True, C=True, B=False.

6. Proof Techniques and Derivations

- Resolution rule (on clauses): from (A ∨ X) and (¬A ∨ Y) infer (X ∨ Y).
  - Resolution refutation: show empty clause derived → unsatisfiable.
  - Keep track of resolvent size; resolution is complete for propositional logic in CNF.

7. Complexity & Theory

- SAT is NP-complete. Understanding reductions (e.g., 3-SAT reductions) is useful for proofs.
- 2-SAT uses implication graphs; strongly connected components identify contradictions (x and ¬x in same SCC → unsat).
- Horn-SAT solvable by linear-time forward-chaining (unit propagation suffices).

8. Practical Solver Tips

- Use unit propagation aggressively; watched-literals implementation is standard.
- Learn simple heuristics: choose variables with high activity (occurrence count), prefer recent conflicts.
- When encoding problems:
  - Keep CNF small: use auxiliary variables (Tseitin) instead of naive expansions.
  - Prefer compact exactly-one encodings for "at most one" constraints.

9. Quick Reference (Cheat Sheet)

- Common formulas:
  - Implication: A → B ≡ (¬A ∨ B)
  - Bi-implication: A ↔ B ≡ (A → B) ∧ (B → A)
  - CNF: AND of ORs
- DPLL steps: decide → propagate → check conflict → backtrack/learn
- Unit propagation: assign units until fixpoint
- Resolution: (A ∨ X), (¬A ∨ Y) ⇒ (X ∨ Y)
- 2-SAT check: build implication graph, check SCCs.

10. Study & Exam Strategy

- Understand core definitions: satisfiable/unsatisfiable, literal, clause, CNF, unit clause.
- Practice: run DPLL by hand on small formulas until unit propagation and backtracking feel natural.
- Do encodings: convert small problems (logic gates, simple Sudoku 4x4) to CNF using Tseitin.
- Memorize common CNF translations (→, ↔, ¬, De Morgan's laws).
- Work through a conflict-driven example: draw implication graph, identify UIP, derive learned clause.

11. Practice Problems (Suggested)

- Convert these to CNF and solve by hand:
  1) (A → (B ∧ C)) ∨ ¬D
  2) (A ⊕ B) ∧ (B → C) ∧ (¬C ∨ A)
  3) Small 4x4 Sudoku encode and check satisfiability.

- Prove unsatisfiable using resolution:
  - Clauses: (A ∨ B), (¬A ∨ B), (A ∨ ¬B), (¬A ∨ ¬B). Show contradiction.

12. Resources & Commands

- Commands useful for working with repository notes:
  - Open in VS Code preview: Command-Shift-V (preview) or Command-K then V (side-by-side).
  - Convert to HTML: `pandoc file.md -s -o file.html` then open.

13. Final Checklist Before Exam

- Can you perform unit propagation quickly by hand?
- Can you convert small boolean formulas to CNF using Tseitin?
- Can you simulate DPLL choices and detect conflicts/backtrack points?
- Do you understand resolution and can produce a short refutation?
- Can you encode a constraint problem (like Sudoku) into CNF and reason about the variable layout?

Good luck — focus practice on unit propagation, CNF conversion, and running DPLL/CDCL examples by hand.
