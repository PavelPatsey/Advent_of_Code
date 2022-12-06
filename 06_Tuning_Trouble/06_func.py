def get_index(string, number):
    zipped = zip(*(string[i:] for i in range(number)))
    enumerated = enumerate(zipped)
    res = (i for i, x in enumerated if len(set(x)) == number)
    return list(res)[0] + number


def read_input():
    with open("input", "r") as file:
        string = file.read()
    return string


def main():
    string = read_input()
    print(get_index(string, 4))
    print(get_index(string, 14))


if __name__ == "__main__":
    assert get_index("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
    assert get_index("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6

    assert get_index("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert get_index("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23

    main()
