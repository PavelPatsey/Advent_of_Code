import re

INPUT = "test_input"


def get_monkeys():
    def _make_monkey(string: str):
        data = string.strip().split("\n")
        monkey = {
            "items": list(map(int, (re.findall(r"\b\d+\b", data[1])))),
            "operation": data[2].split("Operation: new = ")[-1],
            "divisible_by": int(data[3].split("divisible by ")[-1]),
            "condition": (
                int(data[4].split("throw to monkey ")[-1]),
                int(data[5].split("throw to monkey ")[-1]),
            ),
        }
        return monkey

    with open(INPUT) as file:
        data = file.read().strip().split("\n\n")
    monkeys = list(map(_make_monkey, data))
    return monkeys


def main():
    monkeys = get_monkeys()
    print(monkeys)


if __name__ == "__main__":
    main()
