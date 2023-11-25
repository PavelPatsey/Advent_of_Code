INPUT = "input"


def get_packets():
    with open(INPUT) as file:
        data = file.read().strip().split("\n\n")
    packets = [tuple(map(eval, item.split("\n"))) for item in data]
    return packets


def is_int(x):
    return isinstance(x, int)


def is_list(x):
    return isinstance(x, list)


def compare_packets(a, b) -> int:
    if is_list(a) and is_int(b):
        return compare_packets(a, [b])
    if is_int(a) and is_list(b):
        return compare_packets([a], b)
    if is_int(a) and is_int(b):
        if a < b:
            return 1
        elif a == b:
            return 0
        elif a > b:
            return -1

    for new_a, new_b in zip(a, b):
        res = compare_packets(new_a, new_b)
        if res == 1:
            return 1
        elif res == -1:
            return -1

    if len(a) < len(b):
        return 1
    elif len(a) == len(b):
        return 0
    elif len(a) > len(b):
        return -1


def main():
    packets = get_packets()
    lst = list(map(lambda x: compare_packets(*x), packets))
    print(list(enumerate(lst)))
    filtered = filter(lambda x: x[1] == 1, enumerate(lst))
    mapped = map(lambda x: x[0] + 1, filtered)
    print(sum(mapped))


if __name__ == "__main__":
    assert compare_packets([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == 1
    assert compare_packets([[1], [2, 3, 4]], [[1], 4]) == 1
    assert compare_packets([9], [[8, 7, 6]]) == -1
    assert compare_packets([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) == 1
    assert compare_packets([7, 7, 7, 7], [7, 7, 7]) == -1
    assert compare_packets([], [3]) == 1
    assert compare_packets([[[]]], [[]]) == -1
    assert (
        compare_packets(
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        )
        == -1
    )

    main()
