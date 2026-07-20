# Part 3 — Correction, Reflection, Mistake Log, and Archive

## Final result

- Mandatory Core completed: **4/4**
- Mandatory completion: **100%**
- Session result: **PASS**
- Final session score: **9.2/10**
- Optional exercises: not attempted and not penalized

## Exercise results

### Exercise 1 — Path Classification

Accepted. The main correction was recognizing `/mnt/c/...` as absolute WSL/Linux syntax rather than Windows syntax.

### Exercise 2 — Working-Directory Trace

Accepted after clarification. The key result was separating the existence of a file from whether a particular relative path resolves to that file from the current working directory.

### Exercise 3 — Path Inspector Pseudocode

Accepted. The pseudocode established input, path storage, current-working-directory reporting, file/directory classification, existence handling, metadata output, and guarded file opening. Indentation and `$...$` comments are part of George's established notation. `#FILE` and `#DIRECTORY` act as classification tags.

### Exercise 4 — Python Path Inspector

Accepted. The submitted file demonstrated a successful file-path run and all required metadata output. Two method references required parentheses in the directory branch:

```python
file_path.is_dir()
file_path.resolve()
```

The submitted file is preserved unchanged; the corrected reference is archived separately.

## `pass`

`pass` is Python's no-operation statement. It performs no action and is commonly used as a temporary placeholder for an otherwise empty block. In the submitted script, the `pass` statements are harmless but unnecessary because the blocks already contain executable statements.

## Mistake log

🟥 WSL-mounted Windows drive classified as Windows syntax.  
🟨 Physical storage location was confused with the syntax interpreted by the active operating environment.  
🟦 `/mnt/c/...` is an absolute Linux/WSL path.  
🟩 `/mnt/c/Users/George/file.fasta` is resolved by WSL.  
🟪 Reinforcement need: separate storage location from path syntax.

🟥 Repeated the current directory name inside a relative path.  
🟨 The project-tree label was confused with the terminal's active location.  
🟦 Relative paths begin from the current working directory.  
🟩 Inside `data`, use `test_sequence.fasta` or `./test_sequence.fasta`.  
🟪 Reinforcement need: resolve each relative component from the active directory.

🟥 Python methods referenced without invocation parentheses.  
🟨 A method object was confused with the result of executing the method.  
🟦 `.is_dir` names the method; `.is_dir()` executes it.  
🟩 Use `file_path.is_dir()` and `file_path.resolve()`.  
🟪 Reinforcement need: distinguish properties from methods.

## Strength log

- Challenged ambiguous specifications instead of memorizing them.
- Distinguished physical files from path expressions used to reach them.
- Translated filesystem reasoning into pseudocode and functioning Python.
- Used real `pathlib` metadata on a FASTA path.
- Completed all mandatory work despite severe fatigue.

## Command gap log

```python
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

Properties: `.name`, `.stem`, `.suffix`, `.parent`  
Methods: `.cwd()`, `.resolve()`, `.exists()`, `.is_file()`, `.is_dir()`

## Research connection

The path inspector forms the input-validation layer for the genomic indexer and FASTA workflow:

```text
FASTA path
→ validate existence
→ confirm regular file
→ inspect suffix
→ read sequence
→ remove headers
→ reconstruct sequence
→ pass sequence to CLEAVE()
```

## Archive status

```text
CCP
└── Level I
    └── Lesson I.2
        └── Session I.2.1
            Status: completed and locked
            Mandatory Core: 4/4
            Final score: 9.2/10
```
