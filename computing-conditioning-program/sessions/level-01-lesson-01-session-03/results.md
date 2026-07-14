# CCP Level I — Lesson 1 — Session 3 Results

## Session state

- Start Energy: 5/5
- Start Fatigue: 1/5
- Mid-session adjustment: Mandatory-Core Only Adaptation
- Reason: Energy/Fatigue changed during execution
- Optional exercises: frozen, not failed

## Session decision

**PASS — Mandatory Core completed.**

## Submitted files

- `CCP_L1_L1_S3_Part2_Mandatory_Submission.txt`
- `exercise_ccp_l1_les1_s3_code.py`

## Mandatory grades

| Exercise | Grade | Result |
|---|---:|---|
| M1 — Validation-before-division | 78% | Mostly fixed; block structure still unstable |
| M2 — Direct GC count | 76% | Direct count achieved; formatting incomplete |
| M3 — Output synchronization | 70% | Good idea; not fully synchronized |
| M4 — WSL Git diagnosis | 95% | Strong pass |

## Summary scores

- Mandatory Completion: 100%
- Mandatory Mastery: 79.75%
- Adapted Session Result: PASS
- Command Fluency: 78%
- Debugging Maturity: 72%
- Research Readiness: 66%
- Python Track Maturity: 71%
- WSL Ubuntu Track Maturity: 65%
- Git/GitHub Track Maturity: 42%

## Main correction

The first validation-before-division issue improved, but the `gc_percent` validation block remained outside the `else` branch. If `sequence = ""`, then `gc_percent` is never created, and Python raises a `NameError` when the later `if gc_percent <= 0...` line runs.

Correct rule:

```text
All calculations and all checks that depend on gc_percent must stay inside the valid sequence_length branch.
```

## Corrected Python structure

```python
import math

sample_id = "#12345"
organism = "H. sapiens"
sequence = "ATGGCCCCGTAAATGTCGTATAGTGA"
data_source = "www.genericdatabasesite.site"

sequence_length = len(sequence)

if sequence_length <= 0:
    print("Sequence has an invalid value.")
else:
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percent = gc_count / sequence_length * 100

    if gc_percent <= 0 or gc_percent > 100 or math.isnan(gc_percent):
        print("GC% has an invalid value.")
    else:
        print("DNA Sample Report")
        print("-----------------")
        print(f"Sample ID: {sample_id}")
        print(f"Organism: {organism}")
        print(f"Sequence: {sequence}")
        print(f"Sequence Length: {sequence_length} bp")
        print(f"GC percentage: {gc_percent:.2f}%")
        print(f"GC Count: {gc_count}")
        print(f"The data were obtained through public datasets: {data_source}")
```

## Git result

WSL Git works:

```text
git version 2.43.0
```

The local CCP Lessons folder is not yet a Git repository:

```text
fatal: not a git repository
```

## Next session

Level I — Lesson 1 — Session 4: Review + Mini-Assessment + Correction + Git Archive.
