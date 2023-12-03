INPUT = "test_input"


def get_schema():
    with open(INPUT, "r") as file:
        data = file.readlines()
    first_last_string = ["." * (len(data[0]) + 1)]
    schema = (
        first_last_string
        + list(map(lambda x: "." + x[:-1] + ".", data))
        + first_last_string
    )
    return schema


def main():
    schema = get_schema()
    print(schema)


if __name__ == "__main__":
    main()
