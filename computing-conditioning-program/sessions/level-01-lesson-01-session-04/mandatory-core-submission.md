# Mandatory Core Submission

## M1 — Programming Workflow

1. **Problem:** Read a FASTA file, remove header lines, join sequence lines, and print sequence length.
2. **Requirements:** BASIC-style pseudocode, Python 3, Windows CMD/WSL awareness.
3. **Algorithm:** Open FASTA → read line by line → remove lines containing `>` → validate A/T/C/G/N → join valid sequence lines → print line count, sequence length, and sequence.
4. **Pseudocode:** Developed in a BASIC-inspired notation using `OPEN READ`, `FOR /LINES`, `REMOVE /LINES`, `COUNT`, `SUM`, and `PRINT`.
5. **Implementation:** Python using `pathlib.Path`, `with open`, a line loop, `startswith`, `strip`, `upper`, set-based nucleotide validation, `+=`, and `len`.
6. **Testing:** Tested against `test_sequence.fasta`, yielding 4 sequence lines and 104 bases.
7. **Debugging:** The algorithm worked after guided correction; the principal implementation issue was Python indentation.
8. **Documentation:** Comments and an explanation of the pseudocode-to-Python mapping were supplied.
9. **Git Archive:** Archived in this repository with the session files and correction report.

## M2 — FASTA Problem Decomposition

1. Open and read a `.fa` or `.fasta` file.
2. Assign the file path to a variable.
3. Inspect the file line by line.
4. Ignore lines beginning with `>`.
5. Remove whitespace and newline characters.
6. Convert sequence letters to uppercase.
7. Validate that all characters belong to A, T, C, G, or N.
8. Join accepted lines into one sequence.
9. Count sequence lines and bases.
10. Print the sequence and metadata.

## M3 — BASIC-Style Pseudocode

```text
START
CLS
OPEN READ %~~.fa% OR %~~.fasta%
SET FILE_PATH = %~~.fa% OR %~~.fasta%
SET SEQUENCE = %~~%
SET NUCLEOTIDES = "A", "T", "G", "C", "N"

FOR /LINES
    IF ">" IN /LINES
        REMOVE /LINES
        CONTINUE
    END IF

    IF ANY NOT NUCLEOTIDES IN /LINES
        PRINT ERROR = "Invalid Values in %SEQUENCE%"
    ELSE
        CONTINUE
    END IF
END FOR

COUNT SEQUENCE /LINES
PRINT "NUMBER OF LINES"
SET LINES = /LINES
COUNT LINES /%NUCLEOTIDES%
PRINT "LINE LENGTH"
SET FULL_SEQUENCE = SUM /LINES
PRINT FULL_SEQUENCE
END
```

## M4 — Implementation and Test

The submitted code is preserved in `fasta_reader_submission.py`. An indentation-corrected reference is stored in `fasta_reader_corrected.py`.

### Test FASTA

```text
>test_sequence_001
ATGCGTACGTTAGCCTAGGCTAACGT
GGTACCNNTTAGCGATCGATCGTACG
TTACGATCGGATCCGATGCTAGCTAA
CGTAGCTAGGCTTACGATCGTANNNG
```

### Expected Corrected Output

```text
Number of lines: 4
Full sequence length: 104 bases
ATGCGTACGTTAGCCTAGGCTAACGTGGTACCNNTTAGCGATCGATCGTACGTTACGATCGGATCCGATGCTAGCTAACGTAGCTAGGCTTACGATCGTANNNG
```
