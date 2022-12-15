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
    matrix = [[y if y != "E" else "{" for y in x] for x in data]
    return matrix


def print_matrix(matrix):
    for y in range(len(matrix)):
        print("".join(matrix[y]))


def get_traversed_matrix(matrix, x, y, acc):
    if matrix[y][x] in ("^", "!", "<", ">"):
        return

    if matrix[y][x] == "{":
        print(acc)
        print_matrix(matrix)
        return matrix

    for (dy, dx) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_x = x + dx
        new_y = y + dy
        new_matrix = copy.deepcopy(matrix)

        if 0 <= new_y <= len(new_matrix) - 1 and 0 <= new_x <= len(new_matrix[0]) - 1:
            # print(new_y, new_x)
            # print(len(matrix))
            # print(len(matrix[0]))
            if abs(
                ord(new_matrix[new_y][new_x]) - ord(new_matrix[y][x])
            ) <= 1 and not new_matrix[new_y][new_x] in ("^", "!", "<", ">"):
                print(new_y, new_x)
                print(acc)
                print_matrix(new_matrix)
                new_matrix[y][x] = SYMBOLS[dy, dx]
                get_traversed_matrix(new_matrix, new_x, new_y, acc + 1)
                


def main():
    matrix = read_input()
    # print_matrix(matrix)

    matrix[0][0] = "a"
    traversed_matrix = get_traversed_matrix(matrix, 0, 0, 0)
    # print_matrix(traversed_matrix)


if __name__ == "__main__":
    main()
