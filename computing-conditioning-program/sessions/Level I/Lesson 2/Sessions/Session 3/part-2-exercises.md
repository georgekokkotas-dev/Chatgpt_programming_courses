# CCP — Level I → Lesson I.2 → Session I.2.3
## Part 2 — Adaptive Exercise Set

**Energy:** 5/5  
**Fatigue:** 2/5  
**Mode:** B — Normal Conditioning, upper-band independence  
**Theme:** Strict FASTA intake gates, path-resolution verification, validation algorithms, and structured manifest records  
**Primary track:** Python  
**Secondary environment:** WSL Ubuntu  
**Operational layer:** Ubuntu CLI, Windows CMD, Git  
**Side-subjects:** Algorithm theory; Databases and Structured Data

## Session rules

1. Complete **M1–M4** before optional exercises.
2. The set contains exactly **13 exercises**.
3. Submit every exercise under its exact label.
4. Do not copy the Part 1 demonstration as a final solution.
5. Do not open or read any FASTA file during this session.
6. Do not alter supplied research files.
7. Temporary test objects may be created only where an exercise explicitly permits it.
8. Resolve every relative path from the stated current working directory.
9. Empty input must be handled before constructing `Path("")`.
10. Every validation run must end with exactly one final status.
11. Record commands, outputs, errors, and corrections exactly.
12. M4 is the Mandatory Core research-integration exercise.
13. No full Hardest/THE Hardest task is assigned in this session; the highest required tier is **Harder**.

---

# MANDATORY CORE

## M1 — FASTA-Gate Decision Trace

**Active block:** Algorithms / Files, Paths and Directories / Debugging  
**Track:** Algorithmic thinking and path tracing  
**Difficulty:** Hard  
**Type:** D — Drill/Trace  
**Status:** Mandatory Core  
**Language/environment:** Language-independent, WSL path semantics  
**Tags:** `[Difficulty: Hard] [Topic: guard-clause tracing] [Category: Mandatory Core]`

Assume:

```text
/home/george/ccp_fasta_gate/
├── data/
│   ├── BRCA2_reference.FASTA
│   ├── empty.fa
│   └── notes.txt
├── results/
│   └── archive.fasta/
└── scripts/
    └── fasta_gate.py
```

`archive.fasta` is a **directory**, despite its suffix-like name. All other entries shown under `data` are existing regular files. Their contents are irrelevant and must not be opened.

Trace these eight cases:

| Case | Current working directory | Input |
|---|---|---|
| 1 | `/home/george/ccp_fasta_gate/scripts` | `../data/BRCA2_reference.FASTA` |
| 2 | `/home/george/ccp_fasta_gate/scripts` | `data/BRCA2_reference.FASTA` |
| 3 | `/home/george/ccp_fasta_gate` | `data/notes.txt` |
| 4 | `/home/george/ccp_fasta_gate/results` | `archive.fasta` |
| 5 | `/home/george/ccp_fasta_gate/results` | `../data/empty.fa` |
| 6 | `/home/george/ccp_fasta_gate/data` | `BRCA2_reference.FASTA` |
| 7 | `/home/george/ccp_fasta_gate/scripts` | empty input |
| 8 | `/home/george/ccp_fasta_gate` | `results/archive.fasta` |

For every case state:

- stripped input;
- whether a `Path` object should be constructed;
- fully resolved attempted path, when applicable;
- existence;
- classification;
- original suffix;
- normalized suffix;
- first guard clause that decides the result;
- exactly one final status.

Use only these final statuses:

```text
REJECTED_EMPTY_INPUT
REJECTED_MISSING
REJECTED_DIRECTORY
REJECTED_OTHER_OBJECT
REJECTED_SUFFIX
ACCEPTED_FASTA
```

### Expected output

Eight labelled decision traces with no contradictory statuses.

### Submission format

```text
Case 1
CWD:
Input:
Construct Path:
Resolved attempted path:
Exists:
Classification:
Original suffix:
Normalized suffix:
Deciding guard:
Final status:
```

---

## M2 — Complete Guard-Clause Algorithm

**Active block:** Algorithmic Thinking / Pseudocode / Problem Decomposition  
**Track:** George’s BASIC-style pseudocode  
**Difficulty:** Hard  
**Type:** A — Application  
**Status:** Mandatory Core  
**Language/environment:** Plain-text pseudocode  
**Tags:** `[Difficulty: Hard] [Topic: validation algorithm] [Category: Mandatory Core]`

Write a complete START-to-END FASTA validation algorithm.

It must:

- print the current working directory;
- request a path;
- strip surrounding whitespace;
- support the command `exit`;
- reject empty input before path construction;
- construct exactly one path object for non-empty, non-exit input;
- print the entered and resolved attempted paths;
- classify Missing, File, Directory, or Other;
- accept only regular files ending in `.fa` or `.fasta`, case-insensitively;
- assign exactly one final validation status;
- prevent rejected cases from falling through into later branches;
- open nothing;
- terminate cleanly;
- preserve meaningful indentation and `$...$` comments.

### Algorithm-theory component

After the pseudocode, explain:

1. why the guards are ordered as they are;
2. the maximum number of major validation decisions needed for an accepted path;
3. where short-circuiting occurs;
4. why suffix validation alone is insufficient.

### Expected output

One complete algorithm with:

- no unclosed branch;
- no unreachable command after termination;
- no possible double status;
- no classification after an empty-input rejection.

### Submission format

Plain-text pseudocode followed by four numbered algorithm notes.

### Template

```text
START
CLS

$ input stage $

$ empty and exit guards $

$ path construction $

$ existence and classification guards $

$ suffix guard $

$ accepted branch $

FINISH:
PRINT FINAL_STATUS
END
```

---

## M3 — Implement `fasta_gate.py`

**Active block:** Python Programming / Testing / Debugging  
**Track:** Python  
**Difficulty:** Hard  
**Type:** A — Application/Project  
**Status:** Mandatory Core  
**Language/environment:** Python 3  
**Tags:** `[Difficulty: Hard] [Topic: strict FASTA validation] [Category: Mandatory Core]`

Create:

```text
fasta_gate.py
```

### Requirements

The program must:

- import `Path` from `pathlib`;
- print the current working directory;
- accept stripped input;
- support `exit`;
- reject empty input before constructing a `Path`;
- construct one `Path` object for a valid textual input;
- print the entered path;
- print the resolved attempted path;
- classify the target as File, Directory, Other filesystem object, or Missing;
- normalize the suffix only for comparison;
- accept `.fa` and `.fasta` case-insensitively;
- print the original suffix;
- print exactly one final validation status;
- contain no `pass`;
- contain no `open()`, `.read()`, `.write()`, deletion, or modification operation.

### Required tests

Run these six outcomes:

1. empty input;
2. missing path;
3. existing directory;
4. existing non-FASTA file;
5. existing lowercase `.fa` or `.fasta` file;
6. existing uppercase `.FASTA` file.

At least one accepted FASTA must be supplied through a valid **relative path**.

### Testing rule

A single continuous interactive run is acceptable if it clearly demonstrates all six outcomes and clean exit behaviour.

### Expected output

- complete source;
- exact command used;
- six labelled inputs and outputs;
- no traceback;
- one final status per validation attempt;
- error-and-correction notes for defects encountered during development.

### Submission format

1. Python source  
2. Command transcript  
3. Test evidence  
4. Debugging notes

### Template

```python
from pathlib import Path

# Print program heading and CWD

# Input

# Empty-input and exit decisions

# Construct Path only after validation

# Mutually exclusive filesystem decisions

# Suffix decision

# Exactly one final status
```

---

## M4 — Research File-Manifest Record

**Active block:** Bioinformatics Computing / Research Pipelines / Databases and Structured Data  
**Track:** Python + structured research metadata  
**Difficulty:** Harder  
**Type:** A — Research/Application  
**Status:** Mandatory Core — Research Integration  
**Language/environment:** Python 3, terminal output only  
**Tags:** `[Difficulty: Harder] [Topic: FASTA manifest provenance] [Category: Mandatory Core] [Research Integration]`

Extend the FASTA gate so every validation attempt produces one structured manifest record.

The required fields are:

```text
original_input
source_cwd
resolved_path
name
suffix
classification
validation_status
```

### Requirements

- Print the seven fields in a stable order.
- Preserve the exact stripped input in `original_input`.
- Record `Path.cwd()` in `source_cwd`.
- For empty input, do not construct a path merely to fill the remaining fields.
- Develop a consistent placeholder policy for fields that cannot exist.
- Record the original suffix, not only its lowercase comparison form.
- Record exactly one classification.
- Record exactly one validation status.
- Produce one record for rejected inputs as well as accepted inputs.
- Do not connect to SQLite yet.
- Do not write the manifest to disk.
- Do not open or read the FASTA.

### Required evidence

Generate manifest records for:

1. accepted relative FASTA;
2. accepted uppercase `.FASTA`;
3. existing non-FASTA file;
4. directory named with `.fasta`;
5. missing `.fasta` path;
6. empty input.

### Database side-question

After the implementation, state:

- which field could serve as a database primary key only after adding a separate identifier;
- which fields should be `NOT NULL`;
- why `original_input` and `resolved_path` are not interchangeable;
- whether `resolved_path` alone guarantees the same file contents over time.

### Expected output

Six structured records, source code, terminal evidence, and four database-design answers.

### Submission format

- Python source;
- six manifest outputs;
- field-policy explanation;
- database-design answers;
- development error log.

### Template

```text
MANIFEST RECORD
original_input:
source_cwd:
resolved_path:
name:
suffix:
classification:
validation_status:
END RECORD
```

---

# RECOMMENDED

## R1 — Verify the Gate with WSL Commands

**Active block:** Ubuntu CLI / Command-Line Thinking / Testing  
**Track:** WSL Ubuntu  
**Difficulty:** Post-Moderate  
**Type:** C — Command/Syntax  
**Status:** Recommended  
**Language/environment:** WSL Ubuntu shell  
**Tags:** `[Difficulty: Post-Moderate] [Topic: CLI verification] [Category: Recommended]`

From:

```text
/home/george/ccp_fasta_gate/scripts
```

use commands to verify:

- current working directory;
- project-tree contents;
- resolved path of `../data/BRCA2_reference.FASTA`;
- existence;
- regular-file status;
- final name;
- parent path;
- execution of `fasta_gate.py` with the relative FASTA path.

Use, where applicable:

```text
pwd
ls
realpath
test
basename
dirname
python3
```

### Expected output

A terminal transcript proving that the CLI and Python program interpret the same location.

### Submission format

Command, exact output, and one-sentence diagnosis after each command.

---

## R2 — Windows CMD Translation

**Active block:** Windows CMD / Operating System Concepts  
**Track:** Windows CMD  
**Difficulty:** Post-Moderate  
**Type:** C — Command/Syntax  
**Status:** Recommended  
**Language/environment:** Windows CMD  
**Tags:** `[Difficulty: Post-Moderate] [Topic: cross-platform verification] [Category: Recommended]`

Assume the project is stored at:

```text
C:\Users\George\Desktop\ccp_fasta_gate
```

Translate the R1 workflow into Windows CMD.

Cover:

- current directory;
- directory listing;
- moving into `scripts`;
- checking the sibling `data` directory;
- checking whether a FASTA path exists;
- running the Python script;
- returning to the project root.

### Expected output

A valid CMD command sequence and comparison notes for the WSL commands that do not have identical CMD spelling.

### Submission format

Command block plus command-comparison notes.

---

## R3 — Relative SQLite Database-Path Trace

**Active block:** Databases and Structured Data / Files, Paths and Directories  
**Track:** Python path reasoning  
**Difficulty:** Moderate  
**Type:** D — Drill/Trace  
**Status:** Recommended  
**Language/environment:** Python + filesystem reasoning  
**Tags:** `[Difficulty: Moderate] [Topic: database file paths] [Category: Recommended]`

Do **not** execute the connection.

Given:

```python
sqlite3.connect("manifest.db")
```

resolve where the database path would point from each CWD:

```text
A. /home/george/ccp_fasta_gate
B. /home/george/ccp_fasta_gate/scripts
C. /home/george/ccp_fasta_gate/results
D. /home/george
```

Then evaluate:

```python
sqlite3.connect("../results/manifest.db")
```

from the `scripts` directory.

For every case state:

- supplied database path;
- CWD;
- resolved attempted database location;
- whether the path is absolute or relative;
- risk created by using that location accidentally.

### Expected output

Five labelled database-path traces and a short reproducibility conclusion.

### Submission format

Plain-text table plus one paragraph.

---

## R4 — Git Working-Tree Evidence

**Active block:** Git Basics / Documentation  
**Track:** Git  
**Difficulty:** Moderate  
**Type:** C — Command/Syntax  
**Status:** Recommended  
**Language/environment:** Git CLI  
**Tags:** `[Difficulty: Moderate] [Topic: pre-archive inspection] [Category: Recommended]`

Assume `fasta_gate.py` and the exercise submission are inside a Git repository.

Run commands to show:

- compact status;
- full status;
- unstaged changes to `fasta_gate.py`;
- staged changes, if any;
- the repository root.

Do not stage, commit, push, restore, or delete anything.

### Expected output

A terminal transcript and explanation of every observed status symbol or message.

### Submission format

Commands, output, and interpretation.

---

# STRETCH

## S1 — Refactor Validation into Functions

**Active block:** Functions and Procedures / Modular Programming  
**Track:** Python  
**Difficulty:** Hard  
**Type:** A — Application  
**Status:** Stretch  
**Language/environment:** Python 3  
**Tags:** `[Difficulty: Hard] [Topic: modular validation] [Category: Stretch]`

Refactor the validation logic into functions.

At minimum, design:

```python
def classify_path(path):
    ...

def validate_fasta_path(path):
    ...
```

Constraints:

- each function performs one clearly defined responsibility;
- classification and FASTA suitability remain separate concepts;
- functions return information rather than printing everything internally;
- the main program handles user interaction and reporting;
- no file is opened.

### Expected output

Runnable source, six tests, and an explanation of parameters, return values, and separation of responsibilities.

### Submission format

Source, tests, and architecture note.

---

## S2 — Branch-Coverage Test Matrix

**Active block:** Testing / Algorithms / Debugging  
**Track:** Python testing design  
**Difficulty:** Very Hard  
**Type:** A — Application/Project  
**Status:** Stretch  
**Language/environment:** Python 3  
**Tags:** `[Difficulty: Very Hard] [Topic: branch coverage] [Category: Stretch]`

Construct a test matrix that reaches every meaningful validation branch.

Include at least:

- empty input;
- exit;
- missing relative path;
- missing absolute path;
- existing directory;
- directory with `.fasta` name;
- existing other filesystem object, where safely available;
- `.txt` regular file;
- lowercase `.fa`;
- lowercase `.fasta`;
- uppercase `.FASTA`;
- path containing spaces.

For each test state:

- test ID;
- CWD;
- input;
- branch expected;
- final status expected;
- actual status;
- pass/fail;
- defect discovered.

### Expected output

A completed test matrix and branch-coverage argument showing which branch every test exercises.

### Submission format

Table plus terminal evidence for at least six cases.

---

## S3 — POSIX “Other Filesystem Object” Test

**Active block:** Ubuntu CLI / Filesystem Concepts / Python Testing  
**Track:** WSL Ubuntu + Python  
**Difficulty:** Harder  
**Type:** A — Application/Debugging  
**Status:** Stretch  
**Language/environment:** WSL Ubuntu  
**Tags:** `[Difficulty: Harder] [Topic: non-file filesystem objects] [Category: Stretch]`

Inside a disposable test directory, safely create a named pipe using:

```text
mkfifo
```

Then:

- inspect it with `ls -l`;
- check `test -e`;
- check `test -f`;
- check `test -d`;
- supply it to the Python gate;
- record its classification;
- remove only the named pipe and disposable test directory afterward.

Do not write into or read from the pipe.

### Expected output

Command transcript demonstrating an existing object that is neither a regular file nor a directory.

### Submission format

Commands, outputs, Python result, explanation, and cleanup evidence.

---

# RESEARCH / APPLICATION INTEGRATION

## RI1 — GitHub-Ready FASTA-Gate Mini-Project

**Active block:** Project Architecture / Reproducible Computing / GitHub Publication  
**Track:** Git + Python research project design  
**Difficulty:** Hard  
**Type:** A — Research/Application  
**Status:** Research Integration  
**Language/environment:** Repository architecture  
**Tags:** `[Difficulty: Hard] [Topic: reproducible FASTA validation] [Category: Research Integration]`

Design this project:

```text
fasta-intake-gate/
```

It must include:

- `README.md`;
- submitted source;
- corrected source when applicable;
- pseudocode;
- test-data directory;
- test-output directory;
- manifest-record examples;
- exercise submission;
- Part 3 correction report;
- mistake log;
- command gap log;
- prerequisite gap log;
- Git log;
- database-design note.

For every item state its purpose.

Also provide planned commands for:

- status inspection;
- staging;
- commit;
- final status.

Do not provide or execute a push command.

### Expected output

Complete directory tree, purpose list, command plan, and one professional commit message.

### Submission format

Tree, file-purpose descriptions, command block, and commit message.

---

## RI2 — Validation-Event Database Design

**Active block:** Databases and Structured Data / Research Pipelines / Technical Writing  
**Track:** SQLite design  
**Difficulty:** Harder  
**Type:** A — Research/Application  
**Status:** Research Integration  
**Language/environment:** SQL design; no connection required  
**Tags:** `[Difficulty: Harder] [Topic: validation provenance database] [Category: Research Integration]`

Design an SQLite table named:

```text
validation_event
```

It must represent repeated FASTA validation attempts.

Include fields for:

- unique event identifier;
- original input;
- source CWD;
- resolved path;
- name;
- suffix;
- classification;
- validation status;
- session identifier;
- test-case identifier.

Determine:

- SQLite data type for every field;
- primary key;
- required `NOT NULL` constraints;
- fields that may legitimately be null;
- appropriate status-value restrictions;
- whether resolved paths should be unique;
- how repeated validation attempts should be preserved.

Write three research questions that could later be answered with SQL queries, such as identifying recurring missing paths or working directories associated with failures.

### Expected output

- one `CREATE TABLE` statement;
- field-by-field design explanation;
- integrity-rule explanation;
- three proposed research queries described in words.

### Submission format

SQL block followed by structured design notes.

---

# END OF EXERCISES
