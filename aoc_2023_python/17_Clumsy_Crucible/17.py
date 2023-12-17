import heapq

LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)


def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return [[int(y) for y in x.strip()] for x in data]


def get_new_dirs_lens_1(direction, len_dir):
    if direction in (RIGHT, LEFT):
        new_dirs_lens = [(UP, 1), (DOWN, 1)]
    elif direction in (UP, DOWN):
        new_dirs_lens = [(LEFT, 1), (RIGHT, 1)]
    else:
        assert False
    if len_dir < 3:
        new_dirs_lens.append((direction, len_dir + 1))
    return new_dirs_lens


def get_new_dirs_lens_2(direction, len_dir):
    new_dirs_lens = []
    if direction == (0, 0):
        return [(RIGHT, 1), (DOWN, 1)]
    if len_dir >= 4:
        if direction in (RIGHT, LEFT):
            new_dirs_lens.extend([(UP, 1), (DOWN, 1)])
        elif direction in (UP, DOWN):
            new_dirs_lens.extend([(LEFT, 1), (RIGHT, 1)])
        else:
            assert False
    if len_dir < 10:
        new_dirs_lens.append((direction, len_dir + 1))
    return new_dirs_lens


def get_min_heat_loss(matrix, part_2=False):
    len_rows = len(matrix)
    len_cols = len(matrix[0])
    if part_2:
        queue = [(0, 0, 0, (0, 0), 0)]
    else:
        queue = [(0, 0, 0, RIGHT, 0)]
    heapq.heapify(queue)
    state = [[{} for _ in range(len_cols)] for _ in range(len_rows)]

    while queue:
        dist, r, c, cur_dir, len_dir = heapq.heappop(queue)
        if (cur_dir, len_dir) in state[r][c]:
            continue
        state[r][c][(cur_dir, len_dir)] = dist

        if part_2:
            new_dirs_lens = get_new_dirs_lens_2(cur_dir, len_dir)
        else:
            new_dirs_lens = get_new_dirs_lens_1(cur_dir, len_dir)

        for new_dir, new_len_dir in new_dirs_lens:
            dr, dc = new_dir
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len_rows and 0 <= new_c < len_cols:
                new_dist = dist + matrix[new_r][new_c]
                heapq.heappush(queue, (new_dist, new_r, new_c, new_dir, new_len_dir))

    if part_2:
        for ((cur_dir, len_dir), dist) in state[len_rows - 1][len_cols - 1].items():
            if len_dir >= 4:
                return dist
    else:
        return min(state[len_rows - 1][len_cols - 1].values())


def get_answer(matrix, part_2=False):
    return get_min_heat_loss(matrix, part_2)


def main():
    matrix = get_matrix("input")
    print(get_answer(matrix))
    print(get_answer(matrix, True))


if __name__ == "__main__":
    main()
