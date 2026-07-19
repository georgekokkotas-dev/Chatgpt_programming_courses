# CCP — Level I, Lesson 1, Session 2

## Final Corrected Part 3 Archive

This archive records the final corrected Part 3 grading and logs for Session 2.

## Session decision

**PASS.**

George completed the Mandatory Core, corrected the requested filename target, improved the script variable representation, attempted README documentation, attempted project structure, identified the WSL/Windows Git split, and clarified the BASIC-style pseudocode approach.

## Important scoring correction

The earlier label **Biological / Data Interpretation: 55%** was wrong because it implied an assessment of George's domain competence.

Correct distinction:

- Biology / Genetics domain knowledge: **advanced / not assessed here**
- Bio-computational reporting discipline for this specific GC% mini-report: **70%**
- A1 answer quality: **72%**
- Research readiness overall: **65%**

## Mandatory Core

| Exercise | Score |
|---|---:|
| M1 — File / Path Discipline | 95% |
| M2 — Variables and Data Types | 84% |
| M3 — Validation Logic | 62% |
| M4 — Clean Report Output | 72% |

**Mandatory completion:** 100%  
**Mandatory mastery:** 78%

## Final global scores

| Metric | Score |
|---|---:|
| Mandatory Completion | 100% |
| Overall Attempt Coverage | 85% |
| Mandatory Mastery | 78% |
| Overall Mastery | 70% |
| Coverage | 85% |
| Command Fluency | 72% |
| Debugging Maturity | 69% |
| Research Readiness | 65% |

## Main unresolved technical issue

Validation must happen before division:

```text
sequence → sequence_length → validate → gc_count → gc_percent → report
```

## Git status

- Git works in WSL Ubuntu.
- Git does not work in native Windows CMD.
- Git training should continue through WSL until Windows Git/PATH is fixed.

## Next session preview

Level I — Lesson 1 — Session 3:

1. Fix validation-before-division permanently.
2. Force expected output to match code.
3. Use WSL Git for one real Git action.
4. Split BASIC-like pseudocode into small subroutines.
5. Write a clean `README.md` skeleton.
6. Preview writing report output into `results/sample_report_output.txt`.
