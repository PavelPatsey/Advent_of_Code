DIRS = {
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}


def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def get_vertex_configuration(r, c, matrix, len_rows, len_cols):
    cur_r, cur_c = r, c
    prev_r, prev_c = -1, -1
    d_counter = 0
    d_dirs = []
    while not len(d_dirs) > 1:
        for dr, dc in DIRS[matrix[cur_r][cur_c]]:
            new_r, new_c = cur_r + dr, cur_c + dc
            if (
                0 <= new_r < len_rows
                and 0 <= new_c < len_cols
                and matrix[new_r][new_c] != "#"
                and (new_r, new_c) != (prev_r, prev_c)
            ):
                d_dirs.append((dr, dc))
        if len(d_dirs) == 1:
            prev_r, prev_c = cur_r, cur_c
            dr, dc = d_dirs[0]
            cur_r, cur_c = prev_r + dr, prev_c + dc
            d_counter += 1
            d_dirs = []
        elif len(d_dirs) > 1:
            continue
        else:
            assert False
    return (cur_r, cur_c), d_dirs, d_counter


def get_max_steps(matrix):
    def _get_max_steps(r, c, visited, counter) -> int:
        # start
        print(r, c, "start")
        if (r, c) == end:
            print("visit end", len(visited))
            print((r, c, visited, counter))
            return counter

        next_vertex, d_dirs, d_counter = get_vertex_configuration(
            r, c, matrix, len_rows, len_cols
        )
        print(next_vertex, d_dirs, d_counter)
        exit(0)

        visited.add(next_vertex)
        r, c = next_vertex

        lst = []
        for dr, dc in d_dirs:
            lst.append(_get_max_steps(r + dr, c + dc, set(visited), counter))

        if not lst:
            return 0

        return max(lst)

    len_rows = len(matrix)
    len_cols = len(matrix[0])
    start = 0, 1
    end = len_rows - 1, len_cols - 2
    return _get_max_steps(0, 1, set((start,)), 0)


def main():
    matrix = get_matrix("test_input")
    print(f"{matrix=}")
    # print(get_max_steps(matrix))


if __name__ == "__main__":
    matrix = [
        "#.####",
        "#.#.##",
        "#....#",
        "###.##",
        "######",
    ]
    assert get_vertex_configuration(0, 1, matrix, len(matrix), len(matrix[0])) == (
        (2, 3),
        [(-1, 0), (1, 0), (0, 1)],
        4,
    )

    matrix = [
        "#.####",
        "#.#.##",
        "#....#",
        "#.#.##",
        "#.####",
    ]
    assert get_vertex_configuration(0, 1, matrix, len(matrix), len(matrix[0])) == (
        (2, 1),
        [(1, 0), (0, 1)],
        2,
    )
    # main()
