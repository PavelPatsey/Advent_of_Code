DIRS = {
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}


def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return [line.strip() for line in data]


def get_max_steps(matrix):
    def _get_max_steps(r, c, visited) -> int:
        visited.add((r, c))

        # print((r, c))
        if (r, c) == end:
            print("visit end", len(visited) - 1)
            return len(visited) - 1
        lst = []
        dir_key = matrix[r][c]
        for dr, dc in DIRS[dir_key]:
            new_r, new_c = r + dr, c + dc
            if (
                0 <= new_r < len_rows
                and 0 <= new_c < len_cols
                and matrix[new_r][new_c] != "#"
                and (new_r, new_c) not in visited
            ):
                lst.append(_get_max_steps(new_r, new_c, set(visited)))

        if not lst:
            return 0

        return max(lst)

    len_rows = len(matrix)
    len_cols = len(matrix[0])
    end = len_rows - 1, len_cols - 2
    return _get_max_steps(0, 1, set())


def main():
    matrix = get_matrix("test_input")
    print(matrix)
    print(get_max_steps(matrix))


if __name__ == "__main__":
    main()
