import re
import time
from collections import deque

INPUT = "test_input"
ROOT_NAME = "AA"
TIME_LIMIT = 10


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


def get_distances(valves, flow_rates, tunnels):
    valve_list = list(filter(lambda x: flow_rates[x] != 0, valves))
    if ROOT_NAME not in valve_list:
        valve_list = [ROOT_NAME] + valve_list
    distances = {}
    for i in valve_list:
        for j in valve_list:
            length = len(get_bfs_shortest_path(tunnels, i, j))
            distances[i, j] = length - 1 if length != 0 else 0
    return distances


def walk(flow_rates, tunnels):
    def _walk(valve, dp, t, p_sum, opened):
        a = 0
        temp_p_sum = p_sum + dp
        if t == TIME_LIMIT:
            return p_sum

        if flow_rates[valve] != 0 and valve not in opened:
            temp_set = opened.copy()
            temp_set.add(valve)
            temp_dp = dp + flow_rates[valve]
            a = _walk(valve, temp_dp, t + 1, temp_p_sum, temp_set)

        b = {}
        for valve in tunnels[valve]:
            b[valve] = _walk(valve, dp, t + 1, temp_p_sum, opened)
        return max([a] + list(b.values()))

    max_p_sum = _walk(ROOT_NAME, 0, 0, 0, set())
    return max_p_sum


def main():
    t0 = time.time()
    valves, flow_rates, tunnels = get_valves()
    print(f"{valves=}")
    print(f"{flow_rates=}")
    print(f"{tunnels=}")

    assert get_bfs_shortest_path(tunnels, ROOT_NAME, "GG") == [
        "AA",
        "DD",
        "EE",
        "FF",
        "GG",
    ]

    distances = get_distances(valves, flow_rates, tunnels)
    print(f"{distances=}")

    max_p_sum = walk(flow_rates, tunnels)
    print(max_p_sum)

    print(f"finished in {time.time() - t0:0f} sec")


if __name__ == "__main__":
    main()
