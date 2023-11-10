import time
from functools import cache

INPUT = "test_input"
TIME_LIMIT = 5


def get_resources_change(robots):
    return (
        robots["ore_robot"],
        robots["clay_robot"],
        robots["obsidian_robot"],
        robots["geode_robot"],
    )


def get_available_robots(blueprint, resources):
    def is_available(robot_name):
        robot_price = blueprint[robot_name]
        return all(map(lambda x: x[0] <= x[1], zip(robot_price, resources)))

    return set(filter(is_available, blueprint))


# @cache
def get_max_obsidian(blueprint, t, robots, resources):
    def _get_max_obsidian(t, robots, resources):
        if t == TIME_LIMIT:
            # print(robots)
            # print(resources)
            return resources[-1]

        new_resources = tuple(
            i + j for i, j in zip(resources, get_resources_change(robots))
        )

        b = []
        for robot_name in get_available_robots(blueprint, resources):
            new_robots = robots.copy()
            new_robots[robot_name] += 1
            b.append(
                get_max_obsidian(
                    blueprint,
                    t + 1,
                    new_robots,
                    tuple(i - j for i, j in zip(new_resources, blueprint[robot_name])),
                )
            )

        a = get_max_obsidian(blueprint, t + 1, robots.copy(), new_resources)

        return max([a] + b)

    return _get_max_obsidian(t, robots, resources)


def get_blueprints():
    def get_numbers_from_string(string: str):
        return list(map(int, (filter(lambda x: x.isnumeric(), string.split()))))

    def make_blueprint(lst):
        return {
            "ore_robot": (lst[0], 0, 0, 0),
            "clay_robot": (lst[1], 0, 0, 0),
            "obsidian_robot": (lst[2], lst[3], 0, 0),
            "geode_robot": (lst[4], 0, lst[5], 0),
        }

    with open(INPUT) as file:
        data = file.readlines()

    blueprints = map(get_numbers_from_string, data)
    blueprints = list(map(make_blueprint, blueprints))
    return blueprints


def main():
    t0 = time.time()
    blueprints = get_blueprints()
    robots = {
        "ore_robot": 1,
        "clay_robot": 0,
        "obsidian_robot": 0,
        "geode_robot": 0,
    }
    blueprint = blueprints[0]
    print(get_max_obsidian(blueprint, 0, robots, (0, 0, 0, 0)))
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

    robots = {
        "ore_robot": 0,
        "clay_robot": 0,
        "obsidian_robot": 0,
        "geode_robot": 0,
    }
    assert get_resources_change(robots) == (0, 0, 0, 0)

    robots = {
        "ore_robot": 0,
        "clay_robot": 0,
        "obsidian_robot": 3,
        "geode_robot": 0,
    }
    assert get_resources_change(robots) == (0, 0, 3, 0)

    robots = {
        "ore_robot": 1,
        "clay_robot": 2,
        "obsidian_robot": 44,
        "geode_robot": 210,
    }
    assert get_resources_change(robots) == (1, 2, 44, 210)

    main()
