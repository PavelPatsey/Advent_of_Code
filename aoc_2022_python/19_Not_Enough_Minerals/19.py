INPUT = "test_input"


def get_blueprints():
    def get_numbers_from_string(string: str):
        return list(filter(lambda x: x.isnumeric(), string.split()))

    def make_blueprint(lst):
        ore_robot = (lst[0], 0, 0)
        clay_robot = (lst[1], 0, 0)
        obsidian_robot = (lst[2], lst[3], 0)
        geode_robot = (lst[4], 0, lst[5])
        return ore_robot, clay_robot, obsidian_robot, geode_robot

    with open(INPUT) as file:
        data = file.readlines()

    blueprints = map(get_numbers_from_string, data)
    blueprints = list(map(make_blueprint, blueprints))
    return blueprints


def main():
    blueprints = get_blueprints()
    print(blueprints)


if __name__ == "__main__":
    main()
