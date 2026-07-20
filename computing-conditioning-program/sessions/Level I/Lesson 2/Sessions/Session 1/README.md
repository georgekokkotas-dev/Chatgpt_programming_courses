# CCP — Level I, Lesson 2, Session 1

## Status

- Mode: B+ — Normal Conditioning
- Mandatory Core: 4/4 completed
- Recommended: not attempted
- Stretch: not attempted
- Research/Application Integration: not attempted
- Session result: PASS
- Final session score: **9.2/10**

## Session focus

Files, folders, paths, working directories, cross-platform path logic, `pathlib`, BASIC-style pseudocode, and a Python path inspector.

## Mandatory Core

1. Path classification table
2. Working-directory trace
3. Path inspector in George's established pseudocode notation
4. Python `pathlib` path inspector

## Files

- `mandatory-core-submission.md` — archived answers and session evidence
- `inspect_path.py` — submitted Python implementation preserved as written
- `inspect_path_corrected.py` — corrected reference version with method calls fixed
- `part-3-correction-report.md` — final correction, reflection, logs, and result

## Main learning results

- Absolute and relative paths are classified by syntax and environment.
- `/mnt/c/...` is an absolute WSL/Linux path pointing into the Windows C drive.
- Relative paths are resolved from the current working directory.
- A file may exist while a particular relative path used to reach it is wrong.
- `pathlib` properties such as `.name`, `.stem`, `.suffix`, and `.parent` differ from methods such as `.exists()`, `.is_file()`, `.is_dir()`, and `.resolve()`.
- `pass` is Python's no-operation statement.

## Research connection

The path inspector provides the future input-validation layer for the genomic indexer and FASTA-processing workflow before sequence reading and `CLEAVE(sequence)`.
