# CCP — Level I → Lesson I.2 → Session I.2.3
## Part 1 — Mixed Programming, CLI Verification, and Research Path Intake

**Energy:** 5/5  
**Fatigue:** 2/5  
**Session mode:** **Mode B — Normal Conditioning, upper-band independence**

## Session identity

**Lesson:** Files, Folders, Paths, and Working Directories  
**Session function:** S3 — Mixed Programming + CLI + Application/Research Link  
**Theme:** **Strict FASTA intake gates, path normalization, CLI verification, and file-manifest records**

### Primary objective

Transform the previous general path inspector into a stricter research-computing component that can decide whether a supplied path is suitable for later FASTA processing—without opening or reading the file.

```text
raw input
→ clean input
→ reject empty input
→ construct Path
→ determine attempted location
→ test existence
→ require regular file
→ validate FASTA suffix
→ generate reproducible metadata
→ permit later sequence reading
```

## Active blocks

- Files, Paths and Directories
- Python Programming
- Command-Line Thinking
- Ubuntu CLI / WSL
- Debugging and Error Interpretation
- Algorithms and Algorithmic Complexity
- Databases and Structured Data
- Bioinformatics Computing
- Research Pipelines
- Reproducible Computing
- Git Basics

## Active tracks

| Layer | Track |
|---|---|
| Universal logic | Algorithm and pseudocode |
| Primary language | Python |
| Secondary environment | WSL Ubuntu |
| Operational layer | GNU/Linux CLI and Git |
| Side-subject: algorithms | Guard-clause validation and short-circuit decision trees |
| Side-subject: databases | File-manifest records and SQLite database paths |

## Prerequisites carried forward

George has already demonstrated:

- relative-path resolution from a known CWD;
- `Path.cwd()`, `.resolve()`, `.exists()`, `.is_file()`, and `.is_dir()`;
- `.name`, `.stem`, `.suffix`, and `.parent`;
- retry loops and clean `exit` handling;
- Python file/directory classification;
- pseudocode classification tags;
- CLI awareness across Windows and WSL.

The previous session score was **9.0/10**, with all four Mandatory Core exercises completed.

---

# 1. Concept theory

## 1.1 One input, four different representations

Suppose the user types:

```text
../data/test_sequence.fasta
```

That input exists at four conceptual levels.

### Raw input

```text
"../data/test_sequence.fasta"
```

This is merely text.

### Path object

```python
Path("../data/test_sequence.fasta")
```

This is a structured path representation. It still contains relative movement.

### Resolved path

From:

```text
/home/george/ccp_path_lab/scripts
```

it resolves to:

```text
/home/george/ccp_path_lab/data/test_sequence.fasta
```

### Filesystem state

The operating system then determines whether that resolved location:

- exists;
- is a regular file;
- is a directory;
- is another filesystem object;
- is inaccessible or missing.

`Path.exists()` checks whether a path points to an existing filesystem object, while `Path.is_file()` specifically checks whether it points to a regular file. `Path.resolve()` produces an absolute resolved path and removes components such as `..`; it must not be confused with an existence test.

## 1.2 Correct validation order

The order matters:

```text
1. Obtain input
2. Strip whitespace
3. Reject empty input
4. Construct Path
5. Test existence
6. Test whether it is a regular file
7. Test suffix
8. Produce accepted metadata
```

The invalid order is:

```text
Input
→ construct Path immediately
→ check empty input afterward
```

That order permits an empty string to become a path object representing the current-directory context before the program rejects it.

## 1.3 Classification versus suitability

A path can be valid as a filesystem path but unsuitable as FASTA input.

| Path state | Filesystem classification | FASTA suitability |
|---|---|---|
| Existing `.fasta` regular file | File | Accepted |
| Existing `.txt` regular file | File | Rejected suffix |
| Existing directory named `data.fasta` | Directory | Rejected type |
| Missing `sample.fasta` | Missing | Rejected existence |
| Empty input | No path accepted | Rejected input |

Therefore:

```text
File classification ≠ research-input approval
```

A strict FASTA gate requires both:

```text
existing regular file
AND
suffix is .fa or .fasta
```

---

# 2. Algorithm side-subject

## Guard-clause validation

A **guard clause** rejects an invalid state before the main processing stage.

```text
IF empty:
    reject

ELSE IF missing:
    reject

ELSE IF not a regular file:
    reject

ELSE IF wrong suffix:
    reject

ELSE:
    accept
```

This is a short-circuit decision tree. Once a decisive failure is found, later tests are unnecessary.

### Why order the tests this way?

Calling:

```python
file_path.suffix
```

does not require that the file exist, but suffix validation alone proves nothing.

For example:

```text
missing_file.fasta
```

has the correct suffix but does not exist.

Likewise:

```text
results.fasta/
```

could be a directory despite its name.

The sequence should therefore proceed from fundamental validity toward domain-specific validity:

```text
input validity
→ filesystem validity
→ object-type validity
→ biological-format plausibility
```

## Complexity note

Let `k` be the number of path components.

The program’s textual path processing is approximately proportional to `k`:

```text
O(k)
```

The filesystem checks also require operating-system lookups. Their real time depends on the filesystem, cache state, mounted drives, permissions, and network or WSL boundaries. Therefore, filesystem access should not be treated as a pure constant-time mathematical operation even though individual calls often appear instantaneous.

---

# 3. Pseudocode model

```text
START
CLS

PRINT CURRENT_WORKING_DIRECTORY

PRINT "ENTER FASTA PATH: "
INPUT RAW_PATH

TRIM RAW_PATH

IF RAW_PATH = EMPTY
    PRINT "ERROR: EMPTY INPUT"
    GO TO FINISH
END IF

SET FILE_PATH = PATH(RAW_PATH)

PRINT "ENTERED PATH: ", FILE_PATH
PRINT "ATTEMPTED ABSOLUTE PATH: ", RESOLVE(FILE_PATH)

IF FILE_PATH DOES NOT EXIST
    SET STATUS = #MISSING
    PRINT "ERROR: PATH DOES NOT EXIST"
    GO TO FINISH
END IF

IF FILE_PATH IS NOT A REGULAR FILE
    IF FILE_PATH IS DIRECTORY
        SET STATUS = #DIRECTORY
        PRINT "ERROR: FASTA INPUT MUST BE A FILE"
    ELSE
        SET STATUS = #OTHER
        PRINT "ERROR: UNSUPPORTED FILESYSTEM OBJECT"
    END IF

    GO TO FINISH
END IF

SET NORMALIZED_SUFFIX = LOWERCASE(SUFFIX(FILE_PATH))

IF NORMALIZED_SUFFIX IS NOT ".fa"
AND NORMALIZED_SUFFIX IS NOT ".fasta"
    SET STATUS = #WRONG_SUFFIX
    PRINT "ERROR: EXPECTED .fa OR .fasta"
    GO TO FINISH
END IF

SET STATUS = #ACCEPTED

PRINT "FASTA PATH ACCEPTED"
PRINT NAME(FILE_PATH)
PRINT STEM(FILE_PATH)
PRINT SUFFIX(FILE_PATH)
PRINT PARENT(FILE_PATH)
PRINT RESOLVE(FILE_PATH)

FINISH:
PRINT "STATUS: ", STATUS
END
```

The missing-path branch cannot fall through into File/Directory/Other classification. Every rejection transfers control to `FINISH`.

---

# 4. Python syntax and command table

| Operation | Python |
|---|---|
| Current working directory | `Path.cwd()` |
| Remove surrounding whitespace | `text.strip()` |
| Construct path | `Path(text)` |
| Resolve absolute path | `path.resolve()` |
| Check existence | `path.exists()` |
| Check regular file | `path.is_file()` |
| Check directory | `path.is_dir()` |
| Obtain final name | `path.name` |
| Obtain stem | `path.stem` |
| Obtain suffix | `path.suffix` |
| Normalize suffix case | `path.suffix.lower()` |
| Obtain parent | `path.parent` |
| Membership test | `value in {".fa", ".fasta"}` |
| Negated membership | `value not in {".fa", ".fasta"}` |

---

# 5. Worked demonstration

Assume:

```text
/home/george/ccp_path_lab/
├── data/
│   └── BRCA2_reference.FASTA
├── results/
└── scripts/
    └── fasta_gate.py
```

Current working directory:

```text
/home/george/ccp_path_lab/scripts
```

Input:

```text
../data/BRCA2_reference.FASTA
```

### Path movement

```text
..                      → move from scripts to ccp_path_lab
data                    → enter the data directory
BRCA2_reference.FASTA   → reference the candidate file
```

Resolved path:

```text
/home/george/ccp_path_lab/data/BRCA2_reference.FASTA
```

Validation:

```text
Input empty?          No
Exists?              Yes
Regular file?        Yes
Suffix lowercased?   .fasta
Allowed suffix?      Yes
Final status:        ACCEPTED
```

Possible output:

```text
Current working directory: /home/george/ccp_path_lab/scripts
Entered path: ../data/BRCA2_reference.FASTA
Resolved path: /home/george/ccp_path_lab/data/BRCA2_reference.FASTA
Name: BRCA2_reference.FASTA
Stem: BRCA2_reference
Suffix: .FASTA
Classification: File
FASTA gate: Accepted
```

The original suffix remains `.FASTA`, while:

```python
file_path.suffix.lower()
```

produces `.fasta` for the comparison.

---

# 6. Primary Python implementation

This implementation validates and reports the path but deliberately does **not** open or read the FASTA.

```python
from pathlib import Path

print("=" * 50)
print("FASTA Intake Gate")
print("Current working directory:", Path.cwd())
print("=" * 50)

user_input = input("Enter a FASTA path: ").strip()

if user_input == "":
    print("Status: REJECTED_EMPTY_INPUT")

else:
    file_path = Path(user_input)

    print("Entered path:", file_path)
    print("Resolved attempted path:", file_path.resolve())

    if not file_path.exists():
        print("Status: REJECTED_MISSING")

    elif not file_path.is_file():
        if file_path.is_dir():
            print("Classification: Directory")
            print("Status: REJECTED_DIRECTORY")
        else:
            print("Classification: Other filesystem object")
            print("Status: REJECTED_OTHER_OBJECT")

    elif file_path.suffix.lower() not in {".fa", ".fasta"}:
        print("Classification: File")
        print("Name:", file_path.name)
        print("Suffix:", file_path.suffix)
        print("Status: REJECTED_SUFFIX")

    else:
        print("Classification: File")
        print("Name:", file_path.name)
        print("Stem:", file_path.stem)
        print("Suffix:", file_path.suffix)
        print("Parent:", file_path.parent)
        print("Resolved path:", file_path.resolve())
        print("Status: ACCEPTED_FASTA")

print("=" * 50)
```

### Structural properties

- Empty input is rejected before `Path(user_input)`.
- Exactly one classification/status path executes.
- Missing input cannot later become Other.
- A directory with a `.fasta` name is still rejected.
- Case-insensitive FASTA suffixes are accepted.
- No `open()`, `.read()`, or file-writing operation appears.

---

# 7. WSL Ubuntu operational comparison

For the demonstration path:

```bash
pwd
realpath ../data/BRCA2_reference.FASTA
test -e ../data/BRCA2_reference.FASTA && echo "EXISTS"
test -f ../data/BRCA2_reference.FASTA && echo "REGULAR FILE"
basename ../data/BRCA2_reference.FASTA
dirname ../data/BRCA2_reference.FASTA
```

| Command | Purpose |
|---|---|
| `pwd` | Print the current working directory |
| `realpath PATH` | Print a canonical absolute path |
| `test -e PATH` | Test whether the path exists |
| `test -f PATH` | Test whether it is a regular file |
| `basename PATH` | Extract the final path component |
| `dirname PATH` | Remove the final path component |

```text
Python Path.cwd()        ↔ pwd
Python path.resolve()    ↔ realpath
Python path.exists()     ↔ test -e
Python path.is_file()    ↔ test -f
Python path.name         ↔ basename
Python path.parent       ↔ dirname
```

---

# 8. Database side-subject

## File-manifest records

A research pipeline should not record only:

```text
test_sequence.fasta
```

That name is ambiguous without its working-directory context.

A reproducible file record should preserve:

```text
original_input
source_cwd
resolved_path
file_name
suffix
classification
validation_status
```

Example conceptual record:

```text
original_input: ../data/BRCA2_reference.FASTA
source_cwd: /home/george/ccp_path_lab/scripts
resolved_path: /home/george/ccp_path_lab/data/BRCA2_reference.FASTA
file_name: BRCA2_reference.FASTA
suffix: .FASTA
classification: File
validation_status: ACCEPTED_FASTA
```

Possible future SQLite table:

```sql
CREATE TABLE file_manifest (
    file_id INTEGER PRIMARY KEY,
    original_input TEXT NOT NULL,
    source_cwd TEXT NOT NULL,
    resolved_path TEXT,
    file_name TEXT,
    suffix TEXT,
    classification TEXT NOT NULL,
    validation_status TEXT NOT NULL
);
```

Two path values are retained deliberately:

- `original_input` records exactly what the operator supplied;
- `resolved_path` records which filesystem location the program interpreted.

We are **not creating the database during Part 1**. The database concept is introduced because path provenance eventually belongs in structured research metadata rather than informal terminal notes.

---

# 9. Git operation

Before modifying or archiving a path-validation script:

```bash
git status --short
git status
```

After editing—but before staging:

```bash
git diff -- inspect_fasta_gate.py
```

No staging, commit, push, deletion, or repository write is part of Part 1.

---

# 10. Debugging notes

### Wrong: using resolution as proof of existence

```python
print(file_path.resolve())
```

A plausible absolute path can be produced without proving the target is a valid existing FASTA.

Correct separation:

```python
resolved_path = file_path.resolve()

if file_path.exists():
    ...
```

### Wrong: validating suffix before object type

```python
if file_path.suffix == ".fasta":
    print("Accepted")
```

A directory could be named `results.fasta`.

Correct order:

```text
exists
→ regular file
→ suffix
```

### Wrong: case-sensitive suffix validation

```python
file_path.suffix in {".fa", ".fasta"}
```

This rejects `.FASTA`.

Correct:

```python
file_path.suffix.lower() in {".fa", ".fasta"}
```

### Wrong: assuming the script directory is the CWD

Running:

```bash
python scripts/fasta_gate.py
```

does not necessarily make `scripts/` the current working directory. Relative input is interpreted from the terminal’s CWD, not automatically from the script’s location.

### Wrong: treating a path as an instruction

```text
test_sequence.fasta
```

references a filesystem location. It does not execute, inspect, or read the file by itself.

---

# 11. Research/application connection

```text
User-supplied path
→ reproducible path resolution
→ strict FASTA gate
→ accepted file-manifest record
────────────────────────────────
→ later file opening
→ FASTA header removal
→ sequence reconstruction
→ validation of sequence alphabet
→ CLEAVE(sequence)
→ genomic indexing
```

The gate protects the future genomic indexer from:

- empty input;
- wrong working-directory assumptions;
- missing paths;
- directories supplied as files;
- unsupported suffixes;
- unreproducible path records.

## Source references

- [Official Python `pathlib` documentation](https://docs.python.org/3/library/pathlib.html)
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [Official Git `status` documentation](https://git-scm.com/docs/git-status)
- [Official Python `sqlite3` documentation](https://docs.python.org/3/library/sqlite3.html)

**Part 1 accepted by George.**