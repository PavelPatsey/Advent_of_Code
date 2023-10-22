import re
import time
from typing import Dict, List

INPUT = "test_input"
ROOT_NAME = "AA"
TIME_LIMIT = 15


def get_valves():
    def _split(string):
        return re.split(
            "Valve | has flow rate=|; tunnels lead to valves |; tunnel leads to valve ",
            string,
        )[1:]

    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()

    valve_attributes = list(map(_split, data))

    names = []
    flow_rates = {}
    tunnels = {}
    for name, flow_rate, tunnel in valve_attributes:
        names.append(name)
        flow_rates[name] = flow_rate
        tunnels[name] = tunnel
    return names, flow_rates, tunnels


def main():
    t0 = time.time()
    names, flow_rates, tunnels = get_valves()


    print(f"finished in {time.time() - t0:0f} sec")

    test_example = [
        "AA",
        "DD",
        "DD opened",
        "CC",
        "BB",
        "BB opened",
        "AA",
        "II",
        "JJ",
        "JJ opened",
        "II",
        "AA",
        "DD",
        "EE",
        "FF",
        "GG",
        "HH",
        "HH opened",
        "GG",
        "FF",
        "EE",
        "EE opened",
        "DD",
        "CC",
        "CC opened",  # 25
    ]
    print((test_example, 1651))


if __name__ == "__main__":
    main()
