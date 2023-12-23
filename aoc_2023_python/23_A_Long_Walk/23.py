def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return [line.strip() for line in data]


def get_max_steps(matrix):
    def _get_max_steps(r, c, visited) -> int:
        return 1

    len_rows = len(matrix)
    len_cols = len(matrix[0])
    start = 0, 1
    end = len_rows - 1, len_cols - 2
    return _get_max_steps(0, 1, set())


def main():
    matrix = get_matrix("test_input")
    print(matrix)
    print(get_max_steps(matrix))


if __name__ == "__main__":
    main()
