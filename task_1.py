from pathlib import Path
from typing import Tuple


<<<<<<< HEAD
def total_salary(path: str) -> Tuple[float, float]:
    """
    Read file with salaries and return total and average salary.
    Each line must have format: name,salary
    """
=======
def total_salary(path: str) -> Tuple[int, int]:

>>>>>>> 5fe1d60f89ae8c19ece6df20b7f2fe615205c409
    file_path = Path(path)
    total = 0.0
    count = 0

    try:
        with file_path.open("r", encoding="utf-8") as fh:
            for line in fh:
                parts = line.split(",")
                if len(parts) != 2:
                    continue

                try:
                    salary = float(parts[1].strip())
                except ValueError:
                    continue

                total += salary
                count += 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except OSError as error:
        print(f"Error reading file {file_path}: {error}")

    average = total / count if count else 0.0

    return total, average


if __name__ == "__main__":
    total, average = total_salary("total_salary.txt")

    if total == 0 and average == 0:
        print("No valid salary data to calculate.")
    else:
<<<<<<< HEAD
        print(f"Total Salary: {total:.2f}")
        print(f"Average Salary: {average:.2f}")
=======
        average = total / count
        print(f"Total Salary: {total}")
        print(f"Average Salary: {int(average)}")
        print(f"Number of People: {count}")
>>>>>>> 5fe1d60f89ae8c19ece6df20b7f2fe615205c409
