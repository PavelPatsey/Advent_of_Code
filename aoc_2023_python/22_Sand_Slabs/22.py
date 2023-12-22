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
    (x11, y11, _), (x21, y21, _) = brick_1
    (x12, y12, _), (x22, y22, _) = brick_2
    return True


def get_answer_1(input_bricks):
    sorted_bricks = sorted(input_bricks, key=lambda x: x[0][2])
    supporting = {}

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
        supporting[i] = support_set

    return sum(map(lambda v: v - 1, supporting.values()))


def main():
    bricks = get_bricks("test_input")
    print(bricks)
    print(get_answer_1(bricks))


if __name__ == "__main__":
    main()
