from collections import deque

INPUT = "input"

MAX_VISITED_LEN = 2500


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


def is_water(x, y, z, points):
    queue = deque()
    visited = set()

    queue.append((x, y, z))
    while queue:
        (x, y, z) = queue.popleft()
        if (x, y, z) in points or (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        if len(visited) > MAX_VISITED_LEN:
            return True
        for dx, dy, dz in (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ):
            queue.append((x + dx, y + dy, z + dz))

    return False


def get_touching_water_surface_area(points):
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
            if is_water(x + dx, y + dy, z + dz, points):
                counter += 1

    return counter


def main():
    points = read_input()
    print(get_total_surface_area(points))
    print(get_touching_water_surface_area(points))


if __name__ == "__main__":
    main()
