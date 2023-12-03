INPUT = "input"


def get_schemas():
    with open(INPUT, "r") as file:
        data = file.readlines()
    first_last_string = ["." * (len(data[0]) + 1)]
    schemas = (
        first_last_string
        + list(map(lambda x: "." + x[:-1] + ".", data))
        + first_last_string
    )
    return schemas


def get_adjacent_coordinates(i, j):
    return [(i + x, j + y) for y in [-1, 0, 1] for x in [-1, 0, 1] if (x, y) != (0, 0)]


def is_adjacent_to_symbol(schemas, i, j):
    indexes = get_adjacent_coordinates(i, j)
    adjacent_items = [schemas[x][y] for x, y in indexes]
    return any(map(lambda x: not x.isdigit() and x != ".", adjacent_items))


def get_answer_1(schemas):
    adjacent_numbers = []
    len_string = len(schemas[0])
    i = 1
    while i <= len(schemas) - 2:
        j = 1
        number_indexes = []
        while j <= len_string - 1:
            if schemas[i][j].isdigit():
                number_indexes.append(j)
            elif number_indexes:
                if any(
                    map(lambda x: is_adjacent_to_symbol(schemas, i, x), number_indexes)
                ):
                    number_int = int("".join([schemas[i][n] for n in number_indexes]))
                    adjacent_numbers.append(number_int)
                number_indexes = []
            j += 1
        i += 1
    return sum(adjacent_numbers)


def get_answer_2(schemas):
    gear_dict = dict()
    len_string = len(schemas[0])
    i = 1
    while i <= len(schemas) - 2:
        j = 1
        number_indexes = []
        while j <= len_string - 1:
            if schemas[i][j].isdigit():
                number_indexes.append(j)
            elif number_indexes:
                coordinates = []
                for n in number_indexes:
                    coordinates += get_adjacent_coordinates(i, n)
                gears_coordinates = [
                    (x, y) for x, y in set(coordinates) if schemas[x][y] == "*"
                ]
                if gears_coordinates:
                    number_int = int("".join([schemas[i][n] for n in number_indexes]))
                    for coordinate in gears_coordinates:
                        if coordinate in gear_dict.keys():
                            gear_dict[coordinate].append(number_int)
                        else:
                            gear_dict[coordinate] = [number_int]
                number_indexes = []
            j += 1
        i += 1

    return sum([value[0] * value[1] for value in gear_dict.values() if len(value) == 2])


def main():
    schemas = get_schemas()
    print(get_answer_1(schemas))
    print(get_answer_2(schemas))


if __name__ == "__main__":
    schemas = [
        ".....",
        "..1..",
        ".....",
    ]
    assert is_adjacent_to_symbol(schemas, 1, 2) is False

    schemas = [
        ".....",
        "..1@.",
        ".....",
    ]
    assert is_adjacent_to_symbol(schemas, 1, 2) is True

    schemas = [
        ".....",
        "..1..",
        ".%...",
    ]
    assert is_adjacent_to_symbol(schemas, 1, 2) is True

    main()
