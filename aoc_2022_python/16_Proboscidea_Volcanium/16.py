import re

INPUT = "test_input"


class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections


class Graph:
    pass


def read_input():
    def split(string):
        return re.split("Valve | has flow rate=|; tunnels lead to valves ", string)[1:]

    with open(INPUT, "r") as file:
        data = file.read().strip().splitlines()
    return list(map(split, data))


def get_valves(data):
    pass


def main():
    data = read_input()
    print(data)
    # valves = get_valves(INPUT)
    # print(valves)


if __name__ == "__main__":
    main()
