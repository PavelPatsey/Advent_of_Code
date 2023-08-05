INPUT = "input"


def convert(rucksacks):
    converted_rucksacks = []
    for i in range(0, len(rucksacks), 3):
        converted_rucksacks.append(
            [
                rucksacks[i],
                rucksacks[i + 1],
                rucksacks[i + 2],
            ]
        )
    return converted_rucksacks


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


def get_badge(rucksack):
    a = set(rucksack[0])
    b = set(rucksack[1])
    c = set(rucksack[2])

    a = a.intersection(b)
    a = a.intersection(c)

    return "".join(a)


def read_input():
    with open(INPUT, "r") as file:
        rucksacks = file.read().split()
    return rucksacks


def main():
    rucksacks = read_input()
    repeating_items = map(get_repeating_item, rucksacks)
    priorities_sum = sum(map(get_priority, repeating_items))
    print(priorities_sum)

    converted_rucksacks = convert(rucksacks)
    badges_sum = sum(map(get_priority, map(get_badge, converted_rucksacks)))
    print(badges_sum)


if __name__ == "__main__":
    assert get_repeating_item("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
    assert get_repeating_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert get_repeating_item("PmmdzqPrVvPwwTWBwg") == "P"

    assert get_priority("p") == 16
    assert get_priority("L") == 38
    assert get_priority("P") == 42
    assert get_priority("v") == 22
    assert get_priority("Z") == 52

    assert convert([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    assert (
        get_badge(
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ]
        )
        == "r"
    )

    main()
