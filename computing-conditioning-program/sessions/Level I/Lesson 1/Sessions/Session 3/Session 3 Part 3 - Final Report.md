# CCP — Level I, Lesson 1, Session 3
## Part 3 — Mandatory-Core Correction Report

## Session state

- Energy at start: 5/5
- Fatigue at start: 1/5
- Mid-session adjustment: Mandatory-Core Only Adaptation
- Reason: user reported reduced Energy/Fatigue and completed only M1-M4
- Optional exercises R1-A2: frozen, not failed

## Session decision

**PASS — Mandatory Core completed.**

## Submitted files

1. `CCP_L1_L1_S3_Part2_Mandatory_Submission.txt`
2. `exercise_ccp_l1_les1_s3_code.py`

## Mandatory Core Grades

### M1 — Validation-Before-Division Refactor

**Grade: 78%**

Mostly successful, but still structurally unstable.

What improved:

- `sequence_length` is calculated before GC percentage.
- Division happens inside the `else` branch after `sequence_length` validation.
- `sequence[0]` is not used.

Remaining issue:

- the later GC% validation block is outside the `else` branch.
- if sequence is empty, `gc_percent` is never created, but the next `if` statement still tries to use it.
- this causes a `NameError`, not a `ZeroDivisionError`.

Correct rule:

```text
All calculations and all checks that depend on gc_percent must stay inside the valid branch.
```

### M2 — Direct GC Count and Clean Numeric Types

**Grade: 76%**

Direct GC count achieved; formatting still incomplete.

What improved:

```python
gc_count = sequence.count("G") + sequence.count("C")
```

Remaining issue:

- `gc_percent` is not rounded to two decimal places.
- expected format was `46.15%`, not `46.15384615384615%`.

### M3 — Output Synchronization Check

**Grade: 70%**

Good idea, but not fully synchronized.

What improved:

- the full sequence is now shown.
- GC count is shown as 12.
- the print/output mapping format is present.

Remaining issue:

- code prints `DNA Sample Report` but the table says `DNA Sample Report:`.
- sequence length lacks `bp`.
- GC percentage is unrounded.
- table includes internal logic lines, not only final report-output lines.

### M4 — WSL Git Folder Diagnosis

**Grade: 95%**

Strong pass.

What worked:

- WSL terminal was used.
- `pwd` was run.
- CCP folder was reached through `/mnt/c`.
- `ls -lah` was run.
- `git --version` worked: `git version 2.43.0`.
- `git status` produced a meaningful diagnosis: not a Git repository.

## Mandatory Core Summary

| Exercise | Grade |
|---|---:|
| M1 | 78% |
| M2 | 76% |
| M3 | 70% |
| M4 | 95% |

- Mandatory Completion: 100%
- Mandatory Mastery: 79.75%
- Session Mandatory Result: PASS

## Global Scores — Adapted Session

- Completion: 100% of adapted required workload
- Mandatory Mastery: 79.75%
- Coverage: 31% of full 13-exercise session, intentionally adapted
- Command Fluency: 78%
- Debugging Maturity: 72%
- Research Readiness: 66%
- Python Track Maturity: 71%
- WSL Ubuntu Track Maturity: 65%
- Git/GitHub Track Maturity: 42%
- Documentation Track Maturity: unchanged
- Pseudocode Track Maturity: unchanged

## Mistake Log

🟥 Mistake — The GC validation block is outside the valid `sequence_length` branch.  
🟨 Cause — The first validation was fixed, but the dependent code block was not fully indented under the `else` branch.  
🟦 Correct Rule — Any variable created inside an `else` branch is safe only inside that branch unless guaranteed elsewhere.  
🟩 Corrected Example — Keep `gc_count`, `gc_percent`, GC validation, and report printing all inside the `else` branch.  
🟪 Recurring Pattern — Logic order improved, but block scope/indentation still needs training.

🟥 Mistake — GC percentage was not rounded to two decimals.  
🟨 Cause — The raw floating-point value was printed directly.  
🟦 Correct Rule — Use formatting for report-ready numerical output.  
🟩 Corrected Example — `print(f"GC percentage: {gc_percent:.2f}%")`  
🟪 Recurring Pattern — Scientific output formatting needs separate attention from calculation.

🟥 Mistake — Output synchronization table does not exactly match the script.  
🟨 Cause — The explanatory table mixed logic explanation with expected report lines.  
🟦 Correct Rule — A synchronization check compares final print statements to final output, line by line.  
🟩 Corrected Example — `print("DNA Sample Report") -> DNA Sample Report`  
🟪 Recurring Pattern — Code/report/README synchronization needs continued drilling.

🟥 Mistake — Sequence length output lacks `bp`.  
🟨 Cause — The numerical value was printed without biological unit.  
🟦 Correct Rule — Reports should include units when the value represents a biological measurement.  
🟩 Corrected Example — `Sequence Length: 26 bp`  
🟪 Recurring Pattern — Report formatting must preserve scientific meaning.

## Command Gap Log

No serious command gap in M4.

Strong evidence:

- WSL path navigation succeeded.
- Git version was checked successfully.
- Git status generated a valid diagnostic.

Remaining Git/Archive gap:

```bash
git init
git status
git add .
git commit -m "Add CCP Session 3 mandatory exercises"
```

## Prerequisite Gap Log

1. Python block scope / indentation dependency  
Type: Syntax + Debugging Gap  
Need: practice keeping all dependent code inside the proper `if/else` branch.

2. Output formatting with f-strings  
Type: Syntax Gap  
Need: drill `{:.2f}` formatting for scientific reports.

3. Git repository initialization  
Type: Git/Archive Gap  
Need: learn `git init` in the correct local folder.

## Next Session Preview

Level I — Lesson 1 — Session 4  
Review + Mini-Assessment + Correction + Git Archive

Likely targets:

1. Fix indentation/block scope permanently.
2. Run corrected script with normal sequence and empty sequence.
3. Produce exact expected output.
4. Initialize Git repository in WSL or diagnose repository placement.
5. Create a minimal local archive structure.
6. Upload/update Session 3 archive on GitHub.
