INPUT = "input"


def read_input():
    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()
    points = set((tuple(map(int, line.split(","))) for line in data))
    return points


def get_total_surface_area(points):
    counter = 0
    for x, y, z in points:
        for dx, dy, dz in (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ):
            if (x + dx, y + dy, z + dz) in points:
                counter += 1

    return len(points) * 6 - counter


def main():
    points = read_input()
    print(get_total_surface_area(points))


if __name__ == "__main__":
    main()
