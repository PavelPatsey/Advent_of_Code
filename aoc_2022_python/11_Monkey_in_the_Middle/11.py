import math
import re
from collections import deque
from copy import deepcopy

INPUT = "input"
ROUNDS_NUMBER_1 = 20
ROUNDS_NUMBER_2 = 10_000


def get_monkeys():
    def _make_monkey(string: str):
        data = string.strip().split("\n")
        monkey = {
            "items": deque(map(int, (re.findall(r"\b\d+\b", data[1])))),
            "operation": data[2].split("Operation: new = ")[-1],
            "divisible_by": int(data[3].split("divisible by ")[-1]),
            "condition": (
                int(data[5].split("throw to monkey ")[-1]),
                int(data[4].split("throw to monkey ")[-1]),
            ),
            "inspections_number": 0,
        }
        return monkey

    with open(INPUT) as file:
        data = file.read().strip().split("\n\n")
    monkeys = list(map(_make_monkey, data))
    return monkeys


def get_answer_1(monkeys):
    for i in range(ROUNDS_NUMBER_1):
        for monkey in monkeys:
            while monkey["items"]:
                item = monkey["items"].pop()
                monkey["inspections_number"] += 1
                old = item
                item = eval(monkey["operation"])
                item = item // 3
                condition = item % monkey["divisible_by"] == 0
                to_monkey = monkey["condition"][condition]
                monkeys[to_monkey]["items"].append(item)

    inspections_numbers = [monkey["inspections_number"] for monkey in monkeys]
    inspections_numbers.sort()
    return inspections_numbers[-1] * inspections_numbers[-2]


def get_answer_2(monkeys):
    divs = [monkey["divisible_by"] for monkey in monkeys]
    mod = math.prod(divs)

    for i in range(ROUNDS_NUMBER_2):
        for monkey in monkeys:
            while monkey["items"]:
                item = monkey["items"].pop()
                monkey["inspections_number"] += 1
                old = item
                item = eval(monkey["operation"])
                item %= mod
                condition = item % monkey["divisible_by"] == 0
                to_monkey = monkey["condition"][condition]
                monkeys[to_monkey]["items"].append(item)

    inspections_numbers = [monkey["inspections_number"] for monkey in monkeys]
    inspections_numbers.sort()
    return inspections_numbers[-1] * inspections_numbers[-2]


def main():
    monkeys = get_monkeys()
    print(get_answer_1(deepcopy(monkeys)))
    print(get_answer_2(deepcopy(monkeys)))


if __name__ == "__main__":
    main()
