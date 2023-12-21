def get_map(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    elfs_map = [[x for x in line.strip()] for line in data]
    return elfs_map


def get_answer_1(elfs_map):
    pass


def main():
    elfs_map = get_map("test_input")
    print(elfs_map)
    print(get_answer_1(elfs_map))


if __name__ == "__main__":
    main()
