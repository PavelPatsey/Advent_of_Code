INPUT = "input"


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


def main():
    document = get_document()
    print(get_answer_1(document))


if __name__ == "__main__":
    main()
