def get_space(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    space = [[x for x in row.strip()] for row in data]
    return space


def print_space(space):
    for i in range(len(space)):
        print("".join(space[i]))


def get_empty_lines_indexes(space):
    empty_rows_indexes, empty_columns_indexes = [], []
    len_row = len(space)
    len_column = len(space[0])
    for r in range(len_row):
        if "#" not in space[r]:
            empty_rows_indexes.append(r)

    for c in range(len_column):
        column_is_empty = True
        for r in range(len_row):
            if space[r][c] == "#":
                column_is_empty = False
        if column_is_empty:
            empty_columns_indexes.append(c)
    return empty_rows_indexes, empty_columns_indexes


def get_answer_1(space):
    galaxies_coordinates = []
    empty_rows_indexes, empty_columns_indexes = get_empty_lines_indexes(space)
    print(empty_rows_indexes, empty_columns_indexes)


def main():
    space = get_space("test_input")
    print_space(space)
    print(get_answer_1(space))


if __name__ == "__main__":
    main()
