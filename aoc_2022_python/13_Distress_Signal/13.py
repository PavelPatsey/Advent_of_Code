from functools import cmp_to_key

INPUT = "input"


def get_packets():
    with open(INPUT) as file:
        data = file.read().strip()
    packets_1 = [tuple(map(eval, item.split("\n"))) for item in data.split("\n\n")]
    packets_2 = [eval(x) for x in data.replace("\n\n", "\n").split("\n")]
    packets_2 += [[[2]], [[6]]]
    return packets_1, packets_2


def is_int(x):
    return isinstance(x, int)


def is_list(x):
    return isinstance(x, list)


def compare_packets(a, b) -> int:
    if is_list(a) and is_int(b):
        return compare_packets(a, [b])
    elif is_int(a) and is_list(b):
        return compare_packets([a], b)
    elif is_int(a) and is_int(b):
        return (a < b) - (a > b)
    else:
        for new_a, new_b in zip(a, b):
            res = compare_packets(new_a, new_b)
            if res == 1:
                return 1
            elif res == -1:
                return -1
        len_a, len_b = len(a), len(b)
        return (len_a < len_b) - (len_a > len_b)


def get_answer_1(packets):
    compared = map(lambda x: compare_packets(x[0], x[1]), packets)
    filtered = filter(lambda x: x[1] == 1, enumerate(compared))
    mapped = map(lambda x: x[0] + 1, filtered)
    return sum(mapped)


def get_answer_2(packets):
    sorted_packets = sorted(packets, key=cmp_to_key(compare_packets), reverse=True)
    result = 1
    for i in range(len(sorted_packets)):
        if sorted_packets[i] in ([[2]], [[6]]):
            result *= i + 1
    return result


def main():
    packets_1, packets_2 = get_packets()
    print(f"part 1: {get_answer_1(packets_1)}")
    print(f"part 2: {get_answer_2(packets_2)}")


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
    assert compare_packets([], []) == 0
    assert compare_packets(1, 1) == 0

    main()
