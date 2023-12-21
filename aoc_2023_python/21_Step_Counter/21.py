DIRS_LIST = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def get_map(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    elfs_map = [[x for x in line.strip()] for line in data]

    start = -1, -1
    len_rows = len(elfs_map)
    len_cols = len(elfs_map[0])
    for r in range(len_rows):
        for c in range(len_cols):
            if elfs_map[r][c] == "S":
                start = r, c
                break

    return elfs_map, start


def get_answer_1(elfs_map, start, max_steps):
    len_rows = len(elfs_map)
    len_cols = len(elfs_map[0])
    queue = set()
    queue.add(start)
    s = 0
    while s < max_steps:
        next_queue = set()
        for r, c in queue:
            for dr, dc in DIRS_LIST:
                new_r, new_c = r + dr, c + dc
                if (
                    0 <= new_r < len_rows
                    and 0 <= new_c < len_cols
                    and elfs_map[new_r][new_c] in (".", "S")
                ):
                    next_queue.add((new_r, new_c))
        queue = next_queue
        s += 1
    return len(queue)


def main():
    elfs_map, start = get_map("input")
    max_steps = 64
    print(get_answer_1(elfs_map, start, max_steps))


if __name__ == "__main__":
    main()
