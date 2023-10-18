import re
from typing import List

INPUT = "test_input"


class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections

    def __str__(self):
        return f"name = {self.name}, flow_rate = {self.flow_rate}, connections = {self.connections}"


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


class Graph:
    def __init__(self, valves: List):
        self.valves = {}
        for valve in valves:
            self.add_valve(valve)
        self.root = self.get_valve("AA")

    def add_valve(self, valve: Valve):
        self.valves[valve.name] = valve

    def get_valve(self, valve_name: str):
        return self.valves.get(valve_name)

    def get_all_travels(self):
        pass

    def get_biggest_pressure_release(self):
        pass


def main():
    valves = get_valves()
    graph = Graph(valves)
    a = 1


if __name__ == "__main__":
    main()
