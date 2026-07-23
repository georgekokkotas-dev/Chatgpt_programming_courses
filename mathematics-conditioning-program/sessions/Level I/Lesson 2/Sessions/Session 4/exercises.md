# MCP — Level I · Lesson I.2 · Session I.2.4

## Part 2 — Exercises

**Student:** George Kokkotas  
**Energy/Fatigue:** E5 / F2  
**Mode:** High-energy, moderate-fatigue review  
**Session type:** Review, mini-assessment, mastery evaluation, and lesson archive  
**Theme:** Formal Mathematical Language, Symbolic Verification, Algorithms, Databases, and Research Interpretation

## Submission order

M1–M4 Mandatory Core  
R1–R4 Recommended  
S1–S3 Stretch  
RI1–RI2 Research Integration

## Rules

- Do not look for solutions before attempting.
- Show legal operations, not only final answers.
- Preserve original-domain restrictions.
- Distinguish model domain from supplied-value classification.
- Distinguish a non-negative quantity from a negative rate of change.
- Use \(=\) for exact equality and \(\approx\) only for approximation.
- Applied answers must follow:
  \[
  \text{Object}\rightarrow\text{Result}\rightarrow\text{Interpretation}
  \rightarrow\text{Limitation}\rightarrow\text{Condition/Scope}.
  \]
- Algorithm answers must include Input, Output, Procedure, Correctness, Termination, and Complexity.
- Database answers must identify tables, row meaning, primary keys, and foreign keys.
- Record programming problems separately as **Programming Gaps**.
- Optional work may be marked **Not Attempted due to time/fatigue**.

---

# Mandatory Core

## M1 — Informal-to-Formal Mathematical Language Audit

**Active Blocks:** Mathematical Language, Scientific Writing, Logic  
**Track:** Mathematical and scientific communication  
**Difficulty:** Hard  
**Type:** L — Manual Learning  
**Status:** Mandatory  
**Language:** Written mathematics and scientific English  
**Topic Tags:** formalization, domains, rates of change, interpretation, limitations  
**Category:** Mandatory Core

For every statement, provide:

1. symbolic form where appropriate;
2. one precise mathematical sentence;
3. one precise scientific sentence;
4. required assumptions or conditions;
5. one inference that must not be made.

Statements:

1. “The magnitude cannot be negative, but it can go down.”
2. “These particular values are rational, but the model variables may take other real values.”
3. “Squaring gets rid of the negative sign.”
4. “Cancelling a factor does not make the forbidden input legal.”
5. “The calculation gives exactly \(1\), not roughly \(1\).”
6. “Two different signed-effect pairs can have the same magnitude.”

Required format:

```text
Informal statement:
Symbolic form:
Formal mathematical statement:
Formal scientific statement:
Conditions:
Invalid inference to avoid:
```

Permitted sentence frames:

- “For every ___ in the domain ___, the quantity ___ satisfies ___.”
- “In the supplied numerical instance, ___; however, the model variable is defined over ___.”
- “The transformation preserves ___ but does not preserve ___.”
- “The conclusion holds provided that ___.”

**Expected output:** Six complete formalization blocks.

---

## M2 — Lesson I.2 Symbolic Mini-Assessment

**Active Blocks:** Numbers, Arithmetic, Algebra, Logic  
**Track:** Manual symbolic mathematics  
**Difficulty:** Hard  
**Type:** D+L — Manual Drill and Learning  
**Status:** Mandatory  
**Language:** Written mathematics  
**Topic Tags:** exponent bases, principal roots, factorization, restrictions, exactness  
**Category:** Mandatory Core

For every item:

1. identify every exponent base;
2. state the legal operation order;
3. simplify completely;
4. record restrictions before cancellation;
5. classify numerical results in the smallest applicable set;
6. write one independent final-line check.

\[
\text{a. }-4^2+\sqrt{81}
\]

\[
\text{b. }(-4)^2-\sqrt{81}
\]

\[
\text{c. }\sqrt{(-7)^2}-3
\]

\[
\text{d. }\frac{\sqrt{75}}{\sqrt3}
\]

\[
\text{e. }\frac{x^2-36}{x-6}
\]

\[
\text{f. }\frac{a^2-9}{a+3}
\]

\[
\text{g. }\sqrt{(m+5)^2}
\]

\[
\text{h. }102(0.25)^2
\]

For e–f, also state:

- the factorization identity;
- the excluded value;
- the final form with its inherited restriction;
- why the unrestricted simplified appearance is not fully equivalent to the original.

For h, decide between \(=\) and \(\approx\).

**Expected output:** Eight audited transformations.

---

## M3 — Algorithm-Theory Audit of a Mathematical Solution

**Active Blocks:** Algorithms, Algorithm Theory, Logic, Proof Writing  
**Track:** Pseudocode and correctness reasoning  
**Difficulty:** Harder  
**Type:** L+C  
**Status:** Mandatory  
**Environment:** Pseudocode  
**Topic Tags:** invariant, correctness, termination, complexity  
**Category:** Mandatory Core  
**Side Subject:** Algorithms and Algorithm Theory

A solution is stored as an ordered list of \(k\) lines.

Design an algorithm named:

```text
AUDIT_SOLUTION
```

It must check for:

- exponent-base changes;
- lost unary minus signs;
- illegal radical transformations;
- lost domain restrictions;
- incorrect \(\pm\);
- incorrect \(=\) versus \(\approx\);
- final arithmetic inconsistencies.

Complete:

1. define the input;
2. define the output;
3. write pseudocode;
4. state a loop invariant after lines \(1,\ldots,j\) have been checked;
5. prove initialization;
6. explain maintenance;
7. explain why termination produces a valid conclusion;
8. state worst-case complexity in terms of \(k\);
9. state one limitation.

Apply the algorithm manually to:

```text
√64
= ±8
= -8
```

and:

```text
(x² - 16)/(x - 4)
= (x - 4)(x + 4)/(x - 4)
= x + 4
```

For each trace, identify:

- the first problematic line;
- the relevant rule;
- whether the issue is mathematical, domain-related, or notation-related.

Skeleton:

```text
FUNCTION AUDIT_SOLUTION(lines, original_domain):
    restrictions ← ...

    FOR j FROM ... TO ...:
        previous_line ← ...
        current_line ← ...

        CHECK ...
        UPDATE ...

        IF violation detected:
            RETURN ...

    CHECK final line ...
    RETURN ...
```

Do not implement M3 in Python or R.

---

## M4 — Dynamic Genetic-Effect Magnitude

**Active Blocks:** Mathematical Biology, Mathematical Modelling, Scientific Writing  
**Track:** Research integration  
**Difficulty:** Harder  
**Type:** A+L  
**Status:** Mandatory  
**Language:** Mathematics and scientific English  
**Topic Tags:** time-dependent magnitude, decay, non-negativity, information loss  
**Category:** Mandatory Core + Research Integration

Let:

\[
g_1(t)=-0.60e^{-0.20t},
\]

\[
g_2(t)=0.80e^{-0.20t},
\]

for:

\[
t\geq0.
\]

Define:

\[
G(t)=\sqrt{g_1(t)^2+g_2(t)^2}.
\]

Complete:

1. assign domains to \(t,g_1,g_2,G\);
2. state which quantities are signed and which are non-negative;
3. state whether they are dimensionless;
4. substitute the component formulas;
5. simplify \(G(t)\) exactly;
6. justify every absolute-value step;
7. prove without differentiation that \(G(t_2)<G(t_1)\) whenever \(t_2>t_1\geq0\);
8. distinguish the sign restriction on \(G(t)\) from its direction of change;
9. calculate \(G(0)\) exactly;
10. calculate \(G(5)\) symbolically and approximately to four places;
11. use \(=\) and \(\approx\) correctly;
12. write a two-sentence interpretation;
13. write one mathematical limitation;
14. write one biological/model limitation;
15. explain why \(G(t)\) cannot reconstruct the ordered signed pair;
16. state that the construction is illustrative rather than validated.

Scaffolding:

- Factor the common time-dependent term after squaring.
- Use \(\sqrt{z^2}=|z|\).
- Compare exponential factors to prove decay.
- Keep “non-negative” separate from “decreasing.”

Required structure:

```text
Object:
Domain:
Exact result:
Approximate result:
Interpretation:
Mathematical limitation:
Biological/model limitation:
Scope statement:
```

---

# Recommended

## R1 — Python and R Computational Verification

**Active Blocks:** Scientific Computing, Programming Commands, Numbers  
**Track:** Python and R  
**Difficulty:** Moderate  
**Type:** C+A  
**Status:** Recommended  
**Topic Tags:** dynamic magnitude, floating point, verification  
**Category:** Recommended

Python:

```python
from math import sqrt, exp

def magnitude(g1, g2):
    return ...

times = [0, 1, 5, 10]

for t in times:
    g1 = -0.60 * exp(-0.20 * t)
    g2 =  0.80 * exp(-0.20 * t)
    G = ...
    print(t, g1, g2, G)
```

R:

```r
magnitude <- function(g1, g2) {
  ...
}

times <- c(0, 1, 5, 10)

for (t in times) {
  g1 <- -0.60 * exp(-0.20 * t)
  g2 <-  0.80 * exp(-0.20 * t)
  G <- ...
  print(c(t = t, g1 = g1, g2 = g2, G = G))
}
```

Submit:

- completed code and output for both languages;
- hand-derived \(G(0)\);
- verification of non-negativity;
- verification of decay;
- explanation of exact mathematics versus floating-point output;
- Programming Gaps.

---

## R2 — Database Design for MCP Gap Tracking

**Active Blocks:** Databases, Structured Data, Mathematical Language  
**Track:** SQL  
**Difficulty:** Moderate  
**Type:** C+L  
**Status:** Recommended  
**Topic Tags:** primary keys, foreign keys, normalization, queries  
**Category:** Recommended  
**Side Subject:** Databases

Design tables for:

- `session`
- `exercise`
- `gap`
- `correction`

Complete:

1. columns and data types;
2. primary keys;
3. foreign keys;
4. meaning of one row in each table;
5. reason session data should not be repeated in each gap row;
6. `CREATE TABLE` statements;
7. an `INSERT` for I.2.4 with Energy 5 and Fatigue 2;
8. an `INSERT` for a Formal-Language Gap;
9. a query returning open I.2.4 gaps;
10. a query counting gaps by type;
11. two integrity constraints;
12. one schema limitation.

Do not place several gap types inside one comma-separated field.

---

## R3 — Formal Scientific Reporting Drill

**Active Blocks:** Scientific Writing, Mathematical Language, Modelling  
**Track:** Scientific English  
**Difficulty:** Hard  
**Type:** L+A  
**Status:** Recommended  
**Topic Tags:** interpretation, limitation, scope  
**Category:** Recommended

For each case, write exactly five sentences:

1. object/definition;
2. result;
3. interpretation;
4. limitation;
5. condition or scope.

### Case A

\[
I=\sqrt{2^2+5^2}
\]

### Case B

A population changes from \(800\) to \(920\).

### Case C

The signed pair is:

\[
(-3,4)
\]

with magnitude \(5\).

### Case D

A non-negative magnitude \(G(t)\) decreases over time.

Requirements:

- distinguish exact from approximate;
- distinguish absolute from relative change;
- distinguish vector from magnitude;
- distinguish value from rate of change;
- avoid unsupported causal claims.

---

## R4 — Restriction and Equivalence Ledger

**Active Blocks:** Algebra, Logic, Mathematical Language  
**Track:** Manual symbolic mathematics  
**Difficulty:** Hard  
**Type:** D+L  
**Status:** Recommended  
**Topic Tags:** original domain, cancellation, piecewise forms  
**Category:** Recommended

For each expression:

1. state the original domain;
2. simplify legally;
3. maintain a restriction ledger;
4. state the simplified expression’s apparent domain;
5. determine equivalence on the original domain and on all reals;
6. write a formal conclusion.

\[
\text{a. }\frac{x^2-25}{x-5}
\]

\[
\text{b. }\frac{x^2+5x}{x}
\]

\[
\text{c. }\sqrt{(x-4)^2}
\]

\[
\text{d. }\frac{\sqrt{(x-4)^2}}{x-4}
\]

\[
\text{e. }\frac{x-7}{x-7}
\]

---

# Stretch

## S1 — Proof by Cases with Formal Prose

**Active Blocks:** Proof Writing, Logic, Numbers, Mathematical Language  
**Track:** Manual proof  
**Difficulty:** Harder  
**Type:** L  
**Status:** Stretch  
**Topic Tags:** absolute value, principal root, proof by cases  
**Category:** Stretch

Prove:

\[
\sqrt{x^2}=|x|
\]

for every real \(x\).

Use:

- Case 1: \(x\geq0\)
- Case 2: \(x<0\)

Also explain:

- why checking \(x=4\) and \(x=-4\) is not a universal proof;
- why \(\sqrt{x^2}=x\) is false in general;
- how to state the identity in publication-style prose.

---

## S2 — Correctness Proof for the Audit Algorithm

**Active Blocks:** Algorithms, Proof Writing, Logic  
**Track:** Algorithm theory  
**Difficulty:** Harder  
**Type:** L  
**Status:** Stretch  
**Topic Tags:** partial correctness, total correctness, invariant  
**Category:** Stretch  
**Side Subject:** Algorithms and Algorithm Theory

Using M3:

1. define partial correctness;
2. define termination;
3. explain total correctness;
4. strengthen the loop invariant;
5. prove initialization;
6. prove maintenance;
7. prove termination;
8. give an example a purely syntactic auditor might wrongly accept;
9. explain why symbolic validation is harder than line counting;
10. distinguish scanning complexity from mathematical-validation complexity.

---

## S3 — Composite Piecewise Audit

**Active Blocks:** Algebra, Logic, Functions, Scientific Writing  
**Track:** Symbolic mathematics  
**Difficulty:** Very Hard  
**Type:** D+L  
**Status:** Stretch  
**Topic Tags:** absolute value, factorization, restrictions, piecewise functions  
**Category:** Stretch

Let:

\[
F(x)=\sqrt{(x-2)^2}+\frac{x^2-4}{x-2}.
\]

Complete:

1. original domain;
2. radical simplification;
3. factorization;
4. inherited restriction;
5. piecewise form;
6. \(F(-1),F(2),F(5)\), where legal;
7. whether one linear expression represents \(F\) over its whole domain;
8. why substitution of \(x=2\) into the simplified appearance is misleading;
9. one formal interpretation and one warning.

Scaffolding:

- Start with \(|x-2|\).
- Separate \(x\geq2\) and \(x<2\).
- Preserve \(x\neq2\).

---

# Research Integration

## RI1 — Multi-Component Decaying Genetic-Effect Vector

**Active Blocks:** Mathematical Biology, Modelling, Scientific Computing  
**Track:** Research integration  
**Difficulty:** Very Hard  
**Type:** A+L  
**Status:** Research Integration  
**Topic Tags:** vector norm, decay, computation, interpretation  
**Category:** Research Integration

Let:

\[
\mathbf g(t)=
\left(
-0.40e^{-0.10t},
0.30e^{-0.10t},
-0.20e^{-0.10t},
0.10e^{-0.10t}
\right),
\]

for \(t\geq0\), and define:

\[
G(t)=\|\mathbf g(t)\|_2.
\]

Complete:

1. definitions, domains, and units;
2. exact derivation of \(G(t)\);
3. justification of radical and absolute-value steps;
4. proof of non-negativity;
5. proof of decay without differentiation;
6. \(G(0)\) exactly;
7. \(G(10)\) symbolically and approximately;
8. Python or R implementation;
9. printed squared components, sum, and magnitude;
10. verification at \(t=0,5,10,20\);
11. formal interpretation;
12. mathematical and biological limitations;
13. information lost by replacing \(\mathbf g(t)\) with \(G(t)\);
14. statement that the measure is illustrative rather than validated.

---

## RI2 — Audit-Ready \(dN_{gi}/dt\) Model

**Active Blocks:** Genomic Modelling, Algorithms, Databases, Scientific Writing  
**Track:** Research integration  
**Difficulty:** Very Hard  
**Type:** A+C+L  
**Status:** Research Integration  
**Environment:** Mathematics, pseudocode, Python or R, and SQL  
**Topic Tags:** logistic model, validation, simulation database  
**Category:** Research Integration  
**Side Subjects:** Algorithms and Databases

Consider:

\[
\frac{dN_{gi}}{dt}
=
r_{\mathrm{dem}}G(t)N\left(1-\frac NK\right),
\]

where:

\[
G(t)=\sqrt{g_1(t)^2+g_2(t)^2},
\]

\[
r_{\mathrm{dem}}=0.03\text{ per year},
\]

\[
g_1(t)=-0.60e^{-0.20t},
\qquad
g_2(t)=0.80e^{-0.20t},
\]

\[
N=600,\qquad K=1000,\qquad t\geq0.
\]

Do not solve the differential equation.

### A. Mathematics

- Define every symbol.
- Assign domains, restrictions, and units.
- Derive \(G(t)\).
- Evaluate the logistic factor.
- Evaluate the rate at \(t=0\) and \(t=5\).
- Interpret its sign and changing magnitude.
- Explain \(N=K\) and \(N>K\).
- Explain the distortion caused by replacing the signed vector with \(G(t)\).
- State at least two limitations.

### B. Algorithm

Write pseudocode containing:

```text
INPUTS
DOMAIN CHECKS
RESTRICTION CHECKS
MAGNITUDE CALCULATION
LOGISTIC-FACTOR CALCULATION
RATE CALCULATION
FINAL AUDIT
OUTPUT
```

Also state:

- one invariant or postcondition;
- complexity for one evaluation;
- one algorithmic limitation.

### C. Programming

Implement one evaluation in Python or R.

- Print intermediate values.
- Reject invalid inputs.
- Use a clear error message.

### D. Database

Design:

```text
simulation_result
```

with at least:

```text
run_id
t
r_dem
g1
g2
G
N
K
logistic_factor
rate
model_status
```

Provide:

- primary key;
- data types;
- `CREATE TABLE`;
- an `INSERT` for \(t=0\);
- a query returning positive-rate runs;
- one integrity constraint;
- an explanation of why intermediate values improve reproducibility.

### E. Formal reporting

Write:

1. one result sentence;
2. one interpretation sentence;
3. one mathematical limitation sentence;
4. one biological limitation sentence;
5. one statement that the model and values are simulated and illustrative.

---

# END OF EXERCISES

**Exactly 13 exercises assigned. No solutions or answer key included.**