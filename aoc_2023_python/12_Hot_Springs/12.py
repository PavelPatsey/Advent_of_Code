def get_records(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    records = [
        (
            row.strip().split()[0],
            list(map(int, row.strip().split()[1].split(","))),
        )
        for row in data
    ]

    return records


def get_answer_1(rows):
    pass


def main():
    rows = get_records("test_input")
    print(rows)
    print(get_answer_1(rows))


if __name__ == "__main__":
    main()
