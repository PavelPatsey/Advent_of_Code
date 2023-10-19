import re
from typing import List

INPUT = "test_input"


class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections
        self.is_opened = False

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
        return Valve(name, int(flow_rate), connections.split(", "))

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

    def get_valve(self, valve_name: str) -> Valve:
        return self.valves.get(valve_name)

    def get_max_pressure_release(self):
        pass

    def get_all_travels(self):
        travels = []
        released_pressures = []

        def _get_pressure_release_per_minute(visited_valves_names):
            valve_names = set(visited_valves_names)
            pressure_release_per_minute = 0
            for valve_name in valve_names:
                valve = self.get_valve(valve_name)
                pressure_release_per_minute += valve.flow_rate
            return pressure_release_per_minute

        def _travers(
            go_to_valve_name,
            visited_valves_names: List,
            released_pressure: int,
            past_minutes: int,
        ):
            visited_valves_names.append(go_to_valve_name)
            print(past_minutes)
            past_minutes += 1
            released_pressure += _get_pressure_release_per_minute(visited_valves_names)

            if past_minutes == 30:
                travels.append(visited_valves_names)
                released_pressures.append(released_pressure)
                print(f"{len(visited_valves_names) = }")
                print(visited_valves_names)
                return

            current_valve = self.get_valve(go_to_valve_name)
            if not (current_valve.flow_rate == 0 or current_valve.is_opened):
                current_valve.is_opened = True

            for valve_name in current_valve.connections:
                _travers(
                    valve_name, visited_valves_names, released_pressure, past_minutes
                )

        _travers(self.root.name, [], 0, 0)
        return travels, released_pressures


def main():
    valves = get_valves()
    graph = Graph(valves)
    travels, released_pressures = graph.get_all_travels()
    print(travels)
    print(released_pressures)


if __name__ == "__main__":
    main()
