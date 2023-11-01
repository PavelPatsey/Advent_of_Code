import re
import time
from collections import deque

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
    tunnels = {}
    for valve, flow_rate, tunnel in valve_attributes:
        valves.append(valve)
        flow_rates[valve] = int(flow_rate)
        tunnels[valve] = tunnel.split(", ")
    return valves, flow_rates, tunnels


def get_bfs_shortest_path(graph, start, goal):
    visited = []
    queue = deque((start,))

    if start == goal:
        return []

    while queue:
        path = queue.popleft()
        if isinstance(path, str):
            node = path
            path = [path]
        elif isinstance(path, list):
            node = path[-1]
        else:
            print("ERROR!")
            return
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path

            visited.append(node)

    return []


def get_distances_and_tunnels(valves, tunnels):
    distances = {}
    non_zero_tunnels = {}
    for i in valves:
        for j in valves:
            length = len(get_bfs_shortest_path(tunnels, i, j))
            if length != 0:
                distances[i, j] = length - 1
                if non_zero_tunnels.get(i) is None:
                    non_zero_tunnels[i] = [j]
                else:
                    non_zero_tunnels[i].append(j)

    return distances, non_zero_tunnels


def walk(valves, flow_rates, tunnels, distances):
    indices = dict((element, index) for index, element in enumerate(valves))
    cache = {}

    def _walk(valve, dp, t, dt, p_sum, opened_bitmask):
        if (valve, t, p_sum, opened_bitmask) in cache:
            return cache[(valve, t, p_sum, opened_bitmask)]

        a = 0
        temp_t = t + dt
        temp_p_sum = p_sum + dp * dt

        if temp_t == TIME_LIMIT:
            return p_sum

        bit = 1 << indices[valve]
        if flow_rates[valve] != 0 and not opened_bitmask & bit:
            temp_bitmask = "%s" % opened_bitmask
            temp_bitmask = int(temp_bitmask) | bit
            temp_dp = dp + flow_rates[valve]
            a = _walk(valve, temp_dp, temp_t, 1, temp_p_sum, temp_bitmask)

        b = {}
        for got_to_valve in tunnels[valve]:
            temp_dt = distances[valve, got_to_valve]
            if temp_t + temp_dt > TIME_LIMIT:
                b[got_to_valve] = _walk(
                    valve,
                    dp,
                    temp_t,
                    1,
                    temp_p_sum,
                    opened_bitmask,
                )
            else:
                b[got_to_valve] = _walk(
                    got_to_valve,
                    dp,
                    temp_t,
                    temp_dt,
                    temp_p_sum,
                    opened_bitmask,
                )
        max_value = max([a] + list(b.values()))
        cache[(valve, t, p_sum, opened_bitmask)] = max_value
        return max_value

    max_p_sum = _walk(ROOT_NAME, 0, 0, 0, 0, 0)
    return max_p_sum


def main():
    t0 = time.time()
    valves, flow_rates, tunnels = get_valves()

    non_zero_valves = list(filter(lambda x: flow_rates[x] != 0, valves))
    if ROOT_NAME not in non_zero_valves:
        non_zero_valves = [ROOT_NAME] + non_zero_valves

    distances, non_zero_tunnels = get_distances_and_tunnels(non_zero_valves, tunnels)

    print(walk(non_zero_valves, flow_rates, non_zero_tunnels, distances))
    print(f"finished in {time.time() - t0:0f} sec")


if __name__ == "__main__":
    main()
