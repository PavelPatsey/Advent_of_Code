import re
from typing import List

INPUT = "input"


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


def get_answer_1(cards):
    result = 0
    for card in cards:
        counter = 0
        for number in card[0]:
            if number in card[1]:
                counter += 1
        if counter != 0:
            result += 2 ** (counter - 1)
    return result


def main():
    cards = get_cards()
    print(get_answer_1(cards))


if __name__ == "__main__":
    main()
