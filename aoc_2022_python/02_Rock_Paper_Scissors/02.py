INPUT = "input"

MOVE_INDEX = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

MOVE_PRICE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

COMPARISON_MATRIX = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3],
]

RESULT_PRICE = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

INDEX_MOVE = {
    0: "X",
    1: "Y",
    2: "Z",
}


def get_round_result_2(moves):
    elf_move, my_move = moves

    my_result_price = RESULT_PRICE[my_move]
    index = COMPARISON_MATRIX[MOVE_INDEX[elf_move]].index(my_result_price)
    my_move_price = MOVE_PRICE[INDEX_MOVE[index]]

    return my_result_price + my_move_price


def get_round_result(moves):
    elf_move, my_move = moves
    return (
        COMPARISON_MATRIX[MOVE_INDEX[elf_move]][MOVE_INDEX[my_move]]
        + MOVE_PRICE[my_move]
    )


def read_input():
    with open(INPUT, "r") as file:
        moves = [tuple(x.split()) for x in file.read().strip().split("\n")]
    return moves


def main():
    moves = read_input()
    print(sum(map(get_round_result, moves)))
    print(sum(map(get_round_result_2, moves)))


if __name__ == "__main__":
    assert get_round_result(("A", "X")) == 4
    assert get_round_result(("A", "Y")) == 8
    assert get_round_result(("A", "Z")) == 3
    assert get_round_result(("B", "X")) == 1
    assert get_round_result(("C", "Z")) == 6

    assert get_round_result_2(("A", "Y")) == 4
    assert get_round_result_2(("B", "X")) == 1
    assert get_round_result_2(("C", "Z")) == 7
    main()
