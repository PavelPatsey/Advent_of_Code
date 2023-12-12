def get_rows(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return [row.strip() for row in data]


def main():
    rows = get_rows("test_input")
    print(rows)


if __name__ == "__main__":
    main()
