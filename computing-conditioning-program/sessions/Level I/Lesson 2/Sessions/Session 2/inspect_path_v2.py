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
