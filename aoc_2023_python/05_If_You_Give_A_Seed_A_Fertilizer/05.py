from typing import List, Tuple

INPUT = "test_input"


def get_seed_almanac():
    with open(INPUT, "r") as file:
        data = file.read()
    lst = data.strip().split("\n\n")
    seeds, almanac = lst[0], lst[1:]
    seeds = [int(x) for x in seeds.split(":")[1].strip().split(" ")]
    almanac_dict = {}
    for x in almanac:
        key, lst = x.strip().split(" map:\n")
        value = [[int(y) for y in x.strip().split()] for x in lst.split("\n")]
        almanac_dict[key] = value
    return seeds, almanac_dict


def get_answer_1(seeds, almanac):
    min_location = None
    for seed in seeds:
        match = seed
        for almanac_value in almanac.values():
            for destination, source, range_length in almanac_value:
                if source <= match <= source + range_length - 1:
                    match = match + destination - source
                    break
        if not min_location:
            min_location = match
        else:
            min_location = min(match, min_location)
    return min_location


def get_ranges(seeds):
    pairs = zip(seeds[::2], seeds[1::2])
    ranges = map(
        lambda x: (
            x[0],
            x[0] + x[1],
        ),
        pairs,
    )
    return ranges


def get_range_intersection(tuple_1, tuple_2):
    a1, b1 = tuple_1
    a2, b2 = tuple_2

    if a1 <= a2:
        if b1 <= a2:
            return
        else:
            return a2, min(b1, b2)
    else:
        if b2 <= a1:
            return
        else:
            return a1, min(b1, b2)


def get_non_range_intersections(tuple_1, tuple_2):
    a1, b1 = tuple_1
    a2, b2 = tuple_2

    if a1 == a2:
        if b1 == b2:
            return [(a1, b1)]
        else:
            return [(b2, b1)]
    else:
        if b1 == b2:
            return [(a1, a2)]
        else:
            return [(a1, a2), (b2, b1)]


def get_mapped_ranges(range_tuple: Tuple, map_list: List) -> List[Tuple]:
    mapped_ranges = []
    for destination, source, length in map_list:
        range_intersection = get_range_intersection(
            range_tuple, (source, source + length)
        )
        if range_intersection:
            dx = destination - source
            new_start = range_intersection[0] + dx
            new_end = range_intersection[1] + dx
            mapped_ranges.append(
                (
                    new_start,
                    new_end,
                )
            )
    if not mapped_ranges:
        result = [range_tuple]
    else:
        result = mapped_ranges

    if range_intersection:
        non_range_intersections = get_non_range_intersections(
            range_tuple, get_range_intersection
        )

    return result


def get_min_location(range_tuple, almanac):
    """
    range_tuple = (79, 93)
    map_list = [[50, 98, 2], [52, 50, 48]]
    assert get_mapped_ranges(range_tuple, map_list) == [(81, 95)]

    range_tuple = (8, 20)
    map_list = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]
    assert get_mapped_ranges(range_tuple, map_list) == [(0, 5), (47, 54)]
    :param range_tuple:
    :param almanac:
    :return:
    """
    range_list = [range_tuple]
    for almanac_value in almanac.values():
        new_range_list = []
        while range_list:
            now_range = range_list.pop()
            mapped_ranges = get_mapped_ranges(now_range, almanac_value)
            new_range_list.extend(mapped_ranges)
        range_list = [x for x in new_range_list]

    r = range_list
    lst = [x[0] for x in range_list]
    min_location = min(lst)
    return min_location


def get_answer_2(seeds, almanac):
    min_location = None
    ranges = get_ranges(seeds)
    for range_tuple in ranges:
        if not min_location:
            min_location = get_min_location(range_tuple, almanac)
        min_location = min(get_min_location(range_tuple, almanac), min_location)
    return min_location


def main():
    seeds, almanac = get_seed_almanac()
    print(seeds)
    print(almanac)
    print(get_answer_1(seeds, almanac))
    print(get_answer_2(seeds, almanac))


if __name__ == "__main__":
    assert get_range_intersection((1, 4), (6, 7)) == None
    assert get_range_intersection((1, 4), (4, 5)) == None
    assert get_range_intersection((1, 4), (3, 5)) == (3, 4)
    assert get_range_intersection((1, 5), (2, 3)) == (2, 3)
    assert get_range_intersection((2, 6), (1, 5)) == (2, 5)
    assert get_range_intersection((2, 6), (6, 7)) == None
    assert get_range_intersection((2, 4), (6, 7)) == None

    assert get_non_range_intersections((1, 7), (1, 3)) == [(3, 7)]
    assert get_non_range_intersections((1, 7), (3, 4)) == [(1, 3), (4, 7)]
    assert get_non_range_intersections((1, 7), (4, 7)) == [(1, 4)]
    assert get_non_range_intersections((1, 7), (1, 7)) == [(1, 7)]

    # range_tuple = (79, 93)
    # map_list = [
    #     [50, 98, 2],
    #     [52, 50, 48],
    # ]
    # assert get_mapped_ranges(range_tuple, map_list) == [(81, 95)]
    #
    # range_tuple = (8, 20)
    # map_list = [
    #     [0, 15, 37],
    #     [37, 52, 2],
    #     [39, 0, 15],
    # ]
    # assert get_mapped_ranges(range_tuple, map_list) == [(0, 5), (47, 54)]
    #
    # range_tuple = (81, 95)
    # map_list = [
    #     [0, 15, 37],
    #     [37, 52, 2],
    #     [39, 0, 15],
    # ]
    # assert get_mapped_ranges(range_tuple, map_list) == [(81, 95)]
    #
    # range_tuple = (81, 95)
    # map_list = [
    #     [49, 53, 8],
    #     [0, 11, 42],
    #     [42, 0, 7],
    #     [57, 7, 4],
    # ]
    # assert get_mapped_ranges(range_tuple, map_list) == [(81, 95)]
    #
    # range_tuple = (81, 95)
    # map_list = [
    #     [88, 18, 7],
    #     [18, 25, 70],
    # ]
    # assert get_mapped_ranges(range_tuple, map_list) == [(74, 88)]
    #
    # range_tuple = (74, 88)
    # map_list = [
    #     [45, 77, 23],
    #     [81, 45, 19],
    #     [68, 64, 13],
    # ]
    # assert get_mapped_ranges(range_tuple, map_list) == [(45, 56), (78, 81)]
    #
    # range_tuple = (45, 56)
    # map_list = [
    #     [0, 69, 1],
    #     [1, 0, 69],
    # ]
    # assert get_mapped_ranges(range_tuple, map_list) == [(46, 57)]

    range_tuple = (46, 57)
    map_list = [
        [60, 56, 37],
        [56, 93, 4],
    ]
    print(get_mapped_ranges(range_tuple, map_list))
    assert get_mapped_ranges(range_tuple, map_list) == [(45, 56), (60, 61)]

    main()
