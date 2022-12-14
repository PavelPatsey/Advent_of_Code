from collections import defaultdict

INPUT = "input"


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


def get_rock_dict(rock_set):
    rock_dict = defaultdict(set)
    for rock in rock_set:
        rock_dict[rock[0]].add(rock)
    return rock_dict


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


def get_sand_unit_coordinates(unit_coordinates, rock_dict, sand_dict):
    union_set = rock_dict[unit_coordinates[0]].union(sand_dict[unit_coordinates[0]])
    filtered = set(
        filter(
            lambda x: x[1] > unit_coordinates[1],
            union_set,
        )
    )

    if filtered == set():
        return False

    tile = min(filtered, key=lambda x: x[1])

    unit = tile[0] - 1, tile[1]
    if not unit in rock_dict[unit[0]] and not unit in sand_dict[unit[0]]:
        return get_sand_unit_coordinates(unit, rock_dict, sand_dict)

    unit = tile[0] + 1, tile[1]
    if not unit in rock_dict[unit[0]] and not unit in sand_dict[unit[0]]:
        return get_sand_unit_coordinates(unit, rock_dict, sand_dict)

    return tile[0], tile[1] - 1


def get_sand_dict(rock_dict):
    sand_dict = defaultdict(set)

    is_falling_forever = False
    while not is_falling_forever:
        sand_unit_coordinates = get_sand_unit_coordinates(
            (500, 0),
            rock_dict,
            sand_dict,
        )
        if sand_unit_coordinates:
            sand_dict[sand_unit_coordinates[0]].add(sand_unit_coordinates)
        else:
            is_falling_forever = True

    return sand_dict


def get_sand_unit_coordinates_2(unit_coordinates, rock_dict, sand_dict, max_y):
    if unit_coordinates[1] == max_y - 1:
        return unit_coordinates[0], max_y - 1

    union_set = rock_dict[unit_coordinates[0]].union(sand_dict[unit_coordinates[0]])
    filtered = set(
        filter(
            lambda x: x[1] > unit_coordinates[1],
            union_set,
        )
    )

    if filtered == set():
        return unit_coordinates[0], max_y - 1

    tile = min(filtered, key=lambda x: x[1])

    if tile == (500, 0):
        return False

    unit = tile[0] - 1, tile[1]
    if not unit in rock_dict[unit[0]] and not unit in sand_dict[unit[0]]:
        return get_sand_unit_coordinates_2(unit, rock_dict, sand_dict, max_y)

    unit = tile[0] + 1, tile[1]
    if not unit in rock_dict[unit[0]] and not unit in sand_dict[unit[0]]:
        return get_sand_unit_coordinates_2(unit, rock_dict, sand_dict, max_y)

    return tile[0], tile[1] - 1


def get_sand_dict_2(rock_dict, max_y):
    sand_dict = defaultdict(set)

    is_blocked = False
    while not is_blocked:
        sand_unit_coordinates = get_sand_unit_coordinates_2(
            (500, -2), rock_dict, sand_dict, max_y
        )
        if sand_unit_coordinates:
            sand_dict[sand_unit_coordinates[0]].add(sand_unit_coordinates)
        else:
            is_blocked = True

    return sand_dict


def main():
    rock_traces = read_input()
    rock_set = get_rock_set(rock_traces)
    rock_dict = get_rock_dict(rock_set)
    sand_dict = get_sand_dict(rock_dict)
    print(sum(map(len, sand_dict.values())))

    max_y = max(rock_set, key=lambda x: x[1])[1] + 2
    sand_dict = get_sand_dict_2(rock_dict, max_y)
    print(sum(map(len, sand_dict.values())))


if __name__ == "__main__":
    main()
