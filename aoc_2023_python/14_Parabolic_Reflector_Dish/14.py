def get_platform(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    platform = [[y for y in row.strip()] for row in data]
    return platform


def get_total_load(platform):
    len_rows = len(platform)
    len_cols = len(platform[0])
    load_matrix = []
    for c in range(len_cols):
        load_column = []
        current_load = len_rows
        for r in range(len_rows):
            if platform[r][c] == "O":
                load_column.append(current_load)
                current_load -= 1
            elif platform[r][c] == "#":
                current_load = len_rows - r - 1
        load_matrix.append(load_column)
    return sum(map(sum, load_matrix))


def main():
    platform = get_platform("test_input")
    print(platform)
    print(get_total_load(platform))


if __name__ == "__main__":
    main()
