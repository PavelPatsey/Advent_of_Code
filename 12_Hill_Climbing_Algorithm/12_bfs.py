from collections import deque

INPUT = "input"


def read_input():
    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()
    matrix = [[char for char in row] for row in data]
    matrix = [["$"] * len(matrix[0])] + matrix + [["$"] * len(matrix[0])]
    matrix = [["$"] + line + ["$"] for line in matrix]
    return matrix


def print_matrix(matrix):
    for r in range(len(matrix)):
        print("".join(matrix[r]))


def get_heights(letters):
    R = len(letters)
    C = len(letters[0])

    heights = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if letters[r][c] == "$":
                pass
            elif letters[r][c] == "S":
                heights[r][c] = 1
            elif letters[r][c] == "E":
                heights[r][c] = 26
            else:
                heights[r][c] = ord(letters[r][c]) - ord("a") + 1

    return heights


def get_bfs_steps(letters, heights, part):
    visited = set()
    queue = deque()

    R = len(letters)
    C = len(letters[0])
    for r in range(R):
        for c in range(C):
            if (part == 1 and letters[r][c] == "S") or (
                part == 2 and heights[r][c] == 1
            ):
                queue.append(((r, c), 0))

    while queue:
        (r, c), d = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if letters[r][c] == "E":
            return d
        for dc, dr in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            rr = r + dr
            cc = c + dc
            if letters[rr][cc] != "$" and heights[rr][cc] <= heights[r][c] + 1:
                queue.append(((rr, cc), d + 1))


def main():
    letters = read_input()
    heights = get_heights(letters)

    print(get_bfs_steps(letters, heights, part=1))
    print(get_bfs_steps(letters, heights, part=2))


if __name__ == "__main__":
    main()
