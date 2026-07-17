# MCP — Level I, Lesson I.1, Session I.1.4

**Session title:** Mathematical Language — Review, Mini-Assessment, Portfolio and Archive  
**Energy:** 5/5  
**Fatigue:** 0/5  
**Mode:** High Performance  
**Status:** Completed and locked  
**Session grade:** 90/100 (A−)  
**Lesson I.1 mastery:** 90%

## Session purpose

This session closed Lesson I.1 by reviewing mathematical objects, expressions, equations, identities, formulas, functions, variables, parameters, constants, domains, units, scientific notation, and the distinction between mathematical statements and programming assignments.

The central lesson rule was:

> A symbol has no scientifically useful meaning until its role, domain, units, and context are sufficiently defined.

## Exercise structure

The session contained exactly 13 exercises:

- 4 Mandatory Core
- 4 Recommended
- 3 Stretch
- 2 Research Integration

George completed Exercises 1–8 and 13. Exercises 9–12 were left unanswered in the submitted working file.

## Correction summary

Most issues concerned precision of terminology rather than conceptual failure.

- `P` is the function name; `P(t)` is the evaluated output or dependent quantity.
- Symbols such as `r`, `P0`, and `m` are parameters when fixed during one model evaluation.
- A proportion or genotype frequency is dimensionless; population counts are measured in individuals.
- `f` is the function, while `f(4)` is the value of the function at the input 4.
- In mathematics, `x = 5` is an equality statement or equation. In Python, `x = 5` is assignment and `x == 5` is comparison.
- Cancellation in `ab/a = b` requires `a != 0`.
- In Python, a function definition requires a colon after the signature.
- Hypothetical statistical values are acceptable in a mock publication-style exercise when clearly marked as simulated or illustrative.

## Mistake log

### 🟥 Mistakes

- Occasional confusion between function name and function value.
- Occasional use of “variable” where “parameter” was more precise.
- Physical units were assigned to a dimensionless proportion.
- The non-zero condition for cancellation was omitted.
- Python function syntax omitted the colon.

### 🟨 Sources of confusion

- Set-builder notation syntax.
- Equality versus assignment versus comparison.
- Poor wording in the genotype-frequency “assumption” requirement.

### 🟦 Correct rules

- Function: `f`; evaluated function value: `f(a)`.
- Set-builder form: `{x in S | condition}`.
- Domain of `(2x+1)/(x-3)`: `{x in R | x != 3}` or `R \ {3}`.
- Frequencies and proportions are dimensionless.
- Division and cancellation require a non-zero denominator.

### 🟩 Fixed examples

```text
D_f = {x in R | x != 3}
```

```python
x = 5      # assignment
x == 5     # comparison
```

```python
def formula(h0, k, t):
    return h0 * math.exp(-k * t)
```

### 🟪 Observed pattern

George consistently questioned what symbols represented biologically and whether the notation was scientifically meaningful. This was treated as a major strength in mathematical modelling.

## Grade log

| Category | Score |
|---|---:|
| Mathematical language | 91% |
| Function notation | 88% |
| Set notation | 84% |
| Scientific communication | 92% |
| Programming notation | 86% |
| Mathematical interpretation | 93% |

**Final session grade:** 90/100 (A−)  
**Lesson I.1 result:** Passed  
**Lesson status:** Locked

## Learning outcomes

At the end of Lesson I.1, George can:

- distinguish expressions, equations, identities, formulas, and definitions;
- translate biological statements into mathematical notation;
- critique incomplete or ambiguous notation;
- move between mathematics and Python/R notation;
- identify domain restrictions and basic set notation;
- evaluate whether a model is scientifically interpretable rather than merely algebraically legal.

## Lesson I.1 completion

- [x] Session I.1.1
- [x] Session I.1.2
- [x] Session I.1.3
- [x] Session I.1.4

## Next session

**Level I → Lesson I.2 → Session I.2.1**  
**Topic:** Numbers, number systems, and mathematical operations.
