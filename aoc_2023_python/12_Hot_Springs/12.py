def get_records(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    records = [
        (
            line.strip().split()[0],
            list(map(int, line.strip().split()[1].split(","))),
        )
        for line in data
    ]
    return records


def get_possible_arrangements_number(line):
    return


def get_answer_1(records):
    return sum(map(get_possible_arrangements_number, records))


def main():
    records = get_records("test_input")
    print(records)
    print(get_answer_1(records))


if __name__ == "__main__":
    main()
