import re
import time
from typing import Dict, List

INPUT = "test_input"
ROOT_NAME = "AA"
TIME_LIMIT = 25


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
        return Valve(name, int(flow_rate), connections.split(", "))

    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()

    valve_attributes = list(map(_split, data))

    valves = {}
    for valve in map(_make_valve, valve_attributes):
        valves[valve.name] = valve
    return valves


def get_all_travels(valves: Dict):
    def _valve_is_opened(valve: Valve, visited_valves_names: List):
        return valve.name + " opened" in visited_valves_names

    counter = 0

    def _travers(
        current_valve_name,
        visited_valves_names: List,
        open_valves_number,
        released_pressure: int,
        pressure_change: int,
        past_minutes: int,
    ):
        if past_minutes == TIME_LIMIT or open_valves_number == len(valves):
            travels.append(visited_valves_names)
            released_pressures.append(
                released_pressure + pressure_change * (TIME_LIMIT - past_minutes)
            )
            return

        current_valve = valves[current_valve_name]
        for valve_name in current_valve.connections + [current_valve_name]:
            if valve_name == current_valve_name:
                if not (
                    current_valve.flow_rate == 0
                    or _valve_is_opened(current_valve, visited_valves_names)
                ):
                    _travers(
                        current_valve_name,
                        visited_valves_names + [current_valve_name + " opened"],
                        open_valves_number + 1,
                        released_pressure + pressure_change,
                        pressure_change + current_valve.flow_rate,
                        past_minutes + 1,
                    )
            else:
                _travers(
                    valve_name,
                    visited_valves_names + [valve_name],
                    open_valves_number,
                    released_pressure + pressure_change,
                    pressure_change,
                    past_minutes + 1,
                )
        return

    travels = []
    released_pressures = []
    _travers(
        current_valve_name=ROOT_NAME,
        visited_valves_names=[ROOT_NAME],
        open_valves_number=0,
        released_pressure=0,
        pressure_change=0,
        past_minutes=0,
    )
    return travels, released_pressures


def main():
    t0 = time.time()
    valves = get_valves()
    travels, released_pressures = get_all_travels(valves)

    from pprint import pprint

    # print("travels")
    # pprint(travels)
    # print("released_pressures")
    # print(released_pressures)

    zipped = zip(travels, released_pressures)
    max_zipped = max(zipped, key=lambda x: x[1])
    print(max_zipped)
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
