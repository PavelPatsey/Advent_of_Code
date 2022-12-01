INPUT = "input"


def get_calories():
    with open(INPUT, "r") as file:
        calories = [x.split() for x in file.read().strip().split("\n\n")]
        calories = [[int(y) for y in x] for x in calories]
    return calories


def main():
    calories = get_calories()
    sum_calories = list(map(sum, calories))
    max_calories = max(sum_calories)

    # part_1 answer
    print(max_calories)

    sorted_sum_calories = sorted(sum_calories, reverse=True)
    # part 2 answer
    print(sum(sorted_sum_calories[:3]))


if __name__ == "__main__":
    main()
