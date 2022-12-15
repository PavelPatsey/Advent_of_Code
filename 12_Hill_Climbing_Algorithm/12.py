import copy

# B = copy.deepcopy(A)

INPUT = "test_input"
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
    return matrix


def print_matrix(matrix):
    for y in range(len(matrix)):
        print("".join(matrix[y]))


def get_traversed_matrix(matrix, x, y, acc):
    # if matrix[y][x] in ("^", "!", "<", ">"):
    #     return

    if matrix[y][x] == "E":
        print(acc)
        return matrix

    for (dy, dx) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_x = x + dx
        new_y = y + dy
        new_matrix = copy.deepcopy(matrix)
        
        if 0 <= new_y <= len(matrix) -1 and 0 <= new_x <= len(matrix[0]) -1 :
            # print(new_y, new_x)  
            # print(len(matrix))
            # print(len(matrix[0]))
            if new_matrix[new_y][new_x] == "E":
                print(acc)
                print(new_y, new_x)  
                print_matrix(new_matrix)
                return new_matrix
            if abs(ord(new_matrix[new_y][new_x]) - ord(new_matrix[y][x])) <= 1:
                # print(new_y, new_x)  
                # print_matrix(new_matrix)
                new_matrix[y][x] = SYMBOLS[dy, dx]
                return get_traversed_matrix(new_matrix, new_x, new_y, acc + 1)




def main():
    matrix = read_input()

    matrix[0][0] = "a"
    traversed_matrix = get_traversed_matrix(matrix, 0, 0, 0)
    # print_matrix(traversed_matrix)


if __name__ == "__main__":
    main()
