from pathlib import Path
from typing import Tuple


def total_salary(path: str) -> Tuple[int, int]:

    file_path = Path(path)
    total = 0
    count = 0

    try:
        with file_path.open("r", encoding="utf-8") as fh:
            for line in fh:
                parts = line.split(",")
                if len(parts) != 2:
                    continue

                try:
                    salary = int(parts[1].strip())
                except ValueError:
                    continue

                total += salary
                count += 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except OSError as error:
        print(f"Error reading file {file_path}: {error}")

    return total, count


if __name__ == "__main__":
    total, count = total_salary("total_salary.txt")

    if count == 0:
        print("Error: Division by zero. No people to calculate average salary.")
    else:
        average = total / count
        print(f"Total Salary: {total}")
        print(f"Average Salary: {int(average)}")
        print(f"Number of People: {count}")
