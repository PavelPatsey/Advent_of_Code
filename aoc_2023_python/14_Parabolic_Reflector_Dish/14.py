def get_platform(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    platform = [row.strip() for row in data]
    return platform


def get_answer_1(platform):
    return


def main():
    platform = get_platform("test_input")
    print(platform)
    print(get_answer_1(platform))


if __name__ == "__main__":
    main()
