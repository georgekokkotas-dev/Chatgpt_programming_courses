# Mandatory Core Submission — Session I.2.2

```text
CCP — Level I → Lesson I.2 → Session I.2.2
Part 2 — Adaptive Exercise Set

Energy: 4/5
Fatigue: 2/5
Mode: B — Normal Conditioning with increased independence
Theme: Safe path validation, method calls, relative-path debugging, and second implementation
Primary track: Python
Secondary environment: Windows CMD
Operational environment: WSL Ubuntu

SESSION RULES
1. Complete the Mandatory Core first.
2. Do not use model answers or copied final solutions.
3. Record commands, reasoning, outputs, and errors exactly as they occur.
4. Keep properties and methods distinct.
5. Do not open, alter, create, or delete any submitted test file unless an exercise explicitly asks for file creation.
6. Use the current working directory in every relative-path diagnosis.
7. Submit each exercise under its exact label: M1–M4, R1–R4, S1–S3, RI1–RI2.
8. The exercise set contains exactly 13 exercises.

MANDATORY CORE

M1 — Property or Method: Debugging Classification
Active block: Debugging / Error Interpretation
Track: Python
Difficulty: Moderate
Type: D — Drill/Trace
Status: Mandatory Core
Language/environment: Python 3
Tags: [Difficulty: Moderate] [Topic: pathlib members] [Category: Mandatory Core]

Task:
For each expression below:
- classify it as property, method call, method object, or invalid usage;
- state whether parentheses are required;
- predict the kind of result produced;
- correct only the expressions that are wrong.

Expressions:
1. file_path.name - property - It gives the file's name (filename.extesion)
2. file_path.stem() - Correct - file_path.stem - property - it gives the file's name without the extension (filename)
3. file_path.exists() - method - Returns TRUE/FALSE depending on the path's existance
4. file_path.is_dir - Correct: file_path.is_dir() - method - Without the parentheses, it's the method's object. Otherwise, it's a method and it returns TRUE/FALSE depending if the path is a DIRECTORY or a FILE
5. file_path.parent - property - This is a property, it returns the file's parent directory. if the filename.extension is in C:/george/data/filename.extension it returns (/data/filename.extesion)
6. file_path.resolve - property - This property returns the whole directory for the file (C:/george/data"
7. Path.cwd() - method - This method returns the current working directory the program works in. If, for instance, it works in "C:/Users/George/Desktop" it returns "C:/Users/George/Desktop"
8. Path.cwd - method object - This is the method's object. It means that it will return the variable's cwd in this case.

Expected output:
A table with columns:
Expression | Classification | Parentheses required? | Expected result | Corrected expression

Submission format:
Plain text table plus a two-sentence rule explaining the difference between a property and a method.

Template:
Expression:
Classification:
Parentheses required:
Expected result:
Correction:


M2 — Relative-Path Debug Trace
Active block: Files, Paths and Directories / Command-Line Thinking
Track: WSL Ubuntu
Difficulty: Post-Moderate
Type: D — Drill/Trace
Status: Mandatory Core
Language/environment: WSL Ubuntu
Tags: [Difficulty: Post-Moderate] [Topic: relative-path resolution] [Category: Mandatory Core]

Assume:
/home/george/ccp_path_lab/
├── data/
│   └── test_sequence.fasta
├── results/
└── scripts/
    └── inspect_path_v2.py

For each current working directory below, evaluate both candidate paths.

A. Current directory:
/home/george/ccp_path_lab

Candidates:
data/test_sequence.fasta
../data/test_sequence.fasta

Resolved attempted path: 
For data/test_sequence.fasta 
/home/george/ccp_path_lab/data/test_sequence.fasta
../data/test_sequence.fasta
/home/george/data/test_sequence.fasta

Momevents
data/test_sequence.fasta
data -> enter the data folder
test_sequence.fasta -> Runs the file
Exists - Shorter

../data/test_sequence.fasta
.. -> /home/george/ccp_path/lab
data -> enter the data folder
test_sequence.fasta -> Runs the file
Doesn't exist

B. Current directory:
/home/george/ccp_path_lab/scripts

Candidates:
data/test_sequence.fasta
../data/test_sequence.fasta

Resolved attempted path: 
For data/test_sequence.fasta 
/home/george/ccp_path_lab/scripts/data/test_sequence.fasta
../data/test_sequence.fasta
/home/george/ccp_path_lab/data/test_sequence.fasta

Momevents
data/test_sequence.fasta
data -> enter the data folder
test_sequence.fasta -> Runs the file
Doesn't exit

../data/test_sequence.fasta
.. -> /home/george/ccp_path_lab
data -> enter the data folder
test_sequence.fasta -> Inspects the file
Exists - Shorter

C. Current directory:
/home/george/ccp_path_lab/data

Candidates:
test_sequence.fasta
data/test_sequence.fasta

Resolved attempted path: 
For data/test_sequence.fasta 
/home/george/ccp_path_lab/data/test_sequence.fasta
data/test_sequence.fasta
/home/george/ccp_path_lab/data/data/test_sequence.fasta

Momevents
test_sequence.fasta
test_sequence.fasta -> Inspects the file
Exists - Shorter

data/test_sequence.fasta
data -> enter the data folder
test_sequence.fasta -> Inspects the file
Doesn't Exist

D. Current directory:
/home/george/ccp_path_lab/results

Candidates:
../data/test_sequence.fasta
./data/test_sequence.fasta

Resolved attempted path: 
For ../data/test_sequence.fasta
/home/george/ccp_path_lab/data/test_sequence.fasta
./data/test_sequence.fasta
/home/george/ccp_path_lab/results/data/test_sequence.fasta

Momevents
..data/test_sequence.fasta
.. -> goes back to /home/george/ccp_path_lab
data -> enter the data folder
test_sequence.fasta -> Runs the file
Exists - Shorter

./data/test_sequence.fasta
. -> starts from /results
data -> enter the data folder
test_sequence.fasta -> Runs the file
Doesn't Exist.

Task:
For every candidate:
- write the fully resolved attempted path;
- state whether it exists under the supplied tree;
- explain the movement represented by each path component;
- identify the shortest valid relative path to the FASTA from that working directory.

Expected output:
Eight resolved-path analyses and four shortest valid relative paths.

Submission format:
One labelled block for A, B, C, and D.

M3 — Safe Path Inspector in George’s Pseudocode
Active block: Pseudocode / Problem Decomposition
Track: BASIC-style pseudocode
Difficulty: Post-Moderate
Type: A — Application
Status: Mandatory Core
Language/environment: George’s established pseudocode notation
Tags: [Difficulty: Post-Moderate] [Topic: validation control flow] [Category: Mandatory Core]

Task:
Write complete pseudocode for a second-generation path inspector that:
- prints the current working directory;
- requests a file or directory path;
- strips leading and trailing whitespace;
- rejects empty input;
- stores the input as FILE_PATH;
- prints entered path, absolute path, name, stem, suffix, and parent; (Note: I definitely forgot these!!!!)
- checks existence;
- classifies the path as #FILE, #DIRECTORY, #OTHER, or #MISSING;
- prints one specific message for each classification;
- opens nothing;
- terminates cleanly after any error.

Use indentation meaningfully and preserve your $comment$ notation.

START
CLS
PRINT CWD

PRINT "WRITE THE FILE'S NAME OR THE DIRECTORY: " 
	INPUT ITEM_TYPE = DIR OR ITEM_TYPE = FILE $Ask for either of them, a file or a directory$

GO TO LINE 50 $Removes whitespace and newline$
	REMOVE WHITESPACE AND "/N"
END GO TO

CONTINUE $Continues forward$

IF NOT $It checks whether there is an input. In case there isn't one, it prints "ERROR: NO INPUT"$
	LINE 50
	PRINT "ERROR: NO INPUT"
	GO TO LINE 50
	PRINT "PLEASE INSERT A FILE OR A DIRECTORY: "
		INPUT ITEM_TYPE = DIR OR ITEM_TYPE = FILE
	END GO TO
END IF

SET FILE_PATH = INPUT $Stores INPUT as FILE_PATH$
PRINT FILE_PATH $Prints the input$
PRINT FILE_PATH $Prints the absolute directory$
	ABS
PRINT FILE_PATH $Prints the file path's name$
	NAME
PRINT FILE_PATH $Prints the file's name without the extension$
	STEM
PRINT FILE_PATH $Prints the file's extension$
	SUFFIX
PRINT FILE_PATH $Takes the absolute path and keeps only the Parent directory, hence ../ and not ../../$
	ABS ../

IF $Checks existance of file path, essentially, if the file or directory exists and assigns $MISSING$
	FILE_PATH = TRUE
	PRINT "FILE PATH EXISTS"
ELSE
	PRINT "FILE PATH DOESN'T EXIST"
	SET FILE_PATH = #MISSING
		ITEM_TYPE = MISSING
END IF

IF $Checks #DIRECTORY, #FILE, #OTHER and assigns accordingly$
	FILE_PATH ITEM_TYPE = DIR
	PRINT "IS DIRECTORY"
	SET FILE_PATH = #DIRECTORY
		ITEM_TYPE = DIR
ELIF
	FILE_PATH ITEM_TYPE = FILE
	PRINT "IS FILE"
	SET FILE_PATH = #FILE
		ITEM_TYPE = FILE
ELSE
	PRINT "IS OTHER"
	SET FILE_PATH = #OTHER
		ITEM_TYPE = OTHER

END IF

CONTINUE $Continues forward$

END
	
Expected output:
One complete START-to-END pseudocode algorithm with no unclosed IF block and no unreachable command after a terminating instruction.

Submission format:
Plain text pseudocode followed by a short explanation of:
1. where existence is checked;
	We look for the path's existance at the very early stage of the algorithm, so as to keep it running smoothly and consistently.
2. where classification occurs;
	Right after the existence check.
3. how the algorithm prevents further execution after invalid input.
	We used several GO TO LINE loops, in order to prevent crashing in any form. We also decided that RAISING an error would fatally crash the program, so we opted to give the user more chances to input valid directories.

Template:
START
CLS

$ input and empty-input validation $

$ path construction and metadata $

$ existence decision $

$ classification decision $

FINISH:
END

(Some things happen just because i misplaced something, not because i don't know where they should go. Stop with that patronising crap!)


M4 — Python Path Inspector Version 2
Active block: Python Programming / Testing / Debugging
Track: Python
Difficulty: Post-Moderate
Type: A — Application/Project
Status: Mandatory Core
Language/environment: Python 3
Tags: [Difficulty: Post-Moderate] [Topic: pathlib validation] [Category: Mandatory Core]

Task:
Create inspect_path_v2.py.

Requirements:
- import Path from pathlib;
- accept stripped input;
- reject empty input before constructing Path("");
- construct one Path object for non-empty input;
- print current working directory;
- print entered path;
- print resolved absolute path;
- print name, stem, suffix, and parent;
- report exactly one classification: File, Directory, Other filesystem object, or Missing;
- use method-call parentheses correctly;
- contain no pass statements;
- do not open the path.

Required tests:
1. Existing FASTA file using a valid relative path.
2. Existing directory.
3. Missing path.
4. Empty input.

Expected output:
Four terminal runs showing four distinct outcomes without a traceback.

Submission format:
- complete Python source;
- exact command used to run it;
- all four inputs;
- all four terminal outputs;
- any error encountered and the correction you made.

Template:
from pathlib import Path

user_input = input("Enter a file or directory path: ").strip()

# Empty-input branch

# Non-empty Path construction and metadata

# One classification chain

from pathlib import Path # import Path from pathlib;

print("=" * 25)
user_input = input("Enter a file or directory path: ").strip() # accept stripped input;
print("=" * 25)

# create a Path object, 
file_path = Path(user_input)

while True:
    if user_input == "": # reject empty input before constructing Path("");
        print("=" * 25)
        user_input = input("Enter a file or directory path: ").strip()
        file_path = Path(user_input)
        print("=" * 25)
        continue

    elif user_input == "exit":
        break

    elif not file_path.exists():
        print("=" * 25)
        print("File path doesn't exist.")
        user_input = input("Enter a file or directory path: ").strip()
        file_path = Path(user_input)
        print("=" * 25)
        continue

    elif file_path.exists(): # construct one Path object for non-empty input;
        print("=" * 25)
        print("Current Working Path: ", Path.cwd()) # print current working directory;
        print("Entered Path:", file_path) # print entered path;
        print("Absolute Path:", file_path.resolve()) # print resolved absolute path;
        print("Full name:", file_path.name) # print name, stem, suffix, and parent;
        print("Stem:", file_path.stem)
        print("Suffix:", file_path.suffix)
        print("Parent Directory:", file_path.parent)
        print("The file exists in:", file_path.parent)
        if file_path.is_file(): # report exactly one classification: File, Directory, Other filesystem object, or Missing;
            print("Path is file. File's name:", file_path.name)
        elif file_path.is_dir():
            print("Path is not file, path is directory:", file_path.resolve())
        print("=" * 25)
        user_input = input("Enter a file or directory path: ").strip()
        file_path = Path(user_input)
    else:
        print("Path is neither file nor directory")
        user_input = input("Enter a file or directory path: ").strip()
        file_path = Path(user_input)
        continue 


C:\Users\George\Desktop\CCP Lessons\l1_les2_s2>python inspect_pathv2.py
=========================
Enter a file or directory path:
=========================
=========================
Enter a file or directory path: dfgdfgd
=========================
=========================
File path doesn't exist.
Enter a file or directory path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4
=========================
=========================
Current Working Path:  C:\Users\George\Desktop\CCP Lessons\l1_les2_s2
Entered Path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4
Absolute Path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4
Full name: l1_les1_s4
Stem: l1_les1_s4
Suffix:
Parent Directory: C:\Users\George\Desktop\CCP Lessons
The file exists in: C:\Users\George\Desktop\CCP Lessons
Path is not file, path is directory: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4
Insert an input directory:
=========================
Enter a file or directory path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4\test_sequence.fasta
=========================
Current Working Path:  C:\Users\George\Desktop\CCP Lessons\l1_les2_s2
Entered Path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4\test_sequence.fasta
Absolute Path: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4\test_sequence.fasta
Full name: test_sequence.fasta
Stem: test_sequence
Suffix: .fasta
Parent Directory: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4
The file exists in: C:\Users\George\Desktop\CCP Lessons\l1_les1_s4
Path is file. File's name: test_sequence.fasta
Insert an input directory:
=========================
Enter a file or directory path: exit
```
