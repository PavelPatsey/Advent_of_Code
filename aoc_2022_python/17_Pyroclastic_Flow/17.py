INPUT = "test_input"


def get_jets():
    with open(INPUT) as file:
        jets = file.read().strip()
    return jets


def main():
    jets = get_jets()


if __name__ == "__main__":
    main()
