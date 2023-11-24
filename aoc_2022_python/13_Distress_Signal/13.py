from copy import deepcopy

INPUT = "test_input"


def get_packets():
    with open(INPUT) as file:
        data = file.read().strip().split("\n\n")
    packets = [tuple(map(eval, item.split("\n"))) for item in data]
    return packets


def is_int(x):
    return isinstance(x, int)


def is_list(x):
    return isinstance(x, list)


def is_right_ordered(a, b):
    if is_list(a) and is_int(b):
        return is_right_ordered(deepcopy(a), [b])
    if is_int(a) and is_list(b):
        return is_right_ordered([a], deepcopy(b))
    if is_int(a) and is_int(b):
        return a <= b
    if len(a) > len(b):
        return False
    lst = []
    z = list(zip(a, b))
    for new_a, new_b in zip(a, b):
        lst.append(is_right_ordered(new_a, new_b))
    return all(lst)


def main():
    packets = get_packets()
    print(packets)
    lst = list(map(lambda x: is_right_ordered(*x), packets))
    print(list(enumerate(lst)))


if __name__ == "__main__":
    assert is_right_ordered([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) is True
    # assert is_right_ordered([[1], [2, 3, 4]], [[1], 4]) is True
    # assert is_right_ordered([9], [[8, 7, 6]]) is False
    # assert is_right_ordered([7, 7, 7, 7], [7, 7, 7]) is False

    main()
