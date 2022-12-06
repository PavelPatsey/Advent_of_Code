def get_index(string):
    string = list(string)
    N = len(string)
    i = 3
    while i < N:
        if len(set([string[i], string[i - 1], string[i - 2], string[i - 3]])) == 4:
            return i + 1
        i += 1

def read_input():
    with open("input", "r") as file:
        string = file.read()
    return string

def main():
    string = read_input()
    print(get_index(string))


if __name__ == "__main__":
    assert get_index("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert get_index("nppdvjthqldpwncqszvftbrmjlhg") == 6

    main()
