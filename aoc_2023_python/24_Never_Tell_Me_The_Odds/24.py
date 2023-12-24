import math
import re
from itertools import combinations

MIN_COORD = 7
MAX_COORD = 27


def get_stones(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[int(x) for x in re.split(r",|@", line)] for line in data]


def get_intersection_point(stone_1, stone_2):
    """
    y = k1 * x + c1
    y = k2 * x + c2
    x0 = (c2 - c1) / (k1 - k2)
    y0 = k1 * x0 + c1
    """
    x1, y1, _, dx1, dy1, _ = stone_1
    x2, y2, _, dx2, dy2, _ = stone_2
    k1 = dy1 / dx1
    k2 = dy2 / dx2

    if k1 == k2:
        return
    c1 = y1 - k1 * x1
    c2 = y2 - k2 * x2

    x0 = (c2 - c1) / (k1 - k2)
    y0 = k1 * x0 + c1

    crossed_in_future = all(
        (
            (x0 - x1) / dx1 > 0,
            (x0 - x2) / dx2 > 0,
            (y0 - y1) / dy1 > 0,
            (y0 - y2) / dy2 > 0,
        )
    )

    if not crossed_in_future:
        return crossed_in_future
    return x0, y0


def get_answer_1(stones):
    pairs = list(combinations(stones, 2))
    print(pairs)
    points = list(map(lambda x: get_intersection_point(x[0], x[1]), pairs))
    print(points)
    filtered = list(filter(lambda x: x, points))
    print(filtered)
    filtered_2 = list(
        filter(
            lambda x: MIN_COORD <= x[0] <= MAX_COORD and MIN_COORD <= x[1] <= MAX_COORD,
            filtered,
        )
    )
    print(filtered_2)
    return len(filtered_2)


def main():
    stones = get_stones("test_input")
    print(stones)
    print(get_answer_1(stones))


if __name__ == "__main__":
    stone_1 = [19, 13, 30, -2, 1, -2]
    stone_2 = [18, 19, 22, -1, -1, -2]
    x0, y0 = 14.33333333, 15.33333333
    x1, y1 = get_intersection_point(stone_1, stone_2)
    assert math.isclose(x0, x1) is True
    assert math.isclose(y0, y1) is True

    stone_1 = [19, 13, 30, -2, 1, -2]
    stone_2 = [20, 25, 34, -2, -2, -4]
    x0, y0 = 11.666666666667, 16.666666666667
    x1, y1 = get_intersection_point(stone_1, stone_2)
    assert math.isclose(x0, x1) is True
    assert math.isclose(y0, y1) is True

    stone_1 = [19, 13, 30, -2, 1, -2]
    stone_2 = [20, 19, 15, 1, -5, -3]
    assert get_intersection_point(stone_1, stone_2) is False

    stone_1 = [18, 19, 22, -1, -1, -2]
    stone_2 = [20, 25, 34, -2, -2, -4]
    assert get_intersection_point(stone_1, stone_2) is None

    main()
