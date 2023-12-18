DIR_DICT = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
DIR_LIST = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def get_plan(input_file):
    def _get_parsed(line):
        splitted_line = line.split()
        return (
            DIR_DICT[splitted_line[0]],
            int(splitted_line[1]),
            splitted_line[2].strip("()"),
        )

    with open(input_file, "r") as file:
        data = file.readlines()
        plan = [_get_parsed(line) for line in data]
    return plan


def get_triangle_area(x1, y1, x2, y2, x3, y3):
    return (1 / 2) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


def get_answer(plan, part_2=False):
    """
    see Pick's theorem
    A = i + b/2 - 1
    """
    points = [(0, 0)]
    b = 0
    for dir_, n, hexadecimal_code in plan:
        if part_2:
            n = int(hexadecimal_code[1:-1], 16)
            dir_ = DIR_LIST[int(hexadecimal_code[-1])]
        b += n
        x, y = points[-1]
        dx, dy = dir_[0] * n, dir_[1] * n
        points.append((x + dx, y + dy))

    triangle_areas = [
        get_triangle_area(0, 0, x2, y2, x3, y3)
        for (x2, y2), (x3, y3) in zip(points[1:], points[2:])
    ]
    area = abs(sum(triangle_areas))
    return area + b // 2 + 1


def main():
    plan = get_plan("input")
    print(get_answer(plan))
    print(get_answer(plan, part_2=True))


if __name__ == "__main__":
    assert get_triangle_area(0, 0, 2, 0, 0, 1) == 1
    assert get_triangle_area(0, 0, 2, 0, 0, -1) == -1
    assert get_triangle_area(0, 0, 2, 0, 3, 0) == 0
    assert get_triangle_area(4, -5, 4, -7, 6, -7) == 2
    assert get_triangle_area(0, 0, 4, -5, 4, -7) == -4
    assert get_triangle_area(0, 0, 4, -7, 6, -7) == 7

    main()
