INPUT = "test_input"


def get_races():
    with open(INPUT, "r") as file:
        data = file.readlines()
    races = [[int(y) for y in x.split(":")[1].strip().split()] for x in data]
    races = list(zip(races[0], races[1]))
    return races


def main():
    races = get_races()
    print(races)


if __name__ == "__main__":
    main()
