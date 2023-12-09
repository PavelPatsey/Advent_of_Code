def get_history(inp):
    with open(inp, "r") as file:
        data = file.readlines()
    history = list(map(lambda x: [int(y) for y in x.strip().split()], data))
    return history


def main():
    history = get_history("test_input")
    print(history)


if __name__ == "__main__":
    main()
