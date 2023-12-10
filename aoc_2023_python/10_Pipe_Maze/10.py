from collections import deque
from copy import deepcopy

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

DIRECTIONS = [LEFT, RIGHT, UP, DOWN]

# старое направление -> node -> новое направление
# направо -> J -> наверх
NEXT_DIR_DICT = {
    ".": [None, None, None, None],
    "J": [None, 2, None, 0],
    "L": [2, None, None, 1],
    "F": [3, None, 1, None],
    "7": [None, 3, 0, None],
    "-": [0, 1, None, None],
    "|": [None, None, 2, 3],
}


def get_nodes(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    first_last_string = ["." * (len(data[0]) + 1)]
    pipes = (
        first_last_string
        + list(map(lambda x: "." + x[:-1] + ".", data))
        + first_last_string
    )
    return pipes


def get_next_direction(i, j, nodes, prev_dir_index):
    current_node = nodes[i][j]
    assert current_node != "S"
    new_dir_index = NEXT_DIR_DICT[current_node][prev_dir_index]
    return new_dir_index


def get_cycle_len(start_i, start_j, nodes, dir_index):
    counter = 1
    di, dj = DIRECTIONS[dir_index]
    i, j = start_i + di, start_j + dj
    node = nodes[i][j]

    while node != "S":
        dir_index = get_next_direction(i, j, nodes, dir_index)
        if dir_index is None:
            return
        di, dj = DIRECTIONS[dir_index]
        i = i + di
        j = j + dj
        node = nodes[i][j]
        counter += 1

    return counter


def get_start_coordinates(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes[0])):
            if nodes[i][j] == "S":
                x, y = i, j
                break
    return x, y


def get_answer_1(nodes):
    x, y = get_start_coordinates(nodes)
    for i in range(len(DIRECTIONS)):
        length = get_cycle_len(x, y, nodes, i)
        if length is not None:
            return length // 2


def main():
    nodes = get_nodes("input")
    print(get_answer_1(nodes))


if __name__ == "__main__":
    nodes = [
        ".......",
        ".......",
        "..S-7..",
        "..|.|..",
        "..L-J..",
        ".......",
        ".......",
    ]
    assert get_answer_1(nodes) == 4

    nodes = [
        ".......",
        "...F7..",
        "..FJ|..",
        ".SJ.L7.",
        ".|F--J.",
        ".LJ....",
        ".......",
    ]
    assert get_answer_1(nodes) == 8

    nodes = [
        ".......",
        ".7-F7-.",
        "..FJ|7.",
        ".SJLL7.",
        ".|F--J.",
        ".LJ.LJ.",
        ".......",
    ]
    assert get_answer_1(nodes) == 8

    main()
