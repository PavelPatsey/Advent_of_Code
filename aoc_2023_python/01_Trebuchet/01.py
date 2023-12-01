INPUT = "input"

NUMERIC_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_document():
    with open(INPUT, "r") as file:
        document = file.readlines()
    return document


def get_answer_1(document):
    numbers = []
    for line in document:
        filtered = list(filter(lambda x: x.isnumeric(), line))
        numbers.append(int("".join(filtered[0] + filtered[-1])))
    return sum(numbers)


def get_answer_2(document):
    numbers = []
    for line in document:
        digits = []
        for index, char in enumerate(line):
            if char.isnumeric():
                digits.append(char)
            for key, value in NUMERIC_DICT.items():
                if line[index:].startswith(key):
                    digits.append(NUMERIC_DICT[key])
        numbers.append(digits)
    numbers = [int(digit[0] + digit[-1]) for digit in numbers]
    return sum(numbers)


def main():
    document = get_document()
    print(get_answer_1(document))
    print(get_answer_2(document))


if __name__ == "__main__":
    main()
