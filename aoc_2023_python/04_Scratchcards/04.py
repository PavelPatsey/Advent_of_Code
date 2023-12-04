import re
from typing import List

INPUT = "test_input"


def get_cards():
    def _make_card(string: str) -> List:
        card = string.strip().replace("|", "!")
        card = re.split(": | ! ", card)[1:]
        card = map(lambda x: x.split(), card)
        card = list(map(lambda x: [int(y) for y in x], card))
        return card

    with open(INPUT, "r") as file:
        data = file.readlines()
    cards = list(map(_make_card, data))
    return cards


def main():
    cards = get_cards()
    print(cards)


if __name__ == "__main__":
    main()
