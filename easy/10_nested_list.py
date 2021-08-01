"""
Given the names and grades for each student in a Physics class of students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.
"""


def calc(lsts: list) -> str:
    all_grades = sorted(set([marks for _, marks in data]))
    return f"\n".join([a for a, b in sorted(data) if b == all_grades[1]])


if __name__ == "__main__":
    data = [[input(), float(input())] for _ in range(int(input()))]
    print(calc(data))
