from typing import Set

INDEXES = ((1, 0), (0, 1), (-1, 0), (0, -1))

PIPES_DICT = {
    "F": ("-", "|"),
    "7": 2,
    "7": 2,
    "|": 3,
    "J": 4,
    "-": ("-", "|"),
    "L": 6,
}


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


def get_updated_set(a: Set, b: Set) -> Set:
    new_a = a.copy()
    new_a.update(b)
    return new_a


def can_visit(nodes, i, j, di, dj):
    current_node = nodes[i][j]
    next_node = nodes[i + di][j + dj]
    if next_node == ".":
        return False
    if current_node == "S":
        return True
    if current_node == "F":
        return (
            di == 0
            and dj == 1
            and next_node == "-"
            or di == 1
            and dj == 0
            and next_node == "|"
        )
    elif current_node == "7":
        return (
            di == 0
            and dj == -1
            and next_node == "-"
            or di == 1
            and dj == 0
            and next_node == "|"
        )
    elif current_node == "J":
        return (
            di == 0
            and dj == -1
            and next_node == "-"
            or di == -1
            and dj == 0
            and next_node == "|"
        )
    elif current_node == "L":
        return (
            di == 0
            and dj == 1
            and next_node == "-"
            or di == -1
            and dj == 0
            and next_node == "|"
        )
    elif current_node == "-":
        return (
            di == 0
            and dj == 1
            and next_node in ("7", "J")
            or di == 0
            and dj == -1
            and next_node in ("F", "L")
        )
    elif current_node == "|":
        return (
            di == 1
            and dj == 0
            and next_node in ("L", "J")
            or di == -1
            and dj == 0
            and next_node in ("F", "7")
        )
    else:
        assert False


def get_max_steps_counter(start_i, start_j, nodes):
    counter = 0
    visited = [(start_i, start_j)]
    queue = [(start_i, start_j)]

    while queue:
        i, j = queue.pop()
        condition = True
        for di, dj in INDEXES:
            # if condition is True:
            #     counter += 1
            #     condition = False
            new_i, new_j = i + di, j + dj
            if (i + di, j + dj) not in visited and can_visit(nodes, i, j, di, dj):
                visited.append((new_i, new_j))
                queue.append((new_i, new_j))

    return counter


def get_s_coordinates(nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes[0])):
            if nodes[i][j] == "S":
                x, y = i, j
                break
    return x, y


def get_answer_1(nodes):
    x, y = get_s_coordinates(nodes)
    print(x, y)
    return get_max_steps_counter(x, y, nodes)


def main():
    pipes = get_pipes("test_input")
    print(get_answer_1(pipes))


if __name__ == "__main__":
    main()
