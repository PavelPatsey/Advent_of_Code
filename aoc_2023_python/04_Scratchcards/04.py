INPUT = "test_input"


def get_cards():
    with open(INPUT, "r") as file:
        data = file.readlines()
    return data


def main():
    cards = get_cards()
    print(cards)


if __name__ == "__main__":
    main()
