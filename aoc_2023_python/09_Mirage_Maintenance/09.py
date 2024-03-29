def get_history(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    history = list(map(lambda x: [int(y) for y in x.strip().split()], data))
    return history


def get_predicted_value(sequence, part):
    def _is_all_null(seq):
        return all(map(lambda x: x == 0, seq))

    sequences = [sequence]
    while not _is_all_null(sequences[-1]):
        current_seq = sequences[-1]
        next_seq = [y - x for x, y in zip(current_seq, current_seq[1:])]
        sequences.append(next_seq)

    if part == 1:
        return sum(map(lambda x: x[-1], sequences))
    else:
        return sum(map(lambda x: (-1) ** x[0] * x[1][0], enumerate(sequences)))


def get_answer_1(history):
    return sum(map(lambda x: get_predicted_value(x, part=1), history))


def get_answer_2(history):
    return sum(map(lambda x: get_predicted_value(x, part=2), history))


def main():
    history = get_history("input")
    print(get_answer_1(history))
    print(get_answer_2(history))


if __name__ == "__main__":
    assert get_predicted_value([0, 3, 6, 9, 12, 15], part=1) == 18
    assert get_predicted_value([1, 3, 6, 10, 15, 21], part=1) == 28
    assert get_predicted_value([10, 13, 16, 21, 30, 45], part=1) == 68

    assert get_predicted_value([0, 3, 6, 9, 12, 15], part=2) == -3
    assert get_predicted_value([1, 3, 6, 10, 15, 21], part=2) == 0
    assert get_predicted_value([10, 13, 16, 21, 30, 45], part=2) == 5

    main()
