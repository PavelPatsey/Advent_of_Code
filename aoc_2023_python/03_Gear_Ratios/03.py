INPUT = "test_input"


def get_schemas():
    with open(INPUT, "r") as file:
        data = file.readlines()
    first_last_string = ["." * (len(data[0]) + 1)]
    schemas = (
        first_last_string
        + list(map(lambda x: "." + x[:-1] + ".", data))
        + first_last_string
    )
    return schemas


def get_answer_1(schemas):
    pass


def main():
    schemas = get_schemas()
    print(schemas)
    print(get_answer_1(schemas))


if __name__ == "__main__":
    main()
