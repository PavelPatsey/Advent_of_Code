from collections import deque
from copy import deepcopy

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

TRENDS = [LEFT, RIGHT, UP, DOWN]


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


def get_next_trend(current_node: str, previous_trend):
    if current_node == ".":
        return

    right_nodes = ["-", "7", "J"]
    left_nodes = ["-", "L", "F"]
    up_nodes = ["|", "7", "F"]
    down_nodes = ["|", "L", "J"]

    D_1 = {
        RIGHT: right_nodes,
        LEFT: left_nodes,
        UP: up_nodes,
        DOWN: down_nodes,
    }

    elif current_node == "F":
    if previous_trend == UP:
        return RIGHT
    elif previous_trend == LEFT:
        return DOWN
    else:
        return


next_trend = (0, 1)
return next_trend


def get_visited(start_i, start_j, nodes, trend):
    node = nodes[start_i, start_j]
    visited = [node]

    i = start_i
    j = start_j

    while node != "S":
        di, dj = get_next_trend()
        new_i = i + di
        new_j = j + dj
        node = nodes[new_i][new_j]
        visited.append(node)

    return visited


def get_start_coordinates(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes[0])):
            if nodes[i][j] == "S":
                x, y = i, j
                break
    return x, y


def get_answer_1(nodes):
    x, y = get_start_coordinates(nodes)
    visited_lists = [get_visited(x, y, nodes, trend) for trend in TRENDS]
    return max(map(len, visited_lists))


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
