INPUT = "test_input"


def get_packets():
    with open(INPUT) as file:
        data = file.read().strip().split("\n\n")
    packets = [tuple(map(eval, item.split("\n"))) for item in data]
    return packets


def main():
    packets = get_packets()
    print(packets)


if __name__ == "__main__":
    main()
