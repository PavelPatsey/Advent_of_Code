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


def get_card_cost(card):
    cost = 0
    for number in card[0]:
        if number in card[1]:
            cost += 1
    return cost


def get_answer_1(cards):
    result = 0
    for card in cards:
        cost = get_card_cost(card)
        if cost:
            result += 2 ** (cost - 1)
    return result


def get_answer_2(cards):
    len_cards = len(cards)
    number_of_cards = [1] * len_cards
    for i in range(len_cards):
        for x in range(get_card_cost(cards[i])):
            number_of_cards[i + 1 + x] += number_of_cards[i]
    return sum(number_of_cards)


def main():
    cards = get_cards()
    print(get_answer_1(cards))
    print(get_answer_2(cards))


if __name__ == "__main__":
    main()
