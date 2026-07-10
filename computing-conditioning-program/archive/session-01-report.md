# CCP Session Archive — Level I, Lesson 1, Session 1

## Session

- Course: Computing Conditioning Program
- Level: I — Digital and Algorithmic Foundations
- Lesson: 1 — What is a Computer Program?
- Session: 1 — Program, Algorithm, Pseudocode, First Command

## Outcome

Session passed.

George created and executed a meaningful biological Python script from Windows CMD. The script calculated sequence length, GC%, and estimated GC count, then printed a structured sample report.

## Key Learning Events

- First practical Python execution from CMD.
- Real command-line issue discovered: filenames with spaces require quotes.
- Git command failed because Git was unavailable in CMD.
- Git issue classified as Command Gap / Toolchain Gap, not programming failure.

## Mistake Log

### 1. DNA sequence representation

- Mistake: Treating DNA sequence as “not a string.”
- Cause: Biological concept and programming representation got mixed.
- Correct Rule: In Python, DNA is usually represented as a string.
- Fixed Example: `seq = "ATGGCCCCGTAAATGTCGTATAGTGA"`
- Pattern: Good biological intuition; computational representation needs formalization.

### 2. Variable-name discipline

- Mistake: Using different variable names from the task.
- Cause: Concept understood, but specification was not followed exactly.
- Correct Rule: Exact variable names can matter.
- Fixed Example: `sequence_length` instead of `seq_count`; `gc_percent` instead of `gc_100`.
- Pattern: Specification obedience needs training.

### 3. Git command failure

- Mistake: `git status` failed.
- Cause: Git is not installed or not in PATH.
- Correct Rule: A command must be installed and visible to the terminal before it can run.
- Fixed Example: install Git, reopen CMD, then run `git --version`.
- Pattern: Toolchain setup gap, not programming failure.

## Grade

- Mandatory Completion: 100%
- Mandatory Mastery: 77.5%
- Session Result: PASS

## Next Session

Level I — Lesson 1 — Session 2

Focus:

- Cleaner file naming
- Cleaner variable names
- Sequence length validation
- Allowed-character validation
- Output formatting
- README drafting
- Git setup check
