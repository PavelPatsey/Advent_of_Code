import re

INPUT = "test_input"


class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections

    def __str__(self):
        return f"name = {self.name}, flow_rate = {self.flow_rate}, connection = {self.connections}"


class Graph:
    pass


def get_valves():
    def _split(string):
        return re.split(
            "Valve | has flow rate=|; tunnels lead to valves |; tunnel leads to valve ",
            string,
        )[1:]

    def _make_valve(valve_attributes):
        name, flow_rate, connections = valve_attributes
        return Valve(name, int(flow_rate), connections.split())

    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()

    valve_attributes = list(map(_split, data))
    valves = list(map(_make_valve, valve_attributes))
    return valves


def main():
    valves = get_valves()
    for valve in valves:
        print(valve)


if __name__ == "__main__":
    main()
