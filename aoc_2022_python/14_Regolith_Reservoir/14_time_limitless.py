INPUT = "test_input"


def read_input():
    with open(INPUT, "r") as file:
        data = file.read().strip().split("\n")
    data = [x.split("->") for x in data]
    data = [[tuple(map(int, y.split(","))) for y in x] for x in data]
    return data


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def get_rock_set(rock_traces):
    rock_set = set()
    for rock_trace in rock_traces:
        for i in range(1, len(rock_trace)):
            dx = sign(rock_trace[i][0] - rock_trace[i - 1][0])
            dy = sign(rock_trace[i][1] - rock_trace[i - 1][1])
            x = rock_trace[i - 1][0]
            y = rock_trace[i - 1][1]
            while not (x == rock_trace[i][0] and y == rock_trace[i][1]):
                rock_set.add((x, y))
                x += dx
                y += dy
            rock_set.add((x, y))

    return rock_set


def get_sand_unit_coordinates(unit_coordinates, rock_set, sand_set):
    union_set = rock_set.union(sand_set)
    filtered = set(
        filter(
            lambda x: x[0] == unit_coordinates[0] and x[1] > unit_coordinates[1],
            union_set,
        )
    )

    if filtered == set():
        return False

    tile = min(filtered, key=lambda x: x[1])

    unit = tile[0] - 1, tile[1]
    if not unit in union_set:
        return get_sand_unit_coordinates(unit, rock_set, sand_set)

    unit = tile[0] + 1, tile[1]
    if not unit in union_set:
        return get_sand_unit_coordinates(unit, rock_set, sand_set)

    return tile[0], tile[1] - 1


def get_sand_set(rock_set):
    sand_set = set()

    is_falling_forever = False
    while not is_falling_forever:
        sand_unit_coordinates = get_sand_unit_coordinates(
            (500, 0),
            rock_set,
            sand_set,
        )
        if sand_unit_coordinates:
            sand_set.add(sand_unit_coordinates)
        else:
            is_falling_forever = True

    return sand_set


def get_sand_unit_coordinates_2(unit_coordinates, rock_set, sand_set, max_y):
    if unit_coordinates[1] == max_y - 1:
        return unit_coordinates[0], max_y - 1

    union_set = rock_set.union(sand_set)
    filtered = set(
        filter(
            lambda x: x[0] == unit_coordinates[0] and x[1] > unit_coordinates[1],
            union_set,
        )
    )

    if filtered == set():
        return unit_coordinates[0], max_y - 1

    tile = min(filtered, key=lambda x: x[1])

    if tile == (500, 0):
        return False

    unit = tile[0] - 1, tile[1]
    if not unit in union_set:
        return get_sand_unit_coordinates_2(unit, rock_set, sand_set, max_y)

    unit = tile[0] + 1, tile[1]
    if not unit in union_set:
        return get_sand_unit_coordinates_2(unit, rock_set, sand_set, max_y)

    return tile[0], tile[1] - 1


def get_sand_set_2(rock_set, max_y):
    sand_set = set()

    is_blocked = False
    while not is_blocked:
        sand_unit_coordinates = get_sand_unit_coordinates_2(
            (500, -2),
            rock_set,
            sand_set,
            max_y,
        )
        if sand_unit_coordinates:
            sand_set.add(sand_unit_coordinates)
        else:
            is_blocked = True

    return sand_set


def main():
    rock_traces = read_input()
    rock_set = get_rock_set(rock_traces)
    sand_set = get_sand_set(rock_set)
    print(len(sand_set))

    max_y = max(rock_set, key=lambda x: x[1])[1] + 2
    sand_set_2 = get_sand_set_2(rock_set, max_y)
    print(len(sand_set_2))


if __name__ == "__main__":
    unit_coordinates = (4, 0)
    rock_set = {(6, 2)}
    sand_set = {(7, 2)}
    unit_coordinates = get_sand_unit_coordinates(
        unit_coordinates,
        rock_set,
        sand_set,
    )
    assert unit_coordinates == False

    unit_coordinates = (3, 0)
    rock_set = {(3, 1), (2, 1)}
    sand_set = {(4, 1)}
    unit_coordinates = get_sand_unit_coordinates(
        unit_coordinates,
        rock_set,
        sand_set,
    )
    assert unit_coordinates == (3, 0)

    unit_coordinates = (3, 0)
    rock_set = {(3, 3), (2, 3)}
    sand_set = {}
    unit_coordinates = get_sand_unit_coordinates(
        unit_coordinates,
        rock_set,
        sand_set,
    )
    assert unit_coordinates == False

    unit_coordinates = (3, 0)
    rock_set = {(3, 3)}
    sand_set = {(4, 3)}
    unit_coordinates = get_sand_unit_coordinates(
        unit_coordinates,
        rock_set,
        sand_set,
    )
    assert unit_coordinates == False

    main()
