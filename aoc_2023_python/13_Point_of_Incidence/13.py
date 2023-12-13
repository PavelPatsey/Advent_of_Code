def get_mirrors(input_file):
    with open(input_file, "r") as file:
        data = file.read()
    mirrors = data.strip().split("\n\n")
    mirrors = [x.strip().split() for x in mirrors]
    return mirrors


def get_transposed(mirror):
    return list(map(lambda x: "".join(x), map(list, zip(*mirror))))


def get_amount(mirror):
    len_rows = len(mirror)
    len_cols = len(mirror[0])
    c = 0
    line_is_found = False
    while c < len_cols and not line_is_found:
        dc = 0
        left = c - dc
        right = c + dc + 1
        condition = 0 <= left < right < len_cols
        is_break = False
        while condition and not is_break:
            is_break = False
            for r in range(len_rows):
                if mirror[r][left] != mirror[r][right]:
                    is_break = True
                    break
            dc += 1
            left = c - dc
            right = c + dc + 1
            condition = 0 <= left < right < len_cols
        c += 1
        if not is_break:
            line_is_found = True

    if c == len_cols:
        return get_amount(get_transposed(mirror)) * 100
    else:
        return c


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

    mirror = [
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ]
    assert get_amount(mirror) == 400

    mirror = ["#.##..##.", "..#.##.#.", "##......#", "##......#"]
    t_mirror = ["#.##", "..##", "##..", "#...", ".#..", ".#..", "#...", "##..", "..##"]
    assert get_transposed(mirror) == t_mirror

    main()
