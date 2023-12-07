from collections import defaultdict
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


def get_hands_bids():
    with open(INPUT, "r") as file:
        data = file.readlines()
    hands_bids = []
    for line in data:
        hand_str, bid_str = line.strip().split()
        bid = int(bid_str)
        hand_list = [CARDS_DICT[x] for x in hand_str]
        hands_bids.append((hand_list, bid))
    return hands_bids


def get_hands_bids_2():
    with open(INPUT, "r") as file:
        data = file.readlines()
    hands_bids = []
    for line in data:
        hand_str, bid_str = line.strip().split()
        bid = int(bid_str)
        hand_list = [CARDS_DICT_2[x] for x in hand_str]
        hands_bids.append((hand_list, bid))
    return hands_bids


def get_converted_hand(hand):
    d = defaultdict(int)
    for h in hand:
        d[h] += 1
    return [h for h in hand if d[h] >= 2]


def compare_hands(hand_1, hand_2) -> int:
    if len(set(hand_1)) < len(set(hand_2)):
        return 1
    elif len(set(hand_1)) > len(set(hand_2)):
        return -1
    else:
        converted_hand_1 = get_converted_hand(hand_1)
        converted_hand_2 = get_converted_hand(hand_2)
        if len(set(converted_hand_1)) < len(set(converted_hand_2)):
            return 1
        elif len(set(converted_hand_1)) > len(set(converted_hand_2)):
            return -1
        else:
            if hand_1 > hand_2:
                return 1
            elif hand_1 == hand_2:
                return 0
            else:
                return -1


def compare_hands_bids(h_b_1, h_b_2) -> int:
    return compare_hands(h_b_1[0], h_b_2[0])


def get_jokered_hands(hand_list):
    jokered_hands = [hand_list]
    all_jokered_hands = []
    len_hand = len(hand_list)
    replacements_list = [card for card in set(hand_list) if card != 1]
    # (lst[:i] + ["j"] + lst[i + 1:])
    while jokered_hands:
        hand = jokered_hands.pop()
        if 1 in hand:
            for i in range(len_hand):
                if 1 == hand[i]:
                    for card in replacements_list:
                        jokered_hands.append(hand[:i] + [card] + hand[i + 1 :])
        else:
            if hand not in all_jokered_hands:
                all_jokered_hands.append(hand)
    return all_jokered_hands


def get_max_hand(hand):
    all_jokered_hands = get_jokered_hands(hand)
    return


def compare_hands_bids_2(h_b_1, h_b_2) -> int:
    hand_1 = h_b_1[0]
    hand_2 = h_b_2[0]
    if 1 in hand_1:
        max_hand_1 = get_max_hand(hand_1)
    if 1 in hand_2:
        max_hand_2 = get_max_hand(hand_2)
    return


def get_answer_1(hands_bids):
    sorted_hands_bids = sorted(
        hands_bids, key=cmp_to_key(compare_hands_bids), reverse=False
    )
    sorted_binds = [x[1] for x in sorted_hands_bids]
    return sum(map(lambda x: (x[0] + 1) * x[1], enumerate(sorted_binds)))


def get_answer_2(hands_bids):
    sorted_hands_bids = sorted(
        hands_bids, key=cmp_to_key(compare_hands_bids_2), reverse=False
    )
    sorted_binds = [x[1] for x in sorted_hands_bids]
    return sum(map(lambda x: (x[0] + 1) * x[1], enumerate(sorted_binds)))


def main():
    hands_bids = get_hands_bids()
    print(get_answer_1(hands_bids))
    # hands_bids_2 = get_hands_bids()
    # print(get_answer_1(hands_bids_2))


if __name__ == "__main__":
    assert get_converted_hand([2, 3, 3, 10, 13]) == [3, 3]
    assert get_converted_hand([5, 5, 5, 10, 11]) == [5, 5, 5]

    assert compare_hands_bids(([2, 3, 3, 10, 13], 765), ([5, 5, 5, 10, 11], 684)) == -1
    assert compare_hands_bids(([2, 2, 2, 2, 2], 765), ([2, 2, 2, 2, 1], 684)) == 1
    assert compare_hands_bids(([13, 13, 6, 7, 7], 28), ([13, 10, 11, 11, 10], 220)) == 1

    assert get_jokered_hands([13, 13, 1, 7, 7]) == [
        [13, 13, 7, 7, 7],
        [13, 13, 13, 7, 7],
    ]

    assert get_jokered_hands([1, 13, 1, 1, 1]) == [
        [13, 13, 13, 13, 13],
    ]
    main()
