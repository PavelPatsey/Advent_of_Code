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
    matrix = [[char for char in row] for row in data]
    matrix = [["$"] * len(matrix[0])] + matrix + [["$"] * len(matrix[0])]
    matrix = [["$"] + line + ["$"] for line in matrix]
    return matrix


def print_matrix(matrix):
    for r in range(len(matrix)):
        print("".join(matrix[r]))


def traverse_matrix(matrix, r, c, acc):
    print(r, c)
    print_matrix(matrix)

    if matrix[r][c] in ("$", "#"):
        return

    if matrix[r][c] == "{":
        print(f"{acc=}")
        print_matrix(matrix)
        return

    char = matrix[r][c]
    matrix[r][c] = "#"

    for (dr, dc) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        if ord(matrix[r + dr][c + dc]) <= 1 + ord(char):
            traverse_matrix(copy.deepcopy(matrix), r + dr, c + dc, acc + 1)


def main():
    matrix = read_input()

    E = None
    S = None
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "E":
                matrix[r][c] = "{"
                E = (r, c)
            if matrix[r][c] == "S":
                matrix[r][c] = "a"
                S = (r, c)

    # print(S)
    # print_matrix(matrix)
    traverse_matrix(matrix, S[0], S[1], 0)


if __name__ == "__main__":
    main()
