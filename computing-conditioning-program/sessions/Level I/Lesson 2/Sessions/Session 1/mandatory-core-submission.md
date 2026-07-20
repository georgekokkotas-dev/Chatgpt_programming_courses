# Mandatory Core Submission

## Exercise 1 — Path Classification Table

The submitted work correctly identified:

- `C:\Users\George\Research\BRCA2.fasta` — absolute Windows path
- `/home/george/research/BRCA2.fasta` — absolute Linux/WSL path
- `data/BRCA2.fasta` — relative path dependent on the current working directory
- `../data/BRCA2.fasta` — parent-relative path
- `./scripts/inspect_path.py` — current-directory-relative path
- `/mnt/c/Users/George/Desktop/BRCA2.fasta` — absolute WSL/Linux path

The final name, environment, and dependence on the current working directory were stated for each path.

## Exercise 2 — Working-Directory Trace

The submitted trace followed movement through:

```text
/home/george
/home/george/ccp_path_lab
/home/george/ccp_path_lab/scripts
/home/george/ccp_path_lab
/home/george/ccp_path_lab/data
/home/george/ccp_path_lab
/home/george/ccp_path_lab/results
/home/george/ccp_path_lab/scripts
```

The central result was that the same file can be reached or missed depending on the current working directory and the exact relative path expression.

From `/home/george/ccp_path_lab/data`:

```text
test_sequence.fasta
./test_sequence.fasta
```

reach the file, while:

```text
data/test_sequence.fasta
```

would search for `/home/george/ccp_path_lab/data/data/test_sequence.fasta`.

## Exercise 3 — Path Inspector in Pseudocode

```text
START
CLS
PRINT CWD $prints current working directory$
PRINT "TYPE THE FILE'S DIRECTORY: " 
    INPUT ITEM_TYPE = DIR $asks for a path$

SET FILE_PATH = INPUT DIRECTORY $stores it$

IF $file_path.is_file()$
    FILE_PATH ITEM_TYPE = FILE 
    PRINT "IS FILE"
    SET FILE_PATH = #FILE
        ITEM_TYPE = FILE
END IF
IF $file_path.is_dir()$
    FILE_PATH ITEM_TYPE = DIR 
    PRINT "IS DIRECTORY"
    SET FILE_PATH = #DIRECTORY
        ITEM_TYPE = DIR 
END IF

IF
    #FILE IN #DIRECTORY
    CONTINUE
ELSE
    RAISE_ERROR
    PRINT "NO SUCH FILE IN DIRECTORY"
    GO TO LINE 40
END IF

IF NOT $checks existence and opens nothing unless the path exists and is a file
    #FILE 
        ITEM_TYPE = FILE
    RAISE_ERROR 
    PRINT "PATH IS NOT FILE"
    GO TO LINE 40
ELSE
    OPEN READ #FILE
END IF

PRINT FILE_PATH %~~/~~.~~%
$Prints name/extension/parent. If the absolute directory were required, the notation would be %.../~~.~~%$

END
```

In this notation, `#FILE` and `#DIRECTORY` function as type or classification tags, and indentation carries hierarchical meaning.

## Exercise 4 — Python Path Inspector

The submitted program is archived separately as `inspect_path.py`. It:

- imports `Path`;
- strips input;
- creates a `Path` object;
- prints the current working directory;
- prints entered path, absolute path, name, stem, suffix, and parent;
- checks existence;
- classifies file, directory, other object, or missing;
- does not open the file.

### Submitted test run

```text
Enter a file or directory path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4\test_sequence.fasta
Current Working Path:  C:\Users\George\AppData\Local\Programs\Microsoft VS Code
Entered Path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4\test_sequence.fasta
Absolute Path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4\test_sequence.fasta
Full name: test_sequence.fasta
Stem: test_sequence
Suffix: .fasta
Parent Directory: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4
The file exists in: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4
Path is file. File's name: test_sequence.fasta
```

Two method-call corrections are preserved in `inspect_path_corrected.py`:

```python
file_path.is_dir()
file_path.resolve()
```
