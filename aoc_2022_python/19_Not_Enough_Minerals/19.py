INPUT = "test_input"
TIME_LIMIT = 24


def get_resources_change(robots):
    return 0


def get_available_robots(blueprint, resources):
    def is_available(robot_name):
        robot_price = blueprint[robot_name]
        return all(map(lambda x: x[0] <= x[1], zip(robot_price, resources)))

    return set(filter(is_available, blueprint))


def get_max_obsidian(blueprint, t, robots, resources):
    new_t = t + 1
    if new_t == TIME_LIMIT:
        print(resources)
        return resources["geode"]
    new_resources = get_resources_change(robots)
    b = []
    for robot in get_available_robots(blueprint, resources):
        new_robots = dict(robots)
        b.append(get_max_obsidian(blueprint, new_t, new_robots, new_resources))

    a = get_max_obsidian(blueprint, new_t, dict(robots), new_resources)

    return max([a] + b)


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
    blueprints = get_blueprints()
    print(blueprints)
    resources = {
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0,
    }
    blueprint = blueprints[0]
    print()


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

    main()
