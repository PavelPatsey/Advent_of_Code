"""
was inspired by this solution
https://gitlab.com/0xdf/aoc2022/-/blob/main/day16/day16.py
"""

import re
import time
from functools import cache

INPUT = "input"
ROOT_NAME = "AA"
TIME_LIMIT = 30
TIME_LIMIT_2 = 26


def get_valves():
    def _split(string):
        return re.split(
            "Valve | has flow rate=|; tunnels lead to valves |; tunnel leads to valve ",
            string,
        )[1:]

    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()

    valve_attributes = list(map(_split, data))

    flow_rates = {}
    neighbors = {}
    for valve, flow_rate, neighbor in valve_attributes:
        flow_rates[valve] = int(flow_rate)
        neighbors[valve] = neighbor.split(", ")
    return flow_rates, neighbors


def solve(flow_rates, neighbors, time_limit, elephant_wait=False):
    @cache
    def _solve(valve, time, opened, elephant_wait=False):
        if time == 0:
            if elephant_wait:
                return _solve(ROOT_NAME, time_limit, opened)
            return 0

        b = max(
            _solve(neighbor, time - 1, frozenset(opened), elephant_wait)
            for neighbor in neighbors[valve]
        )

        a = 0
        if flow_rates[valve] != 0 and valve not in opened:
            new_opened = set(opened)
            new_opened.add(valve)
            a = flow_rates[valve] * (time - 1) + _solve(
                valve,
                time - 1,
                frozenset(new_opened),
                elephant_wait,
            )

        return max(a, b)

    return _solve(ROOT_NAME, time_limit, frozenset(), elephant_wait)


def main():
    t0 = time.time()
    flow_rates, neighbors = get_valves()
    print("part 1:", solve(flow_rates, neighbors, TIME_LIMIT))
    print(f"finished in {time.time() - t0:0f} sec")
    print("part 2:", solve(flow_rates, neighbors, TIME_LIMIT_2, True))
    print(f"finished in {time.time() - t0:0f} sec")


if __name__ == "__main__":
    main()
