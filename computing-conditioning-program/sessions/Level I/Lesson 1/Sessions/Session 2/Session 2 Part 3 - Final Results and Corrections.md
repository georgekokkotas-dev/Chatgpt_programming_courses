# CCP — Level I, Lesson 1, Session 2

## Part 3 — Final Corrected Results

**Session decision:** PASS

**State**

- Energy: 4/5
- Fatigue: 2/5
- Mode: B+ / Controlled C
- Primary track: Python
- Support tracks: Windows CMD, WSL Ubuntu, Git/GitHub, Pseudocode, Documentation

## Important scoring correction

The previous label **Biological / Data Interpretation: 55%** was badly worded.

Correct distinction:

- Biology / Genetics domain knowledge: **advanced / not assessed here**
- Bio-computational reporting discipline for this specific GC% mini-report: **70%**
- A1 answer quality for this specific exercise: **72%**
- Research readiness overall: **65%**

Reason: George's professional biology/genetics competence is not being graded by a beginner Python exercise. The only issue in A1 was claim-control from a single GC% value, plus the known purine/pyrimidine memory mix-up.

## Mandatory Core Result

| Exercise | Score |
|---|---:|
| M1 — File / Path Discipline | 95% |
| M2 — Variables and Data Types | 84% |
| M3 — Validation Logic | 62% |
| M4 — Clean Report Output | 72% |

**Mandatory Completion:** 100%  
**Mandatory Mastery:** 78%

## Recommended / Stretch / Application Result

| Exercise | Score |
|---|---:|
| R1 — Debugging / Name Discipline | 85% |
| R2 — Error Interpretation | 90% |
| R3 — Git Installation Check | 100% |
| R4 — README Skeleton | 70% |
| S1 — Character Validation | 74% |
| S2 — Output Saving Plan | 0% |
| S3 — Project Folder Tree | 62% |
| A1 — GC% Biological Interpretation | 72% |
| A2 — GitHub Portfolio Decision | 88% |

## Global Scores

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

## Track Maturity Update

| Track | Score |
|---|---:|
| Python | 68% |
| Pseudocode | 64% |
| Windows CMD / CLI | 61% |
| WSL Ubuntu | 55% |
| Git / GitHub | 36% |
| Documentation / README | 27% |
| Bio-computational reporting discipline | 70% |
| Biology / Genetics domain knowledge | Advanced / not assessed here |
| Project Architecture | 37% |

## Main remaining technical corrections

1. **Validation must happen before division.**

   Current problem: `gc_percent` is calculated before checking whether `sequence_length <= 0`.

   Correct order:

   ```text
   sequence → sequence_length → validate → gc_count → gc_percent → report
   ```

2. **Expected output must match corrected code.**

   Since the code prints:

   ```python
   print(f"Sequence: {sequence}")
   ```

   the expected output should show:

   ```text
   Sequence: ATGGCCCCGTAAATGTCGTATAGTGA
   ```

   not:

   ```text
   Sequence: A
   ```

3. **GC count should be direct.**

   Preferred:

   ```python
   gc_count = sequence.count("G") + sequence.count("C")
   gc_percent = gc_count / sequence_length * 100
   ```

## Mistake Log

🟥 **Mistake:** Validation is placed after a risky division.  
🟨 **Cause:** The derived calculation was written before the safety check.  
🟦 **Correct Rule:** Validate before risky operations, especially division by a variable.  
🟩 **Corrected Example:** Check `sequence_length <= 0` before calculating `gc_percent`.  
🟪 **Recurring Pattern:** Logic ordering needs drilling: input → validate → compute → report.

🟥 **Mistake:** Expected output still shows `Sequence: A`.  
🟨 **Cause:** The output example was not updated after correcting the code from `sequence[0]` to `sequence`.  
🟦 **Correct Rule:** Expected output must match the current version of the code.  
🟩 **Corrected Example:** `Sequence: ATGGCCCCGTAAATGTCGTATAGTGA`  
🟪 **Recurring Pattern:** Code and report-output synchronization needs practice.

🟥 **Mistake:** Reconstructed GC count from percentage instead of direct count.  
🟨 **Cause:** Algebraic reconstruction worked numerically, so it felt acceptable.  
🟦 **Correct Rule:** Prefer direct primary computation when the data are available.  
🟩 **Corrected Example:** `gc_count = sequence.count("G") + sequence.count("C")`  
🟪 **Recurring Pattern:** Mathematically valid does not always mean computationally clean.

🟥 **Mistake:** GC interpretation overclaim in this specific mini-report.  
🟨 **Cause:** Physical stability, mutation behavior, and biological meaning were compressed into one explanation.  
🟦 **Correct Rule:** GC% is descriptive; interpretation requires genomic and biological context.  
🟩 **Corrected Example:** High GC% can suggest higher melting temperature, but not biological function by itself.  
🟪 **Recurring Pattern:** Strong biological intuition needs controlled report wording.

🟥 **Mistake:** Purine/pyrimidine mix-up.  
🟨 **Cause:** Recurring memorization vulnerability in nucleotide classification.  
🟦 **Correct Rule:** Purines: A/G. Pyrimidines: C/T. GC base pair has 3 hydrogen bonds.  
🟩 **Corrected Example:** G is purine; C is pyrimidine; together they form a GC pair.  
🟪 **Recurring Pattern:** Needs flashcard-style correction, not a biology-competence penalty.

🟥 **Mistake:** S1 pseudocode function had too many responsibilities.  
🟨 **Cause:** Pipeline paranoia expanded the active task.  
🟦 **Correct Rule:** One subroutine/function should do one main job.  
🟩 **Corrected Example:** Separate `CHECK_INPUT_TYPE`, `READ_SEQUENCE`, `CHECK_DNA_BASES`, `PRINT_REPORT`.  
🟪 **Recurring Pattern:** Good systems thinking; needs modular discipline.

## Command Gap Log

- Windows CMD cannot run `git`.
- WSL Ubuntu can run `git`.
- Correct diagnosis: Git is installed in WSL, not available to native Windows CMD.
- Git training should proceed through WSL for now.
- Windows CMD Git remains a separate setup/PATH issue.

## Next Session Preview

**Level I — Lesson 1 — Session 3**  
Mixed Programming + CLI + Application / Research Link

Main targets:

1. Fix validation-before-division permanently.
2. Force expected output to match code.
3. Use WSL Git for one real Git action.
4. Split BASIC-like pseudocode into small subroutines.
5. Write a clean `README.md` skeleton.
6. Preview writing report output into `results/sample_report_output.txt`.
