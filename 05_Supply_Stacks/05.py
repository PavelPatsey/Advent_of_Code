from pprint import pprint

INPUT = "test_input"


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

        stacks = data[0]
        stacks = stacks.split("\n")
        stacks = make_stacks(stacks)
        print(stacks)

        moves = data[1]
        print(moves)


def main():
    read_input()


if __name__ == "__main__":
    main()
