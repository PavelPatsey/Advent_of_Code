from functools import reduce

INPUT = "input"


def get_races():
    with open(INPUT, "r") as file:
        data = file.readlines()
    races = [[int(y) for y in x.split(":")[1].strip().split()] for x in data]
    races = list(zip(races[0], races[1]))
    return races


def get_race():
    with open(INPUT, "r") as file:
        data = file.readlines()
    race = [x.split(":")[1].strip().split() for x in data]
    race = [int("".join(x)) for x in race]
    return race


def get_winning_distances_number(race):
    max_time, max_distance = race
    counter = 0
    for t in range(max_time + 1):
        v = t
        distance = v * (max_time - t)
        if distance > max_distance:
            counter += 1
    return counter


def get_answer_1(races):
    farther_distances = map(get_winning_distances_number, races)
    return reduce((lambda x, y: x * y), farther_distances, 1)


def get_answer_2(race):
    return get_winning_distances_number(race)


def main():
    races = get_races()
    print(get_answer_1(races))
    race = get_race()
    print(get_answer_2(race))


if __name__ == "__main__":
    main()
