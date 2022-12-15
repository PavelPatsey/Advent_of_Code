import copy

INPUT = "input"
SYMBOLS = {
    (-1, 0): "^",
    (0, 1): ">",
    (1, 0): "!",
    (0, -1): "<",
}


def read_input():
    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()
    matrix = [[y for y in x] for x in data]
    matrix = [["$"] * len(matrix[0])] + matrix + [["$"] * len(matrix[0])]
    matrix = [["$"] + line + ["$"] for line in matrix]
    return matrix


def print_matrix(matrix):
    for y in range(len(matrix)):
        print("".join(matrix[y]))


def get_traversed_matrix(matrix, x, y, acc, visited_set):
    char = matrix[y][x]
    matrix[y][x] = "#"
    visited_set.add((y,x))
    # print(x,y)
    # print_matrix(matrix)

    if matrix[y][x] == "{":
        print(acc)
        print_matrix(matrix)
        return matrix

    for (dy, dx) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_x = x + dx
        new_y = y + dy
        new_matrix = copy.deepcopy(matrix)
        new_visited_set = copy.deepcopy(visited_set)

        if not new_matrix[new_y][new_x] in ("$", "#"):
            # print(new_y,new_x)
            if ord(new_matrix[new_y][new_x]) - ord(char) <= 1:
                print(new_matrix[new_y][new_x])
                print_matrix(new_matrix)
                get_traversed_matrix(new_matrix, new_x, new_y, acc + 1, new_visited_set)


def main():
    matrix = read_input()

    E = None
    S = None
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "E":
                matrix[y][x] = "{"
                E = (y, x)
            if matrix[y][x] == "S":
                matrix[y][x] = "a"
                S = (y, x)

    # print(S)
    # print_matrix(matrix)
    traversed_matrix = get_traversed_matrix(matrix, S[1], S[0], 0, set())
    # print_matrix(traversed_matrix)


if __name__ == "__main__":
    main()
