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
        number = []
        while j <= len_string - 1:
            if schemas[i][j].isdigit():
                number.append(j)
            else:
                if any(map(lambda x: is_adjacent_to_symbol(schemas, i, x), number)):
                    lst = [schemas[i][n] for n in number]
                    adjacent_numbers.append(int("".join(lst)))
                number = []
            j += 1
        i += 1
    return sum(adjacent_numbers)


def main():
    schemas = get_schemas()
    print(get_answer_1(schemas))


if __name__ == "__main__":
    schemas = [".....", "..1..", "....."]
    assert is_adjacent_to_symbol(schemas, 1, 2) is False

    schemas = [".....", "..1@.", "....."]
    assert is_adjacent_to_symbol(schemas, 1, 2) is True

    schemas = [".....", "..1..", ".%..."]
    assert is_adjacent_to_symbol(schemas, 1, 2) is True
    main()
