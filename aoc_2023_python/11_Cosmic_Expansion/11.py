from collections import deque


def get_space(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return data


def get_parsed_space(space):
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

    galaxies_coordinates = deque([])
    for r in range(len_row):
        for c in range(len_column):
            if space[r][c] == "#":
                galaxies_coordinates.append((r, c))

    return empty_rows_indexes, empty_columns_indexes, galaxies_coordinates


def get_shortest_paths(
    galaxies_coordinates,
    empty_rows_indexes,
    empty_columns_indexes,
    expansion_coeff,
):
    galaxies_coordinates_copy = galaxies_coordinates.copy()
    shortest_paths = []
    while galaxies_coordinates_copy:
        current_g_c = galaxies_coordinates_copy.popleft()
        for g_c in galaxies_coordinates_copy:
            r1, r2 = sorted((current_g_c[0], g_c[0]))
            c1, c2 = sorted((current_g_c[1], g_c[1]))
            dr = r2 - r1
            dc = c2 - c1
            for r in range(r1, r2 + 1):
                if r in empty_rows_indexes:
                    dr += expansion_coeff
            for c in range(c1, c2 + 1):
                if c in empty_columns_indexes:
                    dc += expansion_coeff
            shortest_paths.append(dr + dc)
    return shortest_paths


def get_answer(space):
    (
        empty_rows_indexes,
        empty_columns_indexes,
        galaxies_coordinates,
    ) = get_parsed_space(space)

    expansion_coeff_1 = 1
    shortest_paths_1 = get_shortest_paths(
        galaxies_coordinates,
        empty_rows_indexes,
        empty_columns_indexes,
        expansion_coeff_1,
    )

    expansion_coeff_2 = 1_000_000 - 1
    shortest_paths_2 = get_shortest_paths(
        galaxies_coordinates,
        empty_rows_indexes,
        empty_columns_indexes,
        expansion_coeff_2,
    )
    return sum(shortest_paths_1), sum(shortest_paths_2)


def main():
    space = get_space("input")
    print(get_answer(space))


if __name__ == "__main__":
    main()
