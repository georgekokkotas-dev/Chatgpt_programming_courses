from pathlib import Path

user_input = input("Enter a file or directory path: ").strip()
file_path = Path(user_input)

print("Current Working Path:", Path.cwd())
print("Entered Path:", file_path)
print("Absolute Path:", file_path.resolve())
print("Full name:", file_path.name)
print("Stem:", file_path.stem)
print("Suffix:", file_path.suffix)
print("Parent Directory:", file_path.parent)

if file_path.exists():
    print("The path exists in:", file_path.parent)

    if file_path.is_file():
        print("Path type: File")
    elif file_path.is_dir():
        print("Path type: Directory")
        print("Resolved directory:", file_path.resolve())
    else:
        print("Path type: Other filesystem object")
else:
    print("Error: Path does not exist")
