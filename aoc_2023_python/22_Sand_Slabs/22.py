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
        assert dy_b1 != 0 and dy_b2 != 0
        return b1_x1 == b2_x1
    elif dy_b1 == dy_b2:
        assert dx_b1 != 0 and dx_b2 != 0
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
    sorted_bricks = sorted(input_bricks, key=lambda x: x[0][2])
    support_dict = {}

    for i, cur_brick in enumerate(sorted_bricks):
        cur_z = cur_brick[0][2]
        z_max = 0
        support_set = set()
        for j, prev_brick in enumerate(sorted_bricks[:i]):
            if is_intersect(cur_brick, prev_brick):
                prev_z = prev_brick[1][2]
                if prev_z > z_max:
                    z_max = prev_z
                    support_set = set()
                if cur_z - 1 == z_max:
                    support_set.add(j)
                dz = z_max + 1 - cur_z
                new_brick = sorted_bricks[i]
                new_brick[0][2] += dz
                new_brick[1][2] += dz
                sorted_bricks[i] = new_brick
        support_dict[i] = support_set

    print(support_dict)
    return sum(map(lambda v: len(v) - 1 if len(v) != 0 else 0, support_dict.values()))


def main():
    bricks = get_bricks("test_input")
    print(bricks)
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

    # main()
