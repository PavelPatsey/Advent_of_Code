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
    match_list = [[seed] for seed in seeds]
    for i in range(len(seeds)):
        is_found = False
        for x in almanac["seed-to-soil"]:
            destination, source, r = x
            if seeds[i] in range(source, source + r):
                match_list[i].append(seeds[i] + destination - source)
                is_found = True
        if not is_found:
            match_list[i].append(seeds[i])

    return match_list


def main():
    seeds, almanac = get_seed_almanac()
    print(seeds)
    print(almanac)
    print(get_answer_1(seeds, almanac))


if __name__ == "__main__":
    main()
