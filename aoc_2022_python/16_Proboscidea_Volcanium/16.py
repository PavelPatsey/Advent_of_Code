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


def get_valves():
    def _split(string):
        return re.split(
            "Valve | has flow rate=|; tunnels lead to valves |; tunnel leads to valve ",
            string,
        )[1:]

    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()

    valve_attributes = list(map(_split, data))

    valves = []
    flow_rates = {}
    neighbors = {}
    for valve, flow_rate, tunnel in valve_attributes:
        valves.append(valve)
        flow_rates[valve] = int(flow_rate)
        neighbors[valve] = tunnel.split(", ")
    return valves, flow_rates, neighbors


def solve_1(flow_rates, neighbors):
    @cache
    def _solve_1(valve, time, opened):
        if time == 0:
            return 0

        b = max(
            _solve_1(neighbor, time - 1, frozenset(opened))
            for neighbor in neighbors[valve]
        )

        a = 0
        if flow_rates[valve] != 0 and valve not in opened:
            new_opened = set(opened)
            new_opened.add(valve)
            a = flow_rates[valve] * (time - 1) + _solve_1(
                valve, time - 1, frozenset(new_opened)
            )

        return max(a, b)

    return _solve_1(ROOT_NAME, TIME_LIMIT, frozenset())


def main():
    t0 = time.time()
    valves, flow_rates, neighbors = get_valves()
    print(solve_1(flow_rates, neighbors))
    print(f"finished in {time.time() - t0:0f} sec")


if __name__ == "__main__":
    main()
