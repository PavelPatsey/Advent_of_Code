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


def get_farther_distances(race):
    time, max_distance = race
    farther_distances = []
    for t in range(time + 1):
        v = t
        distance = v * (time - t)
        if distance > max_distance:
            farther_distances.append(distance)
    return farther_distances


def get_answer_1(races):
    farther_distances = map(get_farther_distances, races)
    lens = map(len, farther_distances)
    return reduce((lambda x, y: x * y), lens, 1)


def get_answer_2(race):
    return len(get_farther_distances(race))


def main():
    races = get_races()
    print(get_answer_1(races))
    race = get_race()
    print(get_answer_2(race))


if __name__ == "__main__":
    main()
