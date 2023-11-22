import re
from collections import deque
from operator import add, mul

INPUT = "test_input"
ROUNDS_NUMBER = 20


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
    def _get_item_after_operation(item: int, operation_str: str) -> int:
        _, operation, b = operation_str.strip().split()
        b = item if b == "old" else int(b)
        if operation == "+":
            return item + b
        elif operation == "*":
            return item * b

    for i in range(ROUNDS_NUMBER):
        for monkey in monkeys:
            item = monkey["items"].pop()
            item = _get_item_after_operation(item, monkey["operation"])
            item = item // 3
            condition = item % monkey["divisible_by"] == 0
            to_monkey = monkey["condition"][condition]
            monkeys[to_monkey]["items"].append(item)
        for monkey in monkeys:
            monkey["inspections_number"] += len(monkey["items"])


def main():
    monkeys = get_monkeys()
    print(get_answer_1(monkeys))


if __name__ == "__main__":
    main()
