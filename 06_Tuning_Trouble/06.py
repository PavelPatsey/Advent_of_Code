def get_index(string, number):
    N = len(string)
    i = number - 1
    while i < N:
        characters = []
        for j in range(number):
            characters.append(string[i - j])

        if len(set(characters)) == number:
            return i + 1
        i += 1


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
