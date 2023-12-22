def get_bricks(input_file):
    def _get_parsed_line(line: str):
        return list(
            map(lambda x: [int(y) for y in x.split(",")], line.strip().split("~"))
        )

    with open(input_file, "r") as file:
        data = file.readlines()
    return [_get_parsed_line(line) for line in data]


def get_answer_1(bricks):
    return


def main():
    bricks = get_bricks("test_input")
    print(bricks)
    print(get_answer_1(bricks))


if __name__ == "__main__":
    main()
