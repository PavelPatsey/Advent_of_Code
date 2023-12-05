import itertools

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
    for i in range(len(seeds)):
        match_list = [seeds[i]]
        for almanac_value in almanac.values():
            is_found = False
            for destination, source, range_length in almanac_value:
                if source <= match_list[-1] <= source + range_length - 1:
                    match_list.append(match_list[-1] + destination - source)
                    del match_list[0]
                    is_found = True
                    break
            if not is_found:
                match_list.append(match_list[-1])
                del match_list[0]
        if not min_location:
            min_location = match_list[-1]
        else:
            min_location = min(match_list[-1], min_location)
    return min_location


def get_ranges(seeds):
    pairs = zip(seeds[::2], seeds[1::2])
    ranges = map(lambda x: range(x[0], x[0] + x[1]), pairs)
    return ranges


def get_answer_2(seeds, almanac):
    min_location = None
    ranges = get_ranges(seeds)
    for seed in itertools.chain(*ranges):
        match_list = [seed]
        for almanac_value in almanac.values():
            is_found = False
            for destination, source, range_length in almanac_value:
                if source <= match_list[-1] <= source + range_length - 1:
                    match_list.append(match_list[-1] + destination - source)
                    del match_list[0]
                    is_found = True
                    break
            if not is_found:
                match_list.append(match_list[-1])
                del match_list[0]
        if not min_location:
            min_location = match_list[-1]
        else:
            min_location = min(match_list[-1], min_location)
    return min_location


def main():
    seeds, almanac = get_seed_almanac()
    print(seeds)
    print(almanac)
    print(get_answer_1(seeds, almanac))
    print(get_answer_2(seeds, almanac))


if __name__ == "__main__":
    main()
