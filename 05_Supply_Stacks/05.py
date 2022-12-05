from pprint import pprint

INPUT = "test_input"


def convert_move(move):
    move = filter(lambda x: x.isdigit(), move.split())
    move = list(map(int, move))
    move[1] -= 1
    move[2] -= 1
    return move


def make_stacks(stacks):
    stacks_number = int(stacks[-1].strip().split()[-1])

    stacks_matrix = []
    for stack in stacks:
        line = []
        for i in range(stacks_number):
            line.append(stack[i * 4 + 1])
        stacks_matrix.append(line)

    transposed_matrix = [
        [stacks_matrix[j][i] for j in range(len(stacks_matrix))]
        for i in range(len(stacks_matrix[0]))
    ]

    new_stacks = [list(filter(lambda x: x != " ", x)) for x in transposed_matrix]
    new_stacks = [x[::-1] for x in new_stacks]
    return new_stacks


def read_input():
    with open(INPUT, "r") as file:
        data = file.read().split("\n\n")

        stacks = data[0].split("\n")
        stacks = make_stacks(stacks)

        moves = data[1].strip().split("\n")
        moves = tuple(map(convert_move, moves))

        return stacks, moves


def main():
    stacks, moves = read_input()


if __name__ == "__main__":
    main()
