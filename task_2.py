from pathlib import Path
from typing import List, Dict


def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Read file with cats data and return list of dicts.
    Each line in file must have format: id,name,age
    """
    file_path = Path(path)
    cats: List[Dict[str, str]] = []

    try:
        with file_path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    continue

                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except OSError as error:
        print(f"Error reading file {file_path}: {error}")

    return cats


if __name__ == "__main__":
    example_path = "cats.txt"
    print(get_cats_info(example_path))

