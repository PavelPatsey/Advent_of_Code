import re

INPUT = "input"


def is_overlapped(assignment):
    a = set(range(assignment[0], assignment[1] + 1))
    b = set(range(assignment[2], assignment[3] + 1))
    return a.issubset(b) or b.issubset(a)


def read_input():
    with open(INPUT, "r") as file:
        assignments = file.read().split()
        assignments = [re.split(r",|-", x) for x in assignments]
        assignments = [[int(y) for y in x] for x in assignments]
    return assignments


def main():
    assignments = read_input()
    print(len(list(filter(is_overlapped, assignments))))


if __name__ == "__main__":
    assert is_overlapped([2, 4, 6, 8]) == False
    assert is_overlapped([6, 6, 4, 6]) == True

    main()


# z = x.issubset(y)
