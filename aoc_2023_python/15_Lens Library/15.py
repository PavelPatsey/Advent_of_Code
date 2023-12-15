def get_sequence(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return data[0].strip().split(",")


def get_hash(string):
    current_value = 0
    for ch in string:
        current_value += ord(ch)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def get_answer_1(sequence):
    return sum(map(get_hash, sequence))


def main():
    sequence = get_sequence("input")
    print(sequence)
    print(get_answer_1(sequence))


if __name__ == "__main__":
    main()
