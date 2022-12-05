import copy

INPUT = "input"


def get_message(stacks):
    return "".join(x[-1] for x in stacks)


def make_procedure(stacks, moves):
    new_stacks = copy.deepcopy(stacks)
    for move in moves:
        new_stacks = do_move(new_stacks, move)
    return new_stacks


def make_procedure_2(stacks, moves):
    new_stacks = copy.deepcopy(stacks)
    for move in moves:
        new_stacks = do_move_2(new_stacks, move)
    return new_stacks


def do_move(stacks, move):
    new_stacks = copy.deepcopy(stacks)
    items_number = move[0]
    from_stack = move[1]
    to_stack = move[2]

    for _ in range(items_number):
        new_stacks[to_stack].append(new_stacks[from_stack].pop())

    return new_stacks


def do_move_2(stacks, move):
    new_stacks = copy.deepcopy(stacks)
    items_number = move[0]
    from_stack = move[1]
    to_stack = move[2]

    lst = [new_stacks[from_stack].pop() for _ in range(items_number)]
    lst.reverse()
    new_stacks[to_stack].extend(lst)

    return new_stacks


def convert_move(move):
    move = filter(lambda x: x.isdigit(), move.split())
    move = list(map(int, move))
    move[1] -= 1
    move[2] -= 1
    return tuple(move)


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
    print(get_message(make_procedure(stacks, moves)))
    print(get_message(make_procedure_2(stacks, moves)))


if __name__ == "__main__":
    stacks_0 = [
        ["1", "Z", "N"],
        ["2", "M", "C", "D"],
        ["3", "P"],
    ]
    move = (1, 1, 0)
    stacks_1 = [
        ["1", "Z", "N", "D"],
        ["2", "M", "C"],
        ["3", "P"],
    ]
    assert do_move(stacks_0, move) == stacks_1

    stacks_1 = [
        ["1"],
        ["2", "M", "C", "D", "Z", "N"],
        ["3", "P"],
    ]
    move = (2, 0, 1)
    assert do_move_2(stacks_0, move) == stacks_1

    main()
