import re

INPUT = "input"


def read_input():
    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()
    sensor_set = set()
    beacon_set = set()
    for line in data:
        numbers = re.split(r"\D", line)
        numbers = list(map(int, filter(lambda x: x != "", numbers)))
        s_x = numbers[0]
        s_y = numbers[1]
        b_x = numbers[2]
        b_y = numbers[3]
        d = abs(s_x - b_x) + abs(s_y - b_y)
        sensor_set.add((s_x, s_y, d))
        beacon_set.add((b_x, b_y))

    return sensor_set, beacon_set


def is_cannot_possibly_exist(x, y, sensor_set, beacon_set):
    if (x, y) in beacon_set:
        return False
    else:
        for (s_x, s_y, d) in sensor_set:
            d_x_y = abs(s_x - x) + abs(s_y - y)
            if d_x_y <= d:
                return True
        return False


def main():
    sensor_set, beacon_set = read_input()

    if INPUT == "test_input":
        y = 10
        min_x = -100
        max_x = 100
    else:
        y = 2_000_000
        min_x = -int(1e7)
        max_x = int(1e7)

    counter = 0
    for x in range(min_x, max_x):
        y = y
        if is_cannot_possibly_exist(x, y, sensor_set, beacon_set):
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
