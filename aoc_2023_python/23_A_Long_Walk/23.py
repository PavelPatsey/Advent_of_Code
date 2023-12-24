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
    end = len_rows - 1, len_cols - 2
    cur_r, cur_c = r, c
    prev_r, prev_c = -1, -1
    d_counter = 0
    d_dirs = []
    while not len(d_dirs) > 1:
        for dr, dc in DIRS[matrix[cur_r][cur_c]]:
            new_r, new_c = cur_r + dr, cur_c + dc
            if (new_r, new_c) == end:
                return (new_r, new_c), [], d_counter + 1
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
            print("d_dirs = [], vertex_configuration is None")
            assert False
    return (cur_r, cur_c), d_dirs, d_counter + 1


def get_max_steps(matrix):
    def _get_max_steps(r, c, visited, counter) -> int:
        vertex, d_dirs, d_counter = get_vertex_configuration(
            r, c, matrix, len_rows, len_cols
        )

        if vertex == end:
            return counter + d_counter

        if vertex not in visited:
            visited.add(vertex)
        else:
            print("vertex is visited")
            return 0

        r, c = vertex
        return max(
            [
                _get_max_steps(r + dr, c + dc, set(visited), counter + d_counter)
                for dr, dc in d_dirs
            ]
        )

    len_rows = len(matrix)
    len_cols = len(matrix[0])
    start = 0, 1
    end = len_rows - 1, len_cols - 2
    return _get_max_steps(0, 1, set((start,)), 0)


def main():
    matrix = get_matrix("input")
    print(get_max_steps(matrix))


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
        5,
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
        3,
    )

    matrix = [
        "#.#####################",
        "#.......#########...###",
        "#######.#########.#.###",
        "###.....#.>.>.###.#.###",
        "###v#####.#v#.###.#.###",
        "###.>...#.#.#.....#...#",
        "###v###.#.#.#########.#",
    ]
    assert get_vertex_configuration(0, 1, matrix, len(matrix), len(matrix[0])) == (
        (5, 3),
        [(1, 0), (0, 1)],
        16,
    )
    main()
