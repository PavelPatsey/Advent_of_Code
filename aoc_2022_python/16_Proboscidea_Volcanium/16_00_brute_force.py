import re
import time

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

    valves = []
    flow_rates = {}
    tunnels = {}
    for valve, flow_rate, tunnel in valve_attributes:
        valves.append(valve)
        flow_rates[valve] = int(flow_rate)
        tunnels[valve] = tunnel.split(", ")
    return valves, flow_rates, tunnels


def main():
    def walk(valve, dp, t, p_sum, opened):
        a = 0
        temp_p_sum = p_sum + dp
        if t == TIME_LIMIT:
            return p_sum

        if flow_rates[valve] != 0 and valve not in opened:
            temp_set = opened.copy()
            temp_set.add(valve)
            temp_dp = dp + flow_rates[valve]
            a = walk(valve, temp_dp, t + 1, temp_p_sum, temp_set)

        b = {}
        for valve in tunnels[valve]:
            b[valve] = walk(valve, dp, t + 1, temp_p_sum, opened)
        return max([a] + list(b.values()))

    t0 = time.time()
    valves, flow_rates, tunnels = get_valves()
    print(valves)
    print(flow_rates)
    print(tunnels)
    max_sum_p = walk(ROOT_NAME, 0, 0, 0, set())
    print(max_sum_p)

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
