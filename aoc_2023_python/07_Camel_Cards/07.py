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

INPUT = "test_input"


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


def main():
    hands_bids = get_hands_bids()
    print(hands_bids)


if __name__ == "__main__":
    main()
