def main() -> str:
    student_marks = {}

    for _ in range(int(input())):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))

    return "%.2f" % (sum(student_marks[input()]) / 3)


if __name__ == "__main__":
    print(main())
