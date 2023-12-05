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
    match_list = [[seed] for seed in seeds]
    for i in range(len(seeds)):
        for almanac_value in almanac.values():
            is_found = False
            for destination, source, range_length in almanac_value:
                if match_list[i][-1] in range(source, source + range_length):
                    match_list[i].append(match_list[i][-1] + destination - source)
                    is_found = True
                    break
            if not is_found:
                match_list[i].append(match_list[i][-1])

    return min([x[-1] for x in match_list])


def main():
    seeds, almanac = get_seed_almanac()
    print(seeds)
    print(almanac)
    print(get_answer_1(seeds, almanac))


if __name__ == "__main__":
    main()
