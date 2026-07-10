# CCP Level I — Lesson 1 — Session 1 Exercises

## Mode

Mode C — High Energy / Low Fatigue

## Target

Build a minimal, meaningful biological sample report script that is clean enough to become the first GitHub-uploadable CCP artifact.

## Mandatory Core

### M1 — Pseudocode
Write pseudocode for a biological sample report program. It must store sample ID, organism name, sequence length, GC percentage, print a readable report, and include one validation idea.

### M2 — Python Variables
Create a Python script skeleton named `sample_report.py` using:

```python
sample_id
organism
sequence_length
gc_percent
data_source
```

### M3 — Computed Field
Add:

```python
gc_count_estimate = sequence_length * gc_percent / 100
```

Print it with a clear label.

### M4 — CLI + Git Archive
Write command sequence to enter the script folder, run the script, check Git status, stage the script, and commit it.

## Recommended

### R1 — Classification
Classify each line as DATA, PROCESSING, OUTPUT, or ARCHIVE.

### R2 — Error Interpretation
Explain why `print(sampleID)` fails if only `sample_id` was defined.

### R3 — Output Formatting
Improve report output with title, separator, labeled fields, units, and percentage symbol.

### R4 — README
Write a short GitHub-ready README description.

## Stretch

### S1 — Validation Logic
Add pseudocode validation for `sequence_length <= 0`.

### S2 — Python Conditional
Express S1 in Python using `if / else`.

### S3 — Project Architecture
Design a folder tree with `scripts/`, `results/`, `notes/`, and `README.md`.

## Research / Application

### A1 — Biological Interpretation
Explain what GC% can and cannot tell us from this script alone.

### A2 — Future Pipeline Thinking
Describe how this single-sample script could become a CSV-processing pipeline for many samples.
