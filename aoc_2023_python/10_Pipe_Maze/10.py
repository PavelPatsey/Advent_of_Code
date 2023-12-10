from collections import deque
from copy import deepcopy

INDEXES = ((1, 0), (0, 1), (-1, 0), (0, -1))


def get_pipes(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    first_last_string = ["." * (len(data[0]) + 1)]
    pipes = (
        first_last_string
        + list(map(lambda x: "." + x[:-1] + ".", data))
        + first_last_string
    )
    return pipes


def can_visit(nodes, i, j, di, dj):
    right = (0, 1)
    left = (0, -1)
    up = (-1, 0)
    down = (1, 0)

    right_nodes = ["-", "7", "J"]
    left_nodes = ["-", "L", "F"]
    up_nodes = ["|", "7", "F"]
    down_nodes = ["|", "L", "J"]

    trend = di, dj
    current_node = nodes[i][j]
    next_node = nodes[i + di][j + dj]

    if next_node == ".":
        return False
    elif current_node == "S":
        return True
    elif current_node == "F":
        return (
            trend == right
            and next_node in right_nodes
            or trend == down
            and next_node in down_nodes,
        )
    elif current_node == "7":
        return (
            trend == left
            and next_node in left_nodes
            or trend == down
            and next_node in down_nodes
        )
    elif current_node == "J":
        return (
            trend == left
            and next_node in left_nodes
            or trend == up
            and next_node in up_nodes
        )
    elif current_node == "L":
        return (
            trend == right
            and next_node in right_nodes
            or trend == up
            and next_node in up_nodes
        )
    elif current_node == "-":
        return (
            trend == right
            and next_node in right_nodes
            or trend == left
            and next_node in left_nodes
        )
    elif current_node == "|":
        return (
            trend == up
            and next_node in up_nodes
            or trend == down
            and next_node in down_nodes
        )
    else:
        assert False


def get_max_steps_counter(start_i, start_j, nodes):
    max_counter = 0
    visited = [(start_i, start_j)]
    queue = deque(((start_i, start_j, 0),))
    test_list = deepcopy(nodes)

    while queue:
        i, j, counter = queue.popleft()
        for di, dj in INDEXES:
            new_i, new_j, new_counter = i + di, j + dj, counter + 1
            if can_visit(nodes, i, j, di, dj) and (new_i, new_j) not in visited:
                visited.append((new_i, new_j))
                queue.append((new_i, new_j, new_counter))
                max_counter = max(max_counter, new_counter)
                test_list[new_i] = (
                    test_list[new_i][:new_j]
                    + str(new_counter)
                    + test_list[new_i][new_j + 1 :]
                )

    for line in test_list:
        print(line)
    return max_counter


def get_s_coordinates(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes[0])):
            if nodes[i][j] == "S":
                x, y = i, j
                break
    return x, y


def get_answer_1(nodes):
    x, y = get_s_coordinates(nodes)
    return get_max_steps_counter(x, y, nodes)


def main():
    assert get_answer_1(get_pipes("test_input")) == 4
    assert get_answer_1(get_pipes("test_input_2")) == 8
    # print(get_answer_1(get_pipes("input")))


if __name__ == "__main__":
    main()
