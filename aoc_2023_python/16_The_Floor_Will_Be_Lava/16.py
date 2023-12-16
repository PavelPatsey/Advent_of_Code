from collections import deque

LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)


def get_grid(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    return data.split()


def get_directions(node, dir):
    if node == ".":
        return [dir]
    elif node == "\\":
        if dir == RIGHT:
            return [DOWN]
        elif dir == DOWN:
            return [RIGHT]
        elif dir == LEFT:
            return [UP]
        elif dir == UP:
            return [LEFT]
    elif node == "/":
        if dir == RIGHT:
            return [UP]
        elif dir == DOWN:
            return [LEFT]
        elif dir == LEFT:
            return [DOWN]
        elif dir == UP:
            return [RIGHT]
    elif node == "|":
        if dir == RIGHT:
            return [UP, DOWN]
        elif dir == DOWN:
            return [DOWN]
        elif dir == LEFT:
            return [UP, DOWN]
        elif dir == UP:
            return [UP]
    elif node == "-":
        if dir == RIGHT:
            return [RIGHT]
        elif dir == DOWN:
            return [LEFT, RIGHT]
        elif dir == LEFT:
            return [LEFT]
        elif dir == UP:
            return [LEFT, RIGHT]
    else:
        assert False


def bfs(grid):
    len_rows = len(grid)
    len_cols = len(grid[0])
    visited = set()
    queue = deque()
    queue.append(((0, 0), RIGHT))
    while queue:
        node, direction = queue.popleft()
        if (node, direction) not in visited:
            visited.add((node, direction))

        node_str = grid[node[0]][node[1]]
        new_directions = get_directions(node_str, direction)
        for new_direction in new_directions:
            r, c = node
            dr, dc = new_direction
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < len_rows and 0 <= new_c < len_cols:
                new_node = r + dr, c + dc
                if (new_node, new_direction) not in visited:
                    queue.append((new_node, new_direction))

    visited_nodes = {x[0] for x in visited}
    return len(visited_nodes)


def get_answer_1(grid):
    return bfs(grid)


def main():
    grid = get_grid("input")
    print(get_answer_1(grid))


if __name__ == "__main__":
    main()
