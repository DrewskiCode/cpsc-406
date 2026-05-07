# Quiz2 Study Guide — Homeworks 6–10

Scope: material from Week 6 through Week 10 (Turing machines, decidability & r.e., asymptotic notation and sorting, propositional logic and CNF/SAT, resolution/Horn, recurrences and Master Theorem).

---

## Quick cheat-sheet
- Asymptotic notation: `O(g)`, `Ω(g)`, `Θ(g)` — existence of constants (`C`, `c`) and threshold `n0`.
- Master Theorem (standard form): For `T(n)=aT(n/b)+f(n)` compare `f(n)` to `n^{log_b a}`:
  - If `f(n)=O(n^{log_b a - ε})` → `T(n)=Θ(n^{log_b a})`.
  - If `f(n)=Θ(n^{log_b a})` → `T(n)=Θ(n^{log_b a} log n)`.
  - If `f(n)=Ω(n^{log_b a + ε})` and regularity holds → `T(n)=Θ(f(n))`.
- Resolution: resolving clauses `(... x ...)` and `(... ¬x ...)` to eliminate `x`.
- Horn clause: at most one positive literal — unit propagation is linear-time.

---

## Week 6 — Turing machines and decidability
- Topics to know:
  - Single-tape and multi-tape TM high-level constructions (copying, marking, moving, multiple tapes as counters).
  - Typical small TM tasks: add zeros, duplicate string, swap bits, validate formats like `10^n10^m`.
  - Difference between **decidable**, **recognizable (r.e.)**, and **co-r.e.** languages.
  - Techniques to prove decidability or r.e. status (simulate, dovetail, bounding steps).
- Key facts:
  - If both `L1` and `L2` decidable → union/intersection/complement decidable.
  - r.e. languages closed under union (dovetail) but complement need not be r.e.
- Example practice questions:
  - Sketch a TM that given `10^n` outputs `10^{n+1}`.
  - Show a recognizer for `HALT` and argue why it's not decidable.

---

## Week 7 — Decidable vs r.e.; Asymptotic notation
- Topics to know:
  - Definitions: decidable, r.e., co-r.e.; sample languages `L1`, `L2`, `L3` in homework.
  - Using simulation bounds (e.g., halting in ≤k steps) to show decidability.
  - Asymptotic notation manipulations (inclusions, polynomial/exponential comparisons).
  - Sorting runtime classes: `O(n^2)` vs `Θ(n log n)` (bubble, insertion, merge, quicksort).
- Key exercises:
  - Prove `O(n log n) ⊂ O(n^2)` and not vice-versa.
  - Classify a language as decidable / r.e. / co-r.e. (give short reasons).

---

## Week 8 — Propositional logic, CNF, satisfiability
- Topics to know:
  - Convert formulas to CNF using De Morgan, distributivity, implication elimination.
  - Check satisfiability: find satisfying assignment or show contradiction.
  - Common patterns: implications, negations of conjunctions/disjunctions, small CNF examples.
- Practice items:
  - Convert `¬((a ∧ b) ∨ (¬c ∧ d))` to CNF.
  - Decide satisfiability of small CNF formulas and give an assignment or a short contradiction proof.

---

## Week 9 — Resolution, Horn clauses, and policy formalization
- Topics to know:
  - General resolution: resolve complementary literals to derive new clauses; deriving empty clause `⊥` shows unsatisfiable.
  - Unit resolution and unit propagation (especially on Horn formulas).
  - Formalizing English rules as propositional clauses and checking consistency via resolution (example: drone policy and incident log).
- Key techniques:
  - Convert implications `A → B` to CNF: `¬A ∨ B` (for multiple antecedents use `¬(A∧B)∨C` → `¬A∨¬B∨C`).
  - For Horn formulas: repeatedly apply unit clauses to simplify until either contradiction or no change.
- Practice items:
  - Run a sequence of resolution steps to derive `⊥` for a given clause set.
  - Formalize a short safety policy and an incident log, convert to clauses, check consistency.

---

## Week 10 — Recurrences and divide-and-conquer analysis
- Topics to know:
  - Common recurrence patterns: `T(n)=T(n−1)+n`, `T(n)=T(⌈n/2⌉)+1`, `T(n)=2T(⌊n/2⌋)+n`.
  - Techniques: unrolling (telescoping sums), recursion trees, Master Theorem, induction for bounds.
  - How to prove O, Ω, and therefore Θ bounds; role of constants `C` (upper) and `c` (lower) and threshold `n0`.
- Practice items:
  - Unroll `T(n)=T(n−1)+n` and compute closed form; choose constants to prove O(n^2) and Ω(n^2).
  - Use Master Theorem to classify `T(n)=aT(n/b)+f(n)`.
  - Draw a recursion tree for mergesort-style recurrence and compute total work.

---

## Likely quiz question types
- Short definitions: decidable vs r.e.; Horn clause; CNF; Master Theorem cases.
- Small constructions: sketch a TM for a simple string-manipulation task; convert a formula to CNF.
- Short proofs: show a language is non-regular (pumping lemma style) or a recurrence is O( ) / Ω( ).
- Calculations: evaluate a recurrence with unrolling or recursion tree; perform a few resolution steps to find a contradiction.
- Classify languages/problems into decidable/r.e./co-r.e. with short reasoning.

---

## Study tips and priorities (what to master before the quiz)
1. Be able to convert simple formulas to CNF quickly and check satisfiability of small clause sets by inspection or resolution.
2. Practice unrolling 2–3 recurrences (linear decrease, halving, divide-and-conquer splits) and recognize which technique to use.
3. Refresh TM high-level algorithms (copy, mark, multi-tape trick) and know how to argue decidability/r.e. using simulation or dovetailing.
4. Memorize Master Theorem statement and common examples (mergesort, binary search, linear recursion).
5. Do 5–10 short exercises: classification (decidable/r.e.), a tiny TM sketch, CNF transformations, and one resolution derivation.

---

## Quick practice checklist
- [ ] Convert 3 formulas to CNF.
- [ ] Unroll `T(n)=T(n−1)+n` and prove Θ(n^2).
- [ ] Use Master Theorem on `T(n)=2T(n/2)+n`.
- [ ] Simulate a TM for doubling a unary string sample by hand.
- [ ] Do one Horn resolution with unit propagation to derive contradiction.

---

If you want, I can:
- produce a PDF of this guide,
- expand any section into worked examples (with LaTeX-ready math), or
- generate a short randomized quiz (10 questions + answers) for practice.

Good luck — tell me which follow-up you want and I'll generate it (PDF, worked solutions, or practice quiz).