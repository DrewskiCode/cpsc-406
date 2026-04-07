# CPSC 406 Midterm Study Sheet (HW 1–5)

This sheet is designed to be fast to review and easy to apply on exam-style questions.

---

## 1) Core ideas you must know

- **DFA**: exactly one next state per input symbol.
- **NFA**: can have multiple next states for one symbol.
- **Regular language**: can be recognized by some DFA/NFA, or described by a regular expression.
- **Key equivalence**: DFA, NFA, and regular expressions have the same expressive power.

---

## 2) DFA basics (HW1)

### Acceptance rule
Given DFA \(A=(Q,\Sigma,\delta,q_0,F)\):
- A string \(w\) is accepted iff
  \[
  \hat\delta(q_0,w)\in F.
  \]

### Extended transition function
- \(\hat\delta(q,\varepsilon)=q\)
- \(\hat\delta(q,xa)=\delta(\hat\delta(q,x),a)\)

### Common construction patterns

1. **Ends with pattern** (example: ends with \(ab\))
   - Track the longest useful suffix.
2. **Contains pattern** (example: contains \(aba\), contains \(100\))
   - Use progress states: matched 0,1,2,… chars.
   - Usually final state is an accepting sink.
3. **Parity/count mod \(k\)**
   - Use states for remainders (ex: even/odd).
   - For two independent parity conditions, use product of parities (4 states).

### Quick exam tip
If language says “odd/even number of symbols,” think **mod arithmetic** in states.

---

## 3) Product automata (HW2)

For DFAs
\[
A_1=(Q_1,\Sigma,\delta_1,q_1,F_1),\quad
A_2=(Q_2,\Sigma,\delta_2,q_2,F_2),
\]
build product DFA:
\[
Q=Q_1\times Q_2,\quad q_0=(q_1,q_2),\quad
\delta((p,r),a)=(\delta_1(p,a),\delta_2(r,a)).
\]

### Accepting states
- **Intersection** \(L_1\cap L_2\):
  \[
  F=F_1\times F_2.
  \]
- **Union** \(L_1\cup L_2\):
  \[
  F=\{(p,r): p\in F_1\ \text{or}\ r\in F_2\}.
  \]
- **Complement** (for DFA): flip accepting/non-accepting states.

### De Morgan useful identity
\[
L_1\cup L_2=\overline{\overline{L_1}\cap\overline{L_2}}.
\]

---

## 4) NFA to DFA determinization (HW3)

### Subset (powerset) construction
If NFA has states \(Q\), DFA states are subsets of \(Q\).

- Start state: \(\{q_0\}\)
- Transition:
  \[
  \delta_D(S,a)=\bigcup_{q\in S}\delta_N(q,a).
  \]
- Accepting subsets:
  \[
  S\ \text{is accepting iff}\ S\cap F_N\neq\emptyset.
  \]

### Memory trick
A DFA state in subset construction means: “all NFA states we could currently be in.”

---

## 5) DFA minimization + equivalence (HW3/HW4)

### Table-filling algorithm
1. List all unordered state pairs.
2. Mark every pair where one is accepting and the other is not.
3. Repeatedly mark pair \((p,q)\) if for some symbol \(a\), pair
   \((\delta(p,a),\delta(q,a))\) is already marked.
4. Unmarked pairs are equivalent (can merge).

### Equivalent DFAs test
Two DFAs are equivalent iff their start states are not distinguishable (or equivalently, symmetric difference language is empty).

---

## 6) Regular expressions + Kleene-style reasoning (HW3/HW4)

### Common regex pieces
- \(a^*\): zero or more \(a\)
- \(a^+\): one or more \(a\)
- Union: \(R+S\)
- Concatenation: \(RS\)

### From automata behavior to regex
- “Any mix of \(a,b\)” → \((a+b)^*\)
- “Then an \(a\), then \(b\) or \(c\)” → \((a+b)^*a(b+c)\)

### Kleene algorithm recurrence (important formula)
\[
R_{ij}^{(k)} = R_{ij}^{(k-1)} + R_{ik}^{(k-1)}\big(R_{kk}^{(k-1)}\big)^*R_{kj}^{(k-1)}.
\]
Use this when asked to compute regex by intermediate states.

---

## 7) Induction pattern on automata (HW3)

If a state \(q\) has \(\delta(q,a)=q\) for all symbols \(a\), then for every string \(w\):
\[
\hat\delta(q,w)=q.
\]

### Proof skeleton
- Base case \(w=\varepsilon\).
- Induction step: write \(x=wa\), apply definition of \(\hat\delta\), then induction hypothesis.

Use this exact structure when proving DFA properties by length.

---

## 8) Pumping Lemma strategy for non-regularity (HW5)

### Statement (memorize)
If \(L\) is regular, then \(\exists p\) such that every \(s\in L\), \(|s|\ge p\), can be written
\[
s=xyz,
\quad |xy|\le p,
\quad |y|\ge 1,
\quad xy^iz\in L\ \forall i\ge 0.
\]

### Standard contradiction template
1. Assume \(L\) regular with pumping length \(p\).
2. Choose a specific hard string \(s\in L\), \(|s|\ge p\).
3. Force \(y\) into a controlled region using \(|xy|\le p\).
4. Pick \(i\) (often \(0\) or \(2\)) so pumped string breaks language rule.
5. Contradiction ⇒ \(L\) not regular.

### Typical choices from HW5
- \(L=\{a^nb^m:n>m\}\): pick \(a^{p+1}b^p\), pump down.
- \(L=\{a^{n^2}\}\): pick \(a^{p^2}\), pump up; land between consecutive squares.
- \(L=\{a^q:q\text{ prime}\}\): pump to composite length.
- \(L=\{a^kb^ma^{k+m}\}\): pump first \(a\)-block, break final block relation.

---

## 9) Fast “what method should I use?” guide

- “Build machine for pattern/count condition” → design **DFA**.
- “Combine two languages with and/or” → **product construction**.
- “Given NFA, make DFA” → **subset construction**.
- “Are two DFAs same language?” → **table-filling / minimization**.
- “Convert automaton to regex” → **Kleene recurrence** or pattern recognition.
- “Show language not regular” → **Pumping Lemma contradiction**.

---

## 10) Last-minute checklist before midterm

- Can you compute \(\hat\delta(q_0,w)\) quickly?
- Can you define product states and accepting set correctly?
- Can you do subset transitions as unions of NFA moves?
- Can you run at least 2 rounds of table-filling without mistakes?
- Can you write a full pumping-lemma contradiction cleanly?

If yes to all five, you are in strong shape for HW1–HW5 style questions.
