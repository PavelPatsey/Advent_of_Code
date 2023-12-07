from collections import Counter
from functools import cmp_to_key

INPUT = "input"


CARDS_DICT = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

CARDS_DICT_2 = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def get_hands_bids(cards_dict):
    with open(INPUT, "r") as file:
        data = file.readlines()
    hands_bids = []
    for line in data:
        hand_str, bid_str = line.strip().split()
        bid = int(bid_str)
        hand_list = [cards_dict[x] for x in hand_str]
        hands_bids.append((hand_list, bid))
    return hands_bids


def get_max_hand(hand):
    if 1 not in hand:
        return hand

    counter_dict = Counter(hand)

    max_key, max_value = 0, 0
    for key, value in counter_dict.items():
        if key != 1 and value >= max_value:
            max_key, max_value = key, value

    if max_key == 0:
        max_key = 13

    return [x if x != 1 else max_key for x in hand]


def get_hand_cost(hand):
    counter_dict = Counter(hand)
    sorted_values = sorted(counter_dict.values())

    if sorted_values == [5]:
        cost = 7
    elif sorted_values == [1, 4]:
        cost = 6
    elif sorted_values == [2, 3]:
        cost = 5
    elif sorted_values == [1, 1, 3]:
        cost = 4
    elif sorted_values == [1, 2, 2]:
        cost = 3
    elif sorted_values == [1, 1, 1, 2]:
        cost = 2
    elif sorted_values == [1, 1, 1, 1, 1]:
        cost = 1
    else:
        print("Error!")
        assert False
    return cost


def compare_hands(hand_1, hand_2, part) -> int:
    if part == 1:
        cost_hand_1 = get_hand_cost(hand_1)
        cost_hand_2 = get_hand_cost(hand_2)
    else:
        cost_hand_1 = get_hand_cost(get_max_hand(hand_1))
        cost_hand_2 = get_hand_cost(get_max_hand(hand_2))

    if cost_hand_1 > cost_hand_2:
        return 1
    elif cost_hand_1 < cost_hand_2:
        return -1
    else:
        if hand_1 > hand_2:
            return 1
        elif hand_1 == hand_2:
            return 0
        else:
            return -1


def compare_hands_bids(h_b_1, h_b_2) -> int:
    return compare_hands(h_b_1[0], h_b_2[0], part=1)


def compare_hands_bids_2(h_b_1, h_b_2) -> int:
    return compare_hands(h_b_1[0], h_b_2[0], part=2)


def get_answer(hands_bids, compare_hands_bids_function):
    sorted_hands_bids = sorted(
        hands_bids,
        key=cmp_to_key(compare_hands_bids_function),
        reverse=False,
    )
    return sum(map(lambda x: (x[0] + 1) * x[1][1], enumerate(sorted_hands_bids)))


def main():
    hands_bids = get_hands_bids(CARDS_DICT)
    print(get_answer(hands_bids, compare_hands_bids))
    hands_bids_2 = get_hands_bids(CARDS_DICT_2)
    print(get_answer(hands_bids_2, compare_hands_bids_2))


if __name__ == "__main__":
    assert compare_hands_bids(([2, 3, 3, 10, 13], 765), ([5, 5, 5, 10, 11], 684)) == -1
    assert compare_hands_bids(([2, 2, 2, 2, 2], 765), ([2, 2, 2, 2, 1], 684)) == 1
    assert compare_hands_bids(([13, 13, 6, 7, 7], 28), ([13, 10, 11, 11, 10], 220)) == 1

    assert get_max_hand([13, 13, 1, 7, 7]) == [13, 13, 7, 7, 7]
    assert get_max_hand([1, 2, 2, 4, 5]) == [2, 2, 2, 4, 5]
    assert get_max_hand([1, 1, 1, 1, 1]) == [13, 13, 13, 13, 13]
    assert get_max_hand([7, 9, 9, 7, 1]) == [7, 9, 9, 7, 9]
    assert get_max_hand([1, 1, 1, 1, 2]) == [2, 2, 2, 2, 2]
    assert get_max_hand([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]
    assert get_max_hand([10, 5, 5, 1, 5]) == [10, 5, 5, 5, 5]
    assert get_max_hand([10, 5, 5, 2, 5]) == [10, 5, 5, 2, 5]
    assert get_max_hand([12, 10, 1, 1, 10]) == [12, 10, 10, 10, 10]

    main()
