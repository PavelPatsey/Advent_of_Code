def get_mirrors(input_file):
    with open(input_file, "r") as file:
        data = file.read()
    mirrors = data.strip().split("\n\n")
    mirrors = [x.strip().split() for x in mirrors]
    return mirrors


def get_amount(mirror):
    # len_rows = len(mirror)
    # len_cols = len(mirror[0])
    pass


def get_answer_1(mirrors):
    lst = list(map(get_amount, mirrors))
    return sum(lst)


def main():
    mirrors = get_mirrors("test_input")
    print(mirrors)
    print(get_answer_1(mirrors))


if __name__ == "__main__":
    mirror = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
    ]
    assert get_amount(mirror) == 5

    main()
v
