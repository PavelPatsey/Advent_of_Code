INPUT = "input"


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
    ranges = list(
        map(
            lambda x: (
                x[0],
                x[0] + x[1],
            ),
            pairs,
        )
    )
    return ranges


def is_valid_range(range_tuple):
    return range_tuple[1] > range_tuple[0]


def get_transformed_range(range_tuple, almanac_map):
    parts = [range_tuple]
    transformed_parts = []
    for destination, source, length in almanac_map:
        new_parts = []
        start_2, end_2 = source, source + length
        while parts:
            start, end = parts.pop()
            cut_before = (start, min(end, start_2))
            if is_valid_range(cut_before):
                new_parts.append(cut_before)
            cut_intersection = (max(start, start_2), min(end, end_2))
            if is_valid_range(cut_intersection):
                dx = destination - source
                transformed_parts.append(
                    (cut_intersection[0] + dx, cut_intersection[1] + dx)
                )
            cut_after = (max(end_2, start), end)
            if is_valid_range(cut_after):
                new_parts.append(cut_after)
        parts = new_parts
    return transformed_parts + parts


def get_answer_2(seeds, almanac):
    ranges = get_ranges(seeds)
    for almanac_map in almanac.values():
        new_ranges = []
        for r in ranges:
            transformed_range = get_transformed_range(r, almanac_map)
            new_ranges.extend(transformed_range)
        ranges = new_ranges

    return min([r[0] for r in ranges])


def main():
    seeds, almanac = get_seed_almanac()
    print("pat_1:", get_answer_1(seeds, almanac))
    print("pat_2:", get_answer_2(seeds, almanac))


if __name__ == "__main__":
    range_tuple = (79, 93)
    map_list = [
        [50, 98, 2],
        [52, 50, 48],
    ]
    assert get_transformed_range(range_tuple, map_list) == [(81, 95)]

    range_tuple = (8, 20)
    map_list = [
        [0, 15, 37],
        [37, 52, 2],
        [39, 0, 15],
    ]
    assert get_transformed_range(range_tuple, map_list) == [(0, 5), (47, 54)]

    range_tuple = (81, 95)
    map_list = [
        [0, 15, 37],
        [37, 52, 2],
        [39, 0, 15],
    ]
    assert get_transformed_range(range_tuple, map_list) == [(81, 95)]

    range_tuple = (81, 95)
    map_list = [
        [49, 53, 8],
        [0, 11, 42],
        [42, 0, 7],
        [57, 7, 4],
    ]
    assert get_transformed_range(range_tuple, map_list) == [(81, 95)]

    range_tuple = (81, 95)
    map_list = [
        [88, 18, 7],
        [18, 25, 70],
    ]
    assert get_transformed_range(range_tuple, map_list) == [(74, 88)]

    range_tuple = (74, 88)
    map_list = [
        [45, 77, 23],
        [81, 45, 19],
        [68, 64, 13],
    ]
    assert get_transformed_range(range_tuple, map_list) == [(45, 56), (78, 81)]

    range_tuple = (45, 56)
    map_list = [
        [0, 69, 1],
        [1, 0, 69],
    ]
    assert get_transformed_range(range_tuple, map_list) == [(46, 57)]

    range_tuple = (46, 57)
    map_list = [
        [60, 56, 37],
        [56, 93, 4],
    ]
    assert get_transformed_range(range_tuple, map_list) == [(60, 61), (46, 56)]

    main()
