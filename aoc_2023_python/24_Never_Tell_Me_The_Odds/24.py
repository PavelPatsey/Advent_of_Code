import re


def get_stone(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[int(x) for x in re.split(r",|@", line)] for line in data]


def get_answer_1(stone):
    return


def main():
    stone = get_stone("test_input")
    print(stone)
    print(get_answer_1(stone))


if __name__ == "__main__":
    main()
