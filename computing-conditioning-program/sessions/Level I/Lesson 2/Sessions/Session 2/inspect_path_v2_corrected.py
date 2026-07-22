from pathlib import Path


def inspect_path() -> None:
    while True:
        user_input = input("Enter a file or directory path, or 'exit': ").strip()

        if user_input.lower() == "exit":
            print("Path inspector closed.")
            break

        if user_input == "":
            print("Classification: Missing input")
            continue

        file_path = Path(user_input)

        print("Current Working Path:", Path.cwd())
        print("Entered Path:", file_path)
        print("Absolute Path:", file_path.resolve())
        print("Full name:", file_path.name)
        print("Stem:", file_path.stem)
        print("Suffix:", file_path.suffix)
        print("Parent Directory:", file_path.parent)

        if not file_path.exists():
            classification = "Missing"
        elif file_path.is_file():
            classification = "File"
        elif file_path.is_dir():
            classification = "Directory"
        else:
            classification = "Other filesystem object"

        print("Classification:", classification)
        print("=" * 25)


if __name__ == "__main__":
    inspect_path()
