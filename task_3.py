import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_usage() -> None:

    script_name = Path(sys.argv[0]).name
    print(f"Usage: python {script_name} <directory_path>")


def validate_directory(path_str: str) -> Path:

    path = Path(path_str).expanduser().resolve()

    if not path.exists():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Path does not exist: {path}")
        raise SystemExit(1)

    if not path.is_dir():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Path is not a directory: {path}")
        raise SystemExit(1)

    return path


def print_tree(directory: Path, prefix: str = "") -> None:
 
    entries = sorted(directory.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    entries_count = len(entries)

    for index, entry in enumerate(entries):
        connector = "┗━━ " if index == entries_count - 1 else "┣━━ "

        if entry.is_dir():
            color = Fore.BLUE + Style.BRIGHT
        else:
            color = Fore.GREEN

        print(f"{prefix}{connector}{color}{entry.name}{Style.RESET_ALL}")

        if entry.is_dir():
            # Determine the prefix for child elements
            child_prefix = prefix + ("    " if index == entries_count - 1 else "┃   ")
            print_tree(entry, child_prefix)

def main() -> None:

    init(autoreset=False)

    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Warning:{Style.RESET_ALL} directory path argument is required.")
        print_usage()
        raise SystemExit(1)

    dir_path = validate_directory(sys.argv[1])

    # Print root directory name
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{dir_path}{Style.RESET_ALL}")
    print_tree(dir_path)


if __name__ == "__main__":
    main()
