
from pathlib import Path


def validate_repository(repo_path):
    file_path = Path(repo_path)

    if not file_path.exists():
        return False, "The path does not exist."

    if not file_path.is_dir():
        return False, "The path is not a directory."

    return True, "The repository path is valid."


def inspect_repository(repo_path):
    file_path = Path(repo_path)

    ignored_directories = {
        ".git",
        "__pycache__",
        ".venv",
        "venv",
    }

    discovered_files = []

    for item in file_path.rglob("*"):
        if not item.is_file():
            continue

