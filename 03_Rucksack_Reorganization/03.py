INPUT = "input"


def get_priority(item):
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


def get_repeating_item(rucksack):
    N = len(rucksack)
    a = set(rucksack[: N // 2])
    b = set(rucksack[N // 2 :])
    return "".join(a.intersection(b))


def read_input():
    with open(INPUT, "r") as file:
        rucksacks = file.read().split()
    return rucksacks


def main():
    rucksacks = read_input()
    repeating_items = map(get_repeating_item, rucksacks)
    priorities_sum = sum(map(get_priority, repeating_items))
    print(priorities_sum)


if __name__ == "__main__":
    assert get_repeating_item("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
    assert get_repeating_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert get_repeating_item("PmmdzqPrVvPwwTWBwg") == "P"

    assert get_priority("p") == 16
    assert get_priority("L") == 38
    assert get_priority("P") == 42
    assert get_priority("v") == 22
    main()
