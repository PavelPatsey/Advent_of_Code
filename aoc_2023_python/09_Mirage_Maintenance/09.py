def get_history(inp):
    with open(inp, "r") as file:
        data = file.readlines()
    history = list(map(lambda x: [int(y) for y in x.strip().split()], data))
    return history


def get_predicted_value(sequence):
    """
    0   3   6   9  12  15  18
      3   3   3   3   3   3
        0   0   0   0   0
    """

    def _is_all_null(seq):
        return all(map(lambda x: x == 0, seq))

    sequences = [sequence]
    while not _is_all_null(sequences[-1]):
        previous_seq = sequences[-1]
        new_seq = [y - x for x, y in zip(previous_seq, previous_seq[1:])]
        sequences.append(new_seq)

    return sum(map(lambda x: x[-1], sequences))


def get_answer_1(history):
    return sum(map(get_predicted_value, history))


def main():
    history = get_history("test_input")
    print(history)
    print(get_answer_1(history))


if __name__ == "__main__":
    assert get_predicted_value([0, 3, 6, 9, 12, 15]) == 18
    assert get_predicted_value([1, 3, 6, 10, 15, 21]) == 28
    assert get_predicted_value([10, 13, 16, 21, 30, 45]) == 68
    main()
