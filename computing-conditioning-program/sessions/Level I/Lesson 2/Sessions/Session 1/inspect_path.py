# It must import Path
from pathlib import Path

# Accept stripped input,
user_input = input("Enter a file or directory path: ").strip()

# create a Path object, 
file_path = Path(user_input)

# Print metadata here.
# print current working directory, 
print("Current Working Path: ", Path.cwd())

# entered path, absolute path, name, stem, suffix, parent,
print("Entered Path:", file_path) 
print("Absolute Path:", file_path.resolve())
print("Full name:", file_path.name)
print("Stem:", file_path.stem)
print("Suffix:", file_path.suffix)
print("Parent Directory:", file_path.parent)

# and report whether the path exists and is a file, directory, other object, or missing. 
if file_path.exists():
    print("The file exists in:", file_path.parent)
    if file_path.is_file():
        print("Path is file. File's name:", file_path.name)
        pass
    elif file_path.is_dir:
        print("Path is not file, path is directory", file_path.resolve)
    else:
        print("Path is neither file nor directory")
    pass
else:
    print("No file in path")
    pass

# Do not open the file. 
# Submit one test run using data/test_sequence.fasta.
