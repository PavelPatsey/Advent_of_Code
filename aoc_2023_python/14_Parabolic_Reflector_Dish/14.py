import time
from copy import deepcopy


def get_platform(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    platform = [[y for y in row.strip()] for row in data]
    return platform


def get_rotated(matrix):
    list_of_tuples = zip(*matrix[::-1])
    return [list(elem) for elem in list_of_tuples]


def get_rolled(matrix):
    platform = deepcopy(matrix)
    len_rows = len(platform)
    len_cols = len(platform[0])
    for c in range(len_cols):
        for _ in range(len_rows):
            for r in range(len_rows):
                if platform[r][c] == "O" and r > 0 and platform[r - 1][c] == ".":
                    platform[r][c] = "."
                    platform[r - 1][c] = "O"
    return platform


def get_load(platform):
    len_rows = len(platform)
    len_cols = len(platform[0])
    total_load = 0
    for c in range(len_cols):
        for r in range(len_rows):
            if platform[r][c] == "O":
                total_load += len_rows - r

    return total_load


def get_answer_1(platform):
    return get_load(get_rolled(platform))


def get_answer_2(platform):
    cache_dict = {}
    max_t = 10**9
    t = 0
    while t < max_t:
        t += 1
        for j in range(4):
            platform = get_rolled(platform)
            platform = get_rotated(platform)
        platform_tuple = tuple(tuple(row) for row in platform)
        h = hash(platform_tuple)
        if h in cache_dict:
            idx_cycle_start = cache_dict[h]
            cycle_length = t - idx_cycle_start
            cycle_count = (max_t - t) // cycle_length
            t += cycle_count * cycle_length
        cache_dict[h] = t
    return get_load(platform)


def main():
    platform = get_platform("input")
    print(get_answer_1(platform))

    t0 = time.time()
    print(get_answer_2(platform))
    print(f"finished part 2 in {time.time() - t0:0f} sec")


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
