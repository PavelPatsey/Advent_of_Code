import time
from typing import Tuple
from functools import cache

INPUT = "test_input"
TIME_LIMIT = 19


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
    dct = {
        "ore_robot": 0,
        "clay_robot": 1,
        "obsidian_robot": 2,
        "geode_robot": 3,
    }
    index = dct[robot_name]
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


def get_max_obsidian(blueprint, t, robots, resources):
    max_prices = get_max_prices(blueprint)

    def _get_max_obsidian(t, robots: Tuple, resources: Tuple) -> int:
        if t == 0:
            return 0

        new_resources = tuple(
            i + j for i, j in zip(resources, get_resources_change(robots))
        )

        available_robots = get_available_robots(blueprint, resources)
        if "geode_robot" in available_robots:
            available_robots = {"geode_robot"}

        b = [
            _get_max_obsidian(
                t - 1,
                get_updated_robots(robot_name, robots),
                tuple(i - j for i, j in zip(new_resources, blueprint[robot_name])),
            )
            + (t - 1) * (1 if robot_name == "geode_robot" else 0)
            for robot_name in available_robots
        ]

        a = get_max_obsidian(blueprint, t - 1, tuple(i for i in robots), new_resources)

        return max([a] + b)

    return _get_max_obsidian(t, robots, resources)


def main():
    t0 = time.time()
    blueprints = get_blueprints()
    blueprint = blueprints[0]
    print(get_max_obsidian(blueprint, TIME_LIMIT, (1, 0, 0, 0), (0, 0, 0, 0)))
    print(f"finished in {time.time() - t0:0f} sec")


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

    main()
