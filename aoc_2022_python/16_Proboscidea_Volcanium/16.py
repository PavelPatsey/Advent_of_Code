import re
import time
from typing import Dict, List

INPUT = "test_input"
ROOT_NAME = "AA"
TIME_LIMIT = 20
MAX_REPS = 5


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
    def _get_pressure_change(visited_valves_names):
        valve_names = set(visited_valves_names)
        pressure_change = 0
        for valve_name in valve_names:
            valve = valves.get(valve_name)
            if valve:
                pressure_change += valve.flow_rate
        return pressure_change

    def _all_valves_are_opened(visited_valves_names):
        return all(
            map(
                lambda valve: valve.name + " opened" in visited_valves_names,
                valves.values(),
            )
        )

    def _valve_is_opened(valve: Valve, visited_valves_names: List):
        return valve.name + " opened" in visited_valves_names

    # вот это условие не работает, так как можно много раз посещать один и тот же узел
    # можно попробовать сделать по другому
    # итеративно выяснять максимальный сброс давления к некоторому ходу, и отбрасывать например неудачные ходы
    def _trip_is_relevant(visited_valves_names: List) -> bool:
        return len(visited_valves_names) - len(set(visited_valves_names)) < MAX_REPS

    def _travers(
        go_to_valve_name,
        visited_valves_names: List,
        released_pressure: int,
        past_minutes: int,
    ):
        pressure_change = _get_pressure_change(visited_valves_names)

        if not _trip_is_relevant(visited_valves_names):
            return

        if past_minutes == TIME_LIMIT or _all_valves_are_opened(visited_valves_names):
            travels.append(visited_valves_names)
            released_pressures.append(
                released_pressure + pressure_change * (TIME_LIMIT - past_minutes)
            )
            len_travels = len(travels)
            if len_travels % 1000 == 0:
                print(len_travels)
            return

        current_valve = valves[go_to_valve_name]
        if not (
            current_valve.flow_rate == 0
            or _valve_is_opened(current_valve, visited_valves_names)
        ):
            _travers(
                go_to_valve_name,
                visited_valves_names + [go_to_valve_name + " opened"],
                released_pressure + pressure_change,
                past_minutes + 1,
            )

        for valve_name in current_valve.connections:
            _travers(
                valve_name,
                visited_valves_names + [go_to_valve_name],
                released_pressure + pressure_change,
                past_minutes + 1,
            )
        return

    travels = []
    released_pressures = []
    _travers(ROOT_NAME, [], 0, 1)
    return travels, released_pressures


def main():
    t0 = time.time()
    valves = get_valves()
    travels, released_pressures = get_all_travels(valves)

    print(travels)
    print("travels")
    print(released_pressures)
    print("released_pressures")

    zipped = zip(travels, released_pressures)
    max_zipped = max(zipped, key=lambda x: x[1])
    print(max_zipped)
    print(f"finished in {time.time() - t0:0f} sec")

    test_example = [
        "AA",
        "DD opened",
        "DD",
        "CC",
        "BB opened",
        "AA",
        "II",
        "JJ opened",
        "II",
        "AA",
        "DD",
        "EE",
        "FF",
        "GG",
        "HH opened",
        "GG",
        "FF",
        "EE opened",
        "DD",
        "CC opened",
    ]


if __name__ == "__main__":
    main()
