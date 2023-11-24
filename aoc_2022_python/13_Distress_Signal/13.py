from copy import deepcopy

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


def is_right_ordered(a, b) -> int:
    if is_list(a) and is_int(b):
        return is_right_ordered(deepcopy(a), [b])
    if is_int(a) and is_list(b):
        return is_right_ordered([a], deepcopy(b))
    if is_int(a) and is_int(b):
        if a < b:
            return 1
        elif a == b:
            return 0
        elif a > b:
            return -1
        else:
            print("error!")

    for new_a, new_b in zip(a, b):
        res = is_right_ordered(new_a, new_b)
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
    else:
        print("error_2!")


def main():
    packets = get_packets()
    lst = list(map(lambda x: is_right_ordered(*x), packets))
    print(list(enumerate(lst)))
    filtered = filter(lambda x: x[1] == 1, enumerate(lst))
    mapped = map(lambda x: x[0] + 1, filtered)
    print(sum(mapped))


if __name__ == "__main__":
    assert is_right_ordered([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == 1
    assert is_right_ordered([[1], [2, 3, 4]], [[1], 4]) == 1
    assert is_right_ordered([9], [[8, 7, 6]]) == -1
    assert is_right_ordered([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) == 1
    assert is_right_ordered([7, 7, 7, 7], [7, 7, 7]) == -1
    assert is_right_ordered([[[]]], [[]]) == -1
    assert (
        is_right_ordered(
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
        )
        == -1
    )

    main()
