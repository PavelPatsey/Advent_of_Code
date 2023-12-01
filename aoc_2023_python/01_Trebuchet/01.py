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
    result = []
    for line in document:
        filtered = filter(lambda x: x.isnumeric(), line)
        lst = list(filtered)
        lst = lst[0] + lst[-1]
        result.append(int("".join(lst)))
    return sum(result)


def get_answer_2(document):
    digits = []
    for line in document:
        digits_from_line = []
        for index, char in enumerate(line):
            if char.isnumeric():
                digits_from_line.append(char)
            for key, value in NUMERIC_DICT.items():
                if line[index:].startswith(key):
                    digits_from_line.append(NUMERIC_DICT[key])
        digits.append(digits_from_line)
    digits = [int(digit[0] + digit[-1]) for digit in digits]
    return sum(digits)


def main():
    document = get_document()
    print(get_answer_1(document))
    print(get_answer_2(document))


if __name__ == "__main__":
    main()
