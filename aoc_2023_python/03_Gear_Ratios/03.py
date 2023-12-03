INPUT = "test_input"


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


def is_adjacent_to_symbol(schemas, i, j):
    lst = [
        schemas[i + 1][j],
        schemas[i + 1][j + 1],
        schemas[i][j + 1],
        schemas[i - 1][j + 1],
        schemas[i - 1][j],
        schemas[i - 1][j - 1],
        schemas[i][j - 1],
        schemas[i + 1][j - 1],
    ]
    return any(map(lambda x: not x.isdigit() and x != ".", lst))


def get_answer_1(schemas):
    adjacent_numbers = []
    len_string = len(schemas[0])
    i = 1
    while i <= len(schemas) - 2:
        j = 0
        number_indexes = []
        while j <= len_string - 1:
            if schemas[i][j].isdigit():
                number_indexes.append(j)
            else:
                if any(
                    map(lambda x: is_adjacent_to_symbol(schemas, i, x), number_indexes)
                ):
                    lst = [schemas[i][n] for n in number_indexes]
                    adjacent_numbers.append(int("".join(lst)))
                number_indexes = []
            j += 1
        i += 1
    return sum(adjacent_numbers)


def get_adjacent_gears_coordinates(schemas, i, j):
    indexes = [(0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    return [(i + di, j + dj) for di, dj in indexes if schemas[i + di][j + dj] == "*"]


def get_answer_2(schemas):
    gear_dict = dict()
    len_string = len(schemas[0])
    i = 1
    while i <= len(schemas) - 2:
        j = 0
        number_indexes = []
        while j <= len_string - 1:
            if schemas[i][j].isdigit():
                number_indexes.append(j)
            else:
                gears_coordinates = []
                for n in number_indexes:
                    coordinates = get_adjacent_gears_coordinates(schemas, i, n)
                    for coordinate in coordinates:
                        if coordinate not in gears_coordinates:
                            gears_coordinates.append(coordinate)
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

    result_list = []
    result = 0
    from pprint import pprint

    pprint(len(gear_dict))
    for value in gear_dict.values():
        if len(value) == 2:
            result = result + value[0] * value[1]
            result_list.append(value[0] * value[1])
    print(sorted(result_list))
    return result


def main():
    schemas = get_schemas()
    print(get_answer_1(schemas))
    print(get_answer_2(schemas))


if __name__ == "__main__":
    schemas = [".....", "..1..", "....."]
    assert is_adjacent_to_symbol(schemas, 1, 2) is False

    schemas = [".....", "..1@.", "....."]
    assert is_adjacent_to_symbol(schemas, 1, 2) is True

    schemas = [".....", "..1..", ".%..."]
    assert is_adjacent_to_symbol(schemas, 1, 2) is True

    schemas = [
        ".....",
        "..1..",
        ".*...",
    ]
    assert get_adjacent_gears_coordinates(schemas, 1, 2) == [(2, 1)]

    schemas = [
        ".....",
        "..1..",
        ".@...",
    ]
    assert get_adjacent_gears_coordinates(schemas, 1, 2) == []

    main()
