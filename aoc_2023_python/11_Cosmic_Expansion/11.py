from collections import deque


def get_space(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    space = [[x for x in row.strip()] for row in data]
    return space


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


def get_galaxies_coordinates(space):
    galaxies_coordinates = []
    len_row = len(space)
    len_column = len(space[0])
    for r in range(len_row):
        for c in range(len_column):
            if space[r][c] == "#":
                galaxies_coordinates.append((r, c))
    return galaxies_coordinates


def get_shortest_paths(
    galaxies_coordinates,
    empty_rows_indexes,
    empty_columns_indexes,
    d_expansion,
):
    shortest_paths = []
    while galaxies_coordinates:
        current_g_c = galaxies_coordinates.popleft()
        for g_c in galaxies_coordinates:
            r1, r2 = sorted((current_g_c[0], g_c[0]))
            c1, c2 = sorted((current_g_c[1], g_c[1]))
            dr = r2 - r1
            dc = c2 - c1
            for r in range(r1, r2 + 1):
                if r in empty_rows_indexes:
                    dr += d_expansion
            for c in range(c1, c2 + 1):
                if c in empty_columns_indexes:
                    dc += d_expansion
            shortest_paths.append(dr + dc)
    return shortest_paths


def get_answer_1(space):
    galaxies_coordinates = deque(get_galaxies_coordinates(space))
    empty_rows_indexes, empty_columns_indexes = get_empty_lines_indexes(space)
    d_expansion = 1
    shortest_paths = get_shortest_paths(
        galaxies_coordinates,
        empty_rows_indexes,
        empty_columns_indexes,
        d_expansion,
    )
    return sum(shortest_paths)


def get_answer_2(space):
    d_expansion = 1_000_000 - 1
    galaxies_coordinates = deque(get_galaxies_coordinates(space))
    empty_rows_indexes, empty_columns_indexes = get_empty_lines_indexes(space)
    shortest_paths = shortest_paths = get_shortest_paths(
        galaxies_coordinates,
        empty_rows_indexes,
        empty_columns_indexes,
        d_expansion,
    )
    return sum(shortest_paths)


def main():
    space = get_space("input")
    print(get_answer_1(space))
    print(get_answer_2(space))


if __name__ == "__main__":
    main()
