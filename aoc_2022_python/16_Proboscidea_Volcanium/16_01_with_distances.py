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
        if type(path) == str:
            node = path
        elif type(path) == list:
            node = path[-1]
        else:
            print("ERROR!")
            return
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                if type(path) == str:
                    new_path = [path]
                elif type(path) == list:
                    new_path = path.copy()
                else:
                    print("ERROR!")
                    return

                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path

            visited.append(node)

    return []


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
    print(f"{valves=}")
    print(f"{flow_rates=}")
    print(f"{tunnels=}")

    print(get_bfs_shortest_path(tunnels, ROOT_NAME, "GG"))

    # max_p_sum = walk(ROOT_NAME, 0, 0, 0, set())
    # print(max_p_sum)

    print(f"finished in {time.time() - t0:0f} sec")


if __name__ == "__main__":
    main()
