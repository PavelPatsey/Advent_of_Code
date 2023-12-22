from copy import deepcopy


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

    dx_b1 = b1_x2 - b1_x1
    dy_b1 = b1_y2 - b1_y1
    dx_b2 = b2_x2 - b2_x1
    dy_b2 = b2_y2 - b2_y1

    if dx_b1 == dx_b2 == 0:
        return b1_x1 == b2_x1
    elif dy_b1 == dy_b2:
        return b1_y1 == b2_y1
    else:
        if dx_b1 == 0:
            assert dx_b2 != 0
            return b1_y1 <= b2_y1 <= b1_y2
        elif dy_b1 == 0:
            assert dy_b2 != 0
            return b1_x1 <= b2_x1 <= b1_x2
        else:
            assert False


def get_answer_1(input_bricks):
    bricks = sorted(input_bricks, key=lambda x: x[0][2])
    print(bricks)

    # make bricks settled
    for i, cur_brick in enumerate(bricks):
        max_z = 1
        cur_z = cur_brick[0][2]
        for j, prev_brick in enumerate(bricks[:i]):
            if is_intersect(cur_brick, prev_brick):
                prev_z = prev_brick[1][2]
                max_z = max(max_z, prev_z + 1)
        dz = max_z - cur_z
        cur_brick[0][2] = max_z
        cur_brick[1][2] += dz

    print(bricks)
    # search supporting
    k_supports_v = {i: set() for i in range(len(bricks))}
    v_supports_k = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            lower_z = lower[1][2]
            upper_z = upper[0][2]
            if is_intersect(lower, upper) and lower_z + 1 == upper_z:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)

    print(k_supports_v)
    print(v_supports_k)

    result = 0
    for i in range(len(bricks)):
        if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
            result += 1
    return result


def main():
    bricks = get_bricks("test_input")
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
