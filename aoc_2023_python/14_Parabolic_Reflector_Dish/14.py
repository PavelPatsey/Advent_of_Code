def get_platform(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    platform = [[y for y in row.strip()] for row in data]
    return platform


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
    print(platform)
    print(get_total_load(platform))


if __name__ == "__main__":
    main()
