# Computing Conditioning Program (CCP)

**Level I — Lesson 2:** Files, Folders, Paths, and Working Directories  
**Lesson status:** In progress  
**Current lesson score:** **9.1/10**

## Lesson sessions

- [Session 1](Sessions/Session%201/README.md) — completed and passed, **9.2/10**
- [Session 2](Sessions/Session%202/README.md) — completed and passed, **9.0/10**

## Current lesson focus

- filesystem structure;
- files and directories;
- absolute, relative, parent-relative, and current-directory-relative paths;
- current working directory;
- Windows, Linux, and WSL path syntax;
- Python `pathlib` properties, methods, and method objects;
- safe empty-input validation;
- mutually exclusive filesystem classification;
- BASIC-style pseudocode;
- preparation for FASTA input handling.

## Session 1 result

- Mandatory Core: 4/4 completed
- Session result: PASS
- Main strength: persistent path reasoning across Windows, Linux/WSL, pseudocode, and Python
- Main reinforcement need: distinguishing properties from methods and remembering method-call parentheses

## Session 2 result

- Mandatory Core: 4/4 completed
- Session result: PASS
- Final session score: **9.0/10**
- Main strength: complete relative-path resolution and a functioning retry-based Python path inspector
- Main reinforcement need: validate empty input before constructing `Path`, and keep Missing/File/Directory/Other in one reachable classification chain
- Optional categories: deferred without penalty because the ending state was Energy 1/5 and Fatigue 4/5

## Research connection

Validated paths will feed the future FASTA reader and `CLEAVE(sequence)` pipeline. The next reinforcement step is to turn the path inspector into a strict FASTA intake gate before any file is opened.

## Next course target

**Level I → Lesson I.2 → Session I.2.3**
