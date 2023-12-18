def get_plan(input_file):
    def _get_parsed(line):
        splitted_line = line.split()
        return splitted_line[0], int(splitted_line[1]), splitted_line[2].strip("()")

    with open(input_file, "r") as file:
        data = file.readlines()
        plan = [_get_parsed(line) for line in data]
    return plan


def get_triangle_area(x1, y1, x2, y2, x3, y3):
    return (1 / 2) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


def get_answer_1(plan):
    return


def main():
    plan = get_plan("test_input")
    print(plan)
    print(get_answer_1(plan))


if __name__ == "__main__":
    assert get_triangle_area(0, 0, 2, 0, 0, 1) == 1
    assert get_triangle_area(0, 0, 2, 0, 0, -1) == -1
    main()
