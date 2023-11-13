import time
from collections import deque
from typing import Set, Tuple

INPUT = "input"
TIME_LIMIT = 24
TIME_LIMIT_2 = 32
ROBOT_INDEXES = {
    "ore_robot": 0,
    "clay_robot": 1,
    "obsidian_robot": 2,
    "geode_robot": 3,
}


def get_blueprints():
    def _get_numbers_from_string(string: str):
        return list(map(int, (filter(lambda x: x.isnumeric(), string.split()))))

    def _make_blueprint(lst):
        return {
            "ore_robot": (lst[0], 0, 0, 0),
            "clay_robot": (lst[1], 0, 0, 0),
            "obsidian_robot": (lst[2], lst[3], 0, 0),
            "geode_robot": (lst[4], 0, lst[5], 0),
        }

    with open(INPUT) as file:
        data = file.readlines()

    blueprints = map(_get_numbers_from_string, data)
    blueprints = list(map(_make_blueprint, blueprints))
    return blueprints


def get_max_prices(blueprint):
    return tuple(map(max, zip(*blueprint.values())))


def get_updated_robots(robot_name: str, robots: Tuple) -> Tuple:
    index = ROBOT_INDEXES[robot_name]
    lst = list(robots)
    lst[index] += 1
    return tuple(lst)


def get_resources_change(robots):
    return robots


def get_available_robots(blueprint, resources):
    def _is_available(robot_name):
        robot_price = blueprint[robot_name]
        return all(map(lambda x: x[0] <= x[1], zip(robot_price, resources)))

    return set(filter(_is_available, blueprint))


def get_robots_to_build(robots: Tuple, max_prices: Tuple, available_robots: Set) -> Set:
    def _is_to_build(name):
        return (
            robots[ROBOT_INDEXES[name]] < max_prices[ROBOT_INDEXES[name]]
            or name == "geode_robot"
        )

    filtered = set(filter(_is_to_build, available_robots))
    if len(filtered) == 4:
        filtered = {"geode_robot"}

    return filtered


def get_max_geodes(time_limit, blueprint):
    max_prices = get_max_prices(blueprint)
    queue = deque()
    t, robots, resources = (
        time_limit,
        (1, 0, 0, 0),
        (0, 0, 0, 0),
    )
    queue.append((t, robots, resources))
    seen = set()
    max_geodes = 0

    while queue:
        t, robots, resources = queue.popleft()

        max_geodes = max(max_geodes, resources[3] + t * robots[3])

        if (t, robots, resources) in seen:
            continue
        seen.add((t, robots, resources))

        if t == 0:
            continue

        new_resources = tuple(
            i + j for i, j in zip(resources, get_resources_change(robots))
        )

        available_robots = get_available_robots(blueprint, resources)
        robots_to_build = get_robots_to_build(robots, max_prices, available_robots)

        for robot_name in robots_to_build:
            queue.append(
                (
                    t - 1,
                    get_updated_robots(robot_name, robots),
                    tuple(i - j for i, j in zip(new_resources, blueprint[robot_name])),
                )
            )

        if len(available_robots) == 4:
            continue
        else:
            queue.append((t - 1, robots, new_resources))

        # queue.append((t - 1, robots, new_resources))

    return max_geodes


def main():
    t0 = time.time()
    blueprints = get_blueprints()
    part_1 = 0
    for i, blueprint in enumerate(blueprints):
        ti = time.time()
        a = (i + 1) * get_max_geodes(TIME_LIMIT, blueprint)
        print(i, a)
        print(f"finished {i} blueprint in {time.time() - ti:0f} sec")
        part_1 += a
    print(f"{part_1 = }")
    print(f"part 1 finished in {time.time() - t0:0f} sec")

    t0 = time.time()
    part_2 = 1
    for i, blueprint in enumerate(blueprints[:3]):
        ti = time.time()
        a = (i + 1) * get_max_geodes(TIME_LIMIT_2, blueprint)
        print(i, a)
        print(f"finished {i} blueprint in {time.time() - ti:0f} sec")
        part_2 *= a
    print(f"{part_2 = }")
    print(f"part 2 finished in {time.time() - t0:0f} sec")


if __name__ == "__main__":
    blueprint = {
        "ore_robot": (4, 0, 0, 0),
        "clay_robot": (2, 0, 0, 0),
        "obsidian_robot": (3, 14, 0, 0),
        "geode_robot": (2, 0, 7, 0),
    }
    resources = [0, 0, 0, 0]
    assert get_available_robots(blueprint, resources) == set()

    resources = [1, 0, 0, 0]
    assert get_available_robots(blueprint, resources) == set()

    resources = [2, 0, 0, 0]
    assert get_available_robots(blueprint, resources) == {"clay_robot"}

    resources = [4, 0, 0, 0]
    assert get_available_robots(blueprint, resources) == {"clay_robot", "ore_robot"}

    resources = [3, 14, 0, 0]
    assert get_available_robots(blueprint, resources) == {
        "clay_robot",
        "obsidian_robot",
    }

    resources = [5, 14, 0, 0]
    assert get_available_robots(blueprint, resources) == {
        "clay_robot",
        "ore_robot",
        "obsidian_robot",
    }

    resources = [5, 14, 7, 0]
    assert get_available_robots(blueprint, resources) == {
        "ore_robot",
        "obsidian_robot",
        "geode_robot",
        "clay_robot",
    }

    robots = (0, 0, 0, 0)
    assert get_resources_change(robots) == (0, 0, 0, 0)

    robots = (0, 0, 3, 0)
    assert get_resources_change(robots) == (0, 0, 3, 0)

    robots = (1, 2, 44, 210)
    assert get_resources_change(robots) == (1, 2, 44, 210)

    robots = (0, 0, 0, 0)
    robot_name = "ore_robot"
    assert get_updated_robots(robot_name, robots) == (1, 0, 0, 0)

    robots = (3, 4, 5, 6)
    robot_name = "ore_robot"
    assert get_updated_robots(robot_name, robots) == (4, 4, 5, 6)

    robots = (33, 42, 51, 6)
    robot_name = "geode_robot"
    assert get_updated_robots(robot_name, robots) == (33, 42, 51, 7)

    blueprint = {
        "ore_robot": (4, 0, 0, 0),
        "clay_robot": (2, 0, 0, 0),
        "obsidian_robot": (3, 14, 0, 0),
        "geode_robot": (2, 0, 7, 0),
    }
    assert get_max_prices(blueprint) == (4, 14, 7, 0)

    blueprint = {
        "ore_robot": (46, 2, 1, 2),
        "clay_robot": (4, 17, 2, 6),
        "obsidian_robot": (10, 55, 88, 1),
        "geode_robot": (2, 0, 7, 0),
    }
    assert get_max_prices(blueprint) == (46, 55, 88, 6)

    available_robots = {
        "ore_robot",
        "obsidian_robot",
        "geode_robot",
        "clay_robot",
    }
    max_prices = (4, 2, 7, 0)
    robots = (3, 4, 5, 6)
    assert get_robots_to_build(robots, max_prices, available_robots) == {
        "ore_robot",
        "obsidian_robot",
        "geode_robot",
    }

    available_robots = {
        "ore_robot",
        "geode_robot",
    }
    max_prices = (4, 2, 7, 0)
    robots = (4, 4, 4, 4)
    assert get_robots_to_build(robots, max_prices, available_robots) == {
        "geode_robot",
    }

    available_robots = {
        "ore_robot",
        "obsidian_robot",
        "clay_robot",
    }
    max_prices = (4, 2, 7, 0)
    robots = (3, 4, 5, 6)
    assert get_robots_to_build(robots, max_prices, available_robots) == {
        "ore_robot",
        "obsidian_robot",
    }

    available_robots = {
        "ore_robot",
    }
    max_prices = (4, 2, 7, 0)
    robots = (7, 4, 5, 6)
    assert get_robots_to_build(robots, max_prices, available_robots) == set()

    available_robots = set()
    max_prices = (4, 2, 7, 0)
    robots = (7, 4, 5, 6)
    assert get_robots_to_build(robots, max_prices, available_robots) == set()

    main()
