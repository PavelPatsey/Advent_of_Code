def get_platform(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    platform = [[y for y in row.strip()] for row in data]
    return platform


def get_rotated(matrix):
    list_of_tuples = zip(*matrix[::-1])
    return [list(elem) for elem in list_of_tuples]


def get_total_load(platform):
    len_rows = len(platform)
    len_cols = len(platform[0])
    total_load = 0
    for c in range(len_cols):
        current_load = len_rows
        for r in range(len_rows):
            if platform[r][c] == "O":
                total_load += current_load
                current_load -= 1
            elif platform[r][c] == "#":
                current_load = len_rows - r - 1
    return total_load


def main():
    platform = get_platform("test_input")
    print(get_total_load(platform))


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    assert get_rotated(matrix) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    main()
