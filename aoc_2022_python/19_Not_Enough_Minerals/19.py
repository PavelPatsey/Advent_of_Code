import time
from collections import deque
from typing import List, Set, Tuple

INPUT = "input"
TIME_LIMIT = 24
TIME_LIMIT_2 = 32


def get_blueprints():
    def _get_numbers_from_string(string: str):
        return list(map(int, (filter(lambda x: x.isnumeric(), string.split()))))

    def _make_blueprint(lst: List) -> Tuple:
        return (
            (lst[0], 0, 0, 0),
            (lst[1], 0, 0, 0),
            (lst[2], lst[3], 0, 0),
            (lst[4], 0, lst[5], 0),
        )

    with open(INPUT) as file:
        data = file.readlines()

    blueprints = list(map(_get_numbers_from_string, data))
    blueprints = tuple(map(_make_blueprint, blueprints))
    return blueprints


def get_max_prices(blueprint):
    return tuple(map(max, zip(*blueprint)))


def get_updated_robots(robot_id: int, robots: Tuple) -> Tuple:
    lst = list(robots)
    lst[robot_id] += 1
    return tuple(lst)


def get_resources_change(robots):
    return robots


def get_available_robots(blueprint, resources):
    def _is_available(robot_price):
        return all(map(lambda x: x[0] <= x[1], zip(robot_price, resources)))

    mapped = map(_is_available, blueprint)
    return {i for i, blue_print in enumerate(mapped) if blue_print}


def get_robots_to_build(robots: Tuple, max_prices: Tuple, available_robots: Set) -> Set:
    def _is_to_build(robot_id):
        return robots[robot_id] < max_prices[robot_id] or robot_id == 3

    filtered = set(filter(_is_to_build, available_robots))
    filtered = {3} if 3 in filtered else filtered

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

        if (t, robots, resources) in seen:
            continue
        seen.add((t, robots, resources))

        max_geodes = max(max_geodes, resources[3] + t * robots[3])

        if t == 0:
            continue

        new_resources = tuple(
            i + j for i, j in zip(resources, get_resources_change(robots))
        )

        available_robots = get_available_robots(blueprint, resources)
        robots_to_build = get_robots_to_build(robots, max_prices, available_robots)

        for robot_id in robots_to_build:
            queue.append(
                (
                    t - 1,
                    get_updated_robots(robot_id, robots),
                    tuple(i - j for i, j in zip(new_resources, blueprint[robot_id])),
                )
            )

        if len(available_robots) == 4:
            continue
        else:
            queue.append((t - 1, robots, new_resources))

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

    # t0 = time.time()
    # part_2 = 1
    # for i, blueprint in enumerate(blueprints[:3]):
    #     ti = time.time()
    #     a = (i + 1) * get_max_geodes(TIME_LIMIT_2, blueprint)
    #     print(i, a)
    #     print(f"finished {i} blueprint in {time.time() - ti:0f} sec")
    #     part_2 *= a
    # print(f"{part_2 = }")
    # print(f"part 2 finished in {time.time() - t0:0f} sec")


if __name__ == "__main__":
    blueprint = (
        (4, 0, 0, 0),
        (2, 0, 0, 0),
        (3, 14, 0, 0),
        (2, 0, 7, 0),
    )
    resources = [0, 0, 0, 0]
    assert get_available_robots(blueprint, resources) == set()

    resources = [1, 0, 0, 0]
    assert get_available_robots(blueprint, resources) == set()

    resources = [2, 0, 0, 0]
    assert get_available_robots(blueprint, resources) == {1}

    resources = [4, 0, 0, 0]
    assert get_available_robots(blueprint, resources) == {0, 1}

    resources = [3, 14, 0, 0]
    assert get_available_robots(blueprint, resources) == {1, 2}

    resources = [5, 14, 0, 0]
    assert get_available_robots(blueprint, resources) == {0, 1, 2}

    resources = [5, 14, 7, 0]
    assert get_available_robots(blueprint, resources) == {0, 1, 2, 3}

    robots = (0, 0, 0, 0)
    assert get_resources_change(robots) == (0, 0, 0, 0)

    robots = (0, 0, 3, 0)
    assert get_resources_change(robots) == (0, 0, 3, 0)

    robots = (1, 2, 44, 210)
    assert get_resources_change(robots) == (1, 2, 44, 210)

    robots = (0, 0, 0, 0)
    robot_id = 0
    assert get_updated_robots(robot_id, robots) == (1, 0, 0, 0)

    robots = (3, 4, 5, 6)
    robot_id = 0
    assert get_updated_robots(robot_id, robots) == (4, 4, 5, 6)

    robots = (33, 42, 51, 6)
    robot_id = 3
    assert get_updated_robots(robot_id, robots) == (33, 42, 51, 7)

    blueprint = (
        (4, 0, 0, 0),
        (2, 0, 0, 0),
        (3, 14, 0, 0),
        (2, 0, 7, 0),
    )
    assert get_max_prices(blueprint) == (4, 14, 7, 0)

    blueprint = (
        (46, 2, 1, 2),
        (4, 17, 2, 6),
        (10, 55, 88, 1),
        (2, 0, 7, 0),
    )
    assert get_max_prices(blueprint) == (46, 55, 88, 6)

    available_robots = {0, 1, 2, 3}
    max_prices = (4, 2, 7, 0)
    robots = (3, 4, 5, 6)
    assert get_robots_to_build(robots, max_prices, available_robots) == {3}

    available_robots = {0, 3}
    max_prices = (4, 2, 7, 0)
    robots = (4, 4, 4, 4)
    assert get_robots_to_build(robots, max_prices, available_robots) == {3}

    available_robots = {0, 1, 2}
    max_prices = (4, 2, 7, 0)
    robots = (3, 4, 5, 6)
    assert get_robots_to_build(robots, max_prices, available_robots) == {0, 2}

    available_robots = {0}
    max_prices = (4, 2, 7, 0)
    robots = (7, 4, 5, 6)
    assert get_robots_to_build(robots, max_prices, available_robots) == set()

    available_robots = set()
    max_prices = (4, 2, 7, 0)
    robots = (7, 4, 5, 6)
    assert get_robots_to_build(robots, max_prices, available_robots) == set()

    main()
