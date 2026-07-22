# Part 3 — Correction, Review, Mistake Log, and Lock-In

## Final result

- Mandatory Core completed: **4/4**
- Mandatory completion: **100%**
- Session result: **PASS**
- Final session score: **9.0/10**
- Exact mean before rounding: **8.95/10**
- Recommended, Stretch, and Research/Application Integration exercises: deferred because the ending state was Energy 1/5 and Fatigue 4/5; no penalty applied

## Exercise results

### M1 — Property or Method

**Score: 8.5/10 — completed**

The submission correctly recognized `.name`, `.stem`, and `.parent` as properties; `.exists()` as a method call; `.is_dir` and `Path.cwd` as method objects when parentheses are absent; and `Path.cwd()` as a method call.

Corrections locked in:

- `file_path.resolve` is a method object, not a property. The result-producing expression is `file_path.resolve()`.
- `file_path.parent` returns the containing directory. For `C:/george/data/filename.extension`, the parent is `C:/george/data`.
- `Path.cwd` does not return a working directory until called as `Path.cwd()`.
- The requested table and two-sentence property/method rule were only partially represented in the response format.

### M2 — Relative-Path Debug Trace

**Score: 9.4/10 — completed**

The final submission contains the correct eight resolved attempted paths, eight correct existence decisions, and all four shortest valid relative paths.

Correct final shortest paths:

```text
A: data/test_sequence.fasta
B: ../data/test_sequence.fasta
C: test_sequence.fasta
D: ../data/test_sequence.fasta
```

Remaining correction in the archived submission:

- In A2, from `/home/george/ccp_path_lab`, `..` moves to `/home/george`, not to `/home/george/ccp_path_lab`.

Minor wording and transcription notes:

- A path references a file; it does not run or inspect the file by itself.
- The C heading should read `For test_sequence.fasta` for the first candidate.
- `..data/test_sequence.fasta` is a typing error for `../data/test_sequence.fasta`.
- The earlier C2 mismatch was treated as a placement/transcription mistake because the final resolution `/home/george/ccp_path_lab/data/data/test_sequence.fasta` and the reasoning were correct.

### M3 — Safe Path Inspector in George’s Pseudocode

**Score: 8.7/10 — completed and locked**

The pseudocode includes current-working-directory output, input collection, whitespace removal, empty-input handling, path storage, metadata output, existence checking, classification tags, specific messages, meaningful indentation, and George’s `$...$` comment notation.

Main structural correction:

- The missing-path branch assigns `#MISSING`, but the later separate classification `IF` can still execute and replace that status with `#OTHER`. The classification chain should execute only when the path exists, or the missing branch should immediately transfer control to the finish/retry point.

The use of retry control was accepted. It was not treated as a conceptual error merely because its placement differed from a conventional pseudocode style.

### M4 — Python Path Inspector Version 2

**Score: 9.2/10 — completed and locked**

The submitted program is syntactically valid and demonstrates working retry behaviour, clean exit behaviour, missing-path handling, existing-directory metadata, and existing-FASTA metadata without a traceback. The continuous interactive transcript was accepted as valid evidence of the loop and was not penalized.

Corrections locked in:

1. `Path(user_input)` is constructed before the empty-input check. Empty input should be rejected first.
2. The existing-path classification handles File and Directory but does not print Other filesystem object.
3. The final outer `else` cannot execute because `not file_path.exists()` and `file_path.exists()` already exhaust the Boolean possibilities.
4. The FASTA evidence used an absolute path although that specific test requested a valid relative path.

Strengths beyond the minimum template:

- repeated input is supported;
- missing input does not crash the process;
- `exit` terminates cleanly;
- no path is opened or modified;
- method-call parentheses are correct in the final file and directory checks.

## Mistake log

🟥 `file_path.resolve` classified as a property.  
🟨 The member name was confused with the value produced by calling it.  
🟦 `resolve` is a method.  
🟩 Use `file_path.resolve()`.  
🟪 Reinforcement: classify every `pathlib` member before predicting its result.

🟥 A parent path was described as though it still contained the filename.  
🟨 The complete path and its containing directory were mixed together.  
🟦 `.parent` removes the final path component.  
🟩 `Path("C:/george/data/file.fasta").parent` represents `C:/george/data`.  
🟪 Reinforcement: distinguish path, name, and parent as separate metadata fields.

🟥 In one movement description, `..` did not remove the final CWD component.  
🟨 The resolved destination was understood, but the intermediate movement line was copied incorrectly.  
🟦 `..` moves upward exactly one directory.  
🟩 `/home/george/ccp_path_lab/..` resolves to `/home/george`.  
🟪 Reinforcement: cross out one final component for every `..` before appending the remaining components.

🟥 The pseudocode missing status could be overwritten by the later classification block.  
🟨 Existence and type classification were written as independent decisions.  
🟦 A missing path must not enter the existing-object classification chain.  
🟩 Use `IF missing ... ELSE IF file ... ELIF directory ... ELSE other`.  
🟪 Reinforcement: make classifications mutually exclusive.

🟥 `Path(user_input)` was constructed before empty-input rejection.  
🟨 The validation check existed, but it was placed after construction.  
🟦 `Path("")` represents the current directory, which can make `.exists()` return `True`.  
🟩 Validate the stripped string first, then construct one `Path` object.  
🟪 Reinforcement: validate raw input before interpreting it.

🟥 Other filesystem object had no reachable Python classification branch.  
🟨 The intended outer `else` was placed after an exhaustive existence test.  
🟦 `exists()` separates Missing from Existing; `is_file()` and `is_dir()` then separate existing types.  
🟩 Use one chain: missing → file → directory → other.  
🟪 Reinforcement: test control-flow reachability, not merely indentation.

## Strength log

- Completed all four mandatory exercises across approximately twelve hours of work over two days.
- Challenged unclear grading and forced the rubric to be applied to the actual requirements.
- Distinguished reasoning mistakes from transcription or placement mistakes.
- Corrected the full relative-path trace to eight correct resolutions and existence decisions.
- Produced a functioning retrying path-inspector program rather than merely filling the supplied template.
- Preserved George’s established pseudocode notation and classification tags.
- Demonstrated direct relevance to FASTA intake and the genomic indexer project.

## Command gap log

```python
from pathlib import Path

Path.cwd()
Path(user_input)
file_path.resolve()
file_path.name
file_path.stem
file_path.suffix
file_path.parent
file_path.exists()
file_path.is_file()
file_path.is_dir()
```

Properties:

```text
.name
.stem
.suffix
.parent
```

Methods and method calls:

```text
.cwd()     versus Path.cwd
.resolve() versus file_path.resolve
.exists()
.is_file()
.is_dir()
```

Relative-path components:

```text
.   = remain in the current directory
..  = move to one parent directory
name = enter or reference the named child component
```

## Correct classification architecture

```text
empty input
→ reject and retry

non-empty input
→ construct Path
→ print metadata
→ does not exist: Missing
→ exists and is_file(): File
→ exists and is_dir(): Directory
→ otherwise: Other filesystem object
```

## Research connection

```text
path supplied by user
→ strip whitespace
→ reject empty input
→ construct Path safely
→ check existence
→ require regular file
→ validate .fa/.fasta suffix
→ read FASTA in a later stage
→ remove header and wrapping
→ reconstruct sequence
→ send sequence to CLEAVE(sequence)
```

## Grade log

```text
M1  8.5/10
M2  9.4/10
M3  8.7/10
M4  9.2/10
------------
Mean 8.95/10
Recorded final score: 9.0/10
Result: PASS
```

## Archive status

```text
CCP
└── Level I
    └── Lesson I.2
        └── Session I.2.2
            Status: completed and locked
            Mandatory Core: 4/4
            Final score: 9.0/10
            Next target: Session I.2.3
```
