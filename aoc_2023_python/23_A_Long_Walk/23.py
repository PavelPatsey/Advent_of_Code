def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return [line.strip() for line in data]


def get_answer_1(matrix):
    return


def main():
    matrix = get_matrix("test_input")
    print(matrix)
    print(get_answer_1(matrix))


if __name__ == "__main__":
    main()
