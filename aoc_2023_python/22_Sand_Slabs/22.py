def get_bricks(input_file):
    def _get_parsed_line(line: str):
        return list(
            map(lambda x: [int(y) for y in x.split(",")], line.strip().split("~"))
        )

    with open(input_file, "r") as file:
        data = file.readlines()
    return [_get_parsed_line(line) for line in data]


def is_may_fall(brick, other_bricks):
    return False


def get_on_whom_lies(index, other_bricks):
    return set()


def get_dropped_brick(brick):
    start, end = brick
    xs, ys, zs = start
    xe, ye, ze = end
    assert zs <= ze
    zs = zs - 1
    ze = ze - 1
    return (xs, ys, zs), (xe, ye, ze)


def get_answer_1(input_bricks):
    sorted_bricks = sorted(input_bricks, key=lambda x: x[0][2])
    bricks = []
    supporting = {}

    for i, brick in enumerate(sorted_bricks):
        while not is_may_fall(brick, sorted_bricks[:i]):
            brick = get_dropped_brick()
        bricks.append(brick)
        for x in get_on_whom_lies(i, sorted_bricks[:i]):
            supporting[x].add(i)

    return sum(map(lambda v: v - 1, supporting.values()))


def main():
    bricks = get_bricks("test_input")
    print(bricks)
    print(get_answer_1(bricks))


if __name__ == "__main__":
    main()
