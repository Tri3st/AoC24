from MyMods.ReadDataFile import read_data

from day2.report import Report

big_data = read_data("./day2/input_day2.txt", mode=1)

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def is_safe(report):
    """
    Check if a report is safe.
    A report is safe if:
    1. Levels are all increasing or all decreasing.
    2. Any two adjacent levels differ by at least 1 and at most 3.
    """
    n = len(report)
    if n < 2:
        return True

    # Determine if the report is strictly increasing or decreasing
    is_increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(n - 1))
    is_decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(n - 1))

    return is_increasing or is_decreasing

def is_safe_with_dampener(report):
    """
    Check if a report can be made safe by removing at most one level.
    """
    # If the report is already safe, no need to remove any level
    if is_safe(report):
        return True

    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False

def part1():
    total = 0
    for line in big_data.split("\n"):
        r = Report(line)
        if r.status == "safe":
            total += 1
        print(r)
    print("Total : ", total)

def part2():
    total = 0
    for l in big_data.split("\n"):
        report = [int(r) for r in l.split()]
        if is_safe_with_dampener(report):
            total += 1
    print("Total : ", total)