import math
import re
from functools import reduce
from itertools import combinations

MIN_COORD = 200000000000000
MAX_COORD = 400000000000000


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
        return None
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
    pairs = combinations(stones, 2)
    points_configuration = map(lambda x: get_intersection_point(x[0], x[1]), pairs)
    filtered = filter(
        lambda x: x
        and MIN_COORD <= x[0] <= MAX_COORD
        and MIN_COORD <= x[1] <= MAX_COORD,
        points_configuration,
    )
    return reduce(lambda acc, x: acc + 1, filtered, 0)


def main():
    stones = get_stones("input")
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
