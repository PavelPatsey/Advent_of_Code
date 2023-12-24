import time

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


def get_vertex_configuration(r, c, matrix, len_rows, len_cols, visited_points):
    end = len_rows - 1, len_cols - 2
    cur_r, cur_c = r, c
    prev_r, prev_c = -1, -1
    d_counter = 0
    d_dirs = []
    d_visited_points = set()
    while not len(d_dirs) > 1:
        for dr, dc in DIRS[matrix[cur_r][cur_c]]:
            new_r, new_c = cur_r + dr, cur_c + dc
            if (new_r, new_c) == end:
                d_visited_points.add((new_r, new_c))
                return (new_r, new_c), [], d_counter + 1, d_visited_points
            if (
                0 <= new_r < len_rows
                and 0 <= new_c < len_cols
                and matrix[new_r][new_c] != "#"
                and (new_r, new_c) != (prev_r, prev_c)
                and (new_r, new_c) not in visited_points
            ):
                d_dirs.append((dr, dc))
        if len(d_dirs) == 1:
            prev_r, prev_c = cur_r, cur_c
            dr, dc = d_dirs[0]
            cur_r, cur_c = prev_r + dr, prev_c + dc
            d_visited_points.add((cur_r, cur_c))
            d_counter += 1
            d_dirs = []
        elif len(d_dirs) > 1:
            continue
        else:
            # print("d_dirs = [], vertex_configuration is None", f"{d_visited_points=}")
            return None
    d_visited_points.add((cur_r, cur_c))
    return (cur_r, cur_c), d_dirs, d_counter + 1, d_visited_points


v = 0


def get_max_steps(matrix):
    def _get_max_steps(r, c, visited_vertexes, visited_points, counter) -> int:
        if (r, c) not in visited_points:
            visited_points.add((r, c))

        vertex_configuration = get_vertex_configuration(
            r, c, matrix, len_rows, len_cols, visited_points
        )

        if vertex_configuration is None:
            return 0
        vertex, d_dirs, d_counter, d_visited_points = vertex_configuration

        if vertex == end:
            return counter + d_counter

        visited_points.update(d_visited_points)

        if vertex not in visited_vertexes:
            visited_vertexes.add(vertex)
        else:
            global v
            v = v + 1
            print(f"vertex is visited {v} times")
            return 0

        r, c = vertex
        return max(
            [
                _get_max_steps(
                    r + dr,
                    c + dc,
                    set(visited_vertexes),
                    set(visited_points),
                    counter + d_counter,
                )
                for dr, dc in d_dirs
            ]
        )

    len_rows = len(matrix)
    len_cols = len(matrix[0])
    start = 0, 1
    end = len_rows - 1, len_cols - 2
    return _get_max_steps(0, 1, set((start,)), set(), 0)


def main():
    matrix = get_matrix("input")
    t0 = time.time()
    print(get_max_steps(matrix))
    print(f"finished in {time.time() - t0:0f} sec")


if __name__ == "__main__":
    matrix = [
        "#.####",
        "#.#.##",
        "#....#",
        "###.##",
        "######",
    ]
    assert get_vertex_configuration(
        0, 1, matrix, len(matrix), len(matrix[0]), set()
    ) == (
        (2, 3),
        [(-1, 0), (1, 0), (0, 1)],
        5,
        {(1, 1), (2, 1), (2, 2), (2, 3)},
    )

    matrix = [
        "#.####",
        "#.#.##",
        "#....#",
        "#.#.##",
        "#.####",
    ]
    assert get_vertex_configuration(
        0, 1, matrix, len(matrix), len(matrix[0]), set()
    ) == (
        (2, 1),
        [(1, 0), (0, 1)],
        3,
        {(1, 1), (2, 1)},
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
    assert get_vertex_configuration(
        0, 1, matrix, len(matrix), len(matrix[0]), set()
    ) == (
        (5, 3),
        [(1, 0), (0, 1)],
        16,
        {
            (1, 2),
            (3, 4),
            (2, 7),
            (1, 5),
            (4, 3),
            (3, 7),
            (1, 1),
            (1, 4),
            (1, 7),
            (3, 3),
            (3, 6),
            (5, 3),
            (1, 6),
            (1, 3),
            (3, 5),
        },
    )

    main()
