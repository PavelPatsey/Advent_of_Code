def get_bricks(input_file):
    def _get_parsed_line(line: str):
        return list(
            map(lambda x: [int(y) for y in x.split(",")], line.strip().split("~"))
        )

    def _check_bricks(bricks):
        for brick in bricks:
            z1, z2 = brick[0][2], brick[1][2]
            assert z1 <= z2

    with open(input_file, "r") as file:
        data = file.readlines()

    bricks = [_get_parsed_line(line) for line in data]
    _check_bricks(bricks)
    return bricks


def is_intersect(brick_1, brick_2):
    (b1_x1, b1_y1, _), (b1_x2, b1_y2, _) = brick_1
    (b2_x1, b2_y1, _), (b2_x2, b2_y2, _) = brick_2

    return max(b1_x1, b2_x1) <= min(b1_x2, b2_x2) and max(b1_y1, b2_y1) <= min(
        b1_y2, b2_y2
    )


def get_answer_1(input_bricks):
    def _make_bricks_settled():
        for i, cur_brick in enumerate(bricks):
            max_z = 1
            cur_z = cur_brick[0][2]
            for prev_brick in bricks[:i]:
                if is_intersect(cur_brick, prev_brick):
                    prev_z = prev_brick[1][2]
                    max_z = max(max_z, prev_z + 1)
            dz = max_z - cur_z
            cur_brick[0][2] = max_z
            cur_brick[1][2] += dz

    def _get_supporting_dicts():
        lower_supports_upper = {i: set() for i in range(len(bricks))}
        upper_lies_on_lower = {i: set() for i in range(len(bricks))}

        for j, upper in enumerate(bricks):
            for i, lower in enumerate(bricks[:j]):
                lower_z = lower[1][2]
                upper_z = upper[0][2]
                if is_intersect(lower, upper) and lower_z + 1 == upper_z:
                    lower_supports_upper[i].add(j)
                    upper_lies_on_lower[j].add(i)
        return lower_supports_upper, upper_lies_on_lower

    bricks = sorted(input_bricks, key=lambda x: x[0][2])
    _make_bricks_settled()
    lower_supports_upper, upper_lies_on_lower = _get_supporting_dicts()

    result = 0
    for i in range(len(bricks)):
        if all(len(upper_lies_on_lower[j]) >= 2 for j in lower_supports_upper[i]):
            result += 1
    return result


def main():
    bricks = get_bricks("input")
    print(get_answer_1(bricks))


if __name__ == "__main__":
    brick_1, brick_2 = ([[0, 0, 0], [0, 3, 0]], [[2, 0, 0], [2, 3, 0]])
    assert is_intersect(brick_1, brick_2) is False

    brick_1, brick_2 = ([[0, 0, 0], [0, 3, 0]], [[0, 1, 0], [0, 10, 0]])
    assert is_intersect(brick_1, brick_2) is True

    brick_1, brick_2 = ([[0, 0, 0], [3, 0, 0]], [[-1, 2, 0], [5, 2, 0]])
    assert is_intersect(brick_1, brick_2) is False

    brick_1, brick_2 = ([[0, 2, 0], [3, 2, 0]], [[-1, 2, 0], [5, 2, 0]])
    assert is_intersect(brick_1, brick_2) is True

    brick_1, brick_2 = ([[0, -1, 0], [0, 2, 0]], [[-1, 0, 0], [5, 0, 0]])
    assert is_intersect(brick_1, brick_2) is True

    brick_1, brick_2 = ([[0, -1, 0], [0, 2, 0]], [[-1, -10, 0], [5, -10, 0]])
    assert is_intersect(brick_1, brick_2) is False

    brick_1, brick_2 = ([[-1, 0, 0], [5, 0, 0]], [[0, -10, 0], [0, 10, 0]])
    assert is_intersect(brick_1, brick_2) is True

    brick_1, brick_2 = ([[-1, 0, 0], [5, 0, 0]], [[-5, -10, 0], [-5, 10, 0]])
    assert is_intersect(brick_1, brick_2) is False

    brick_1, brick_2 = ([[-1, 0, 0], [5, 0, 0]], [[-1, 0, 0], [-1, 10, 0]])
    assert is_intersect(brick_1, brick_2) is True

    brick_1, brick_2 = ([[1, 1, 8], [1, 1, 9]], [[1, 0, 1], [1, 2, 1]])
    assert is_intersect(brick_1, brick_2) is True

    brick_1, brick_2 = ([[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]])
    assert is_intersect(brick_1, brick_2) is True

    brick_1, brick_2 = ([[1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2]])
    assert is_intersect(brick_1, brick_2) is False

    main()
