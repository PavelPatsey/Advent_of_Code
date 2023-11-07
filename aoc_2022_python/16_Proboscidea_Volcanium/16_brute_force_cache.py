import re
import time

INPUT = "test_input"
ROOT_NAME = "AA"
TIME_LIMIT = 16


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


def walk(valves, flow_rates, tunnels):
    indices = dict((element, index) for index, element in enumerate(valves))
    cache = {}

    def _walk(valve, dp, t, p_sum, opened_bitmask):
        if (valve, dp, p_sum, opened_bitmask) in cache:
            return cache[(valve, dp, p_sum, opened_bitmask)]

        a = 0
        temp_p_sum = p_sum + dp
        if t == TIME_LIMIT:
            return p_sum

        bit = 1 << indices[valve]
        if flow_rates[valve] != 0 and not opened_bitmask & bit:
            temp_bitmask = "%s" % opened_bitmask
            temp_bitmask = int(temp_bitmask) | bit
            temp_dp = dp + flow_rates[valve]
            a = _walk(valve, temp_dp, t + 1, temp_p_sum, temp_bitmask)

        b = {}
        for valve in tunnels[valve]:
            b[valve] = _walk(valve, dp, t + 1, temp_p_sum, opened_bitmask)

        max_value = max([a] + list(b.values()))
        cache[(valve, dp, p_sum, opened_bitmask)] = max_value
        return max_value

    max_sum_p = _walk(ROOT_NAME, 0, 0, 0, 0)
    return max_sum_p


def main():
    t0 = time.time()
    valves, flow_rates, tunnels = get_valves()
    print(valves)
    print(flow_rates)
    print(tunnels)
    max_sum_p = walk(valves, flow_rates, tunnels)
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
