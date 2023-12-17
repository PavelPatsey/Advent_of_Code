import heapq

LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)


def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return [[int(y) for y in x.strip()] for x in data]


def get_new_dirs_lens(direction, len_dir):
    if direction in (RIGHT, LEFT):
        new_dirs_lens = [(UP, 0), (DOWN, 0)]
    elif direction in (UP, DOWN):
        new_dirs_lens = [(LEFT, 0), (RIGHT, 0)]
    else:
        assert False
    if len_dir < 2:
        new_dirs_lens.append((direction, len_dir + 1))
    return new_dirs_lens


def get_min_heat_loss(matrix):
    len_rows = len(matrix)
    len_cols = len(matrix[0])
    queue = [(0, 0, 0, RIGHT, 0)]
    heapq.heapify(queue)
    state = [[{} for _ in range(len_cols)] for _ in range(len_rows)]

    while queue:
        dist, r, c, cur_dir, len_dir = heapq.heappop(queue)
        if (cur_dir, len_dir) in state[r][c]:
            continue
        state[r][c][(cur_dir, len_dir)] = dist

        for new_dir, new_len_dir in get_new_dirs_lens(cur_dir, len_dir):
            dr, dc = new_dir
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len_rows and 0 <= new_c < len_cols:
                new_dist = dist + matrix[new_r][new_c]
                heapq.heappush(queue, (new_dist, new_r, new_c, new_dir, new_len_dir))

    return min(state[len_rows - 1][len_cols - 1].values())


def get_answer_1(matrix):
    return get_min_heat_loss(matrix)


def main():
    matrix = get_matrix("input")
    print(get_answer_1(matrix))


if __name__ == "__main__":
    main()
