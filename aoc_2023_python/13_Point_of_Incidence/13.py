def get_mirrors(input_file):
    with open(input_file, "r") as file:
        data = file.read()
    mirrors = data.strip().split("\n\n")
    mirrors = [x.strip().split() for x in mirrors]
    return mirrors


def get_transposed(mirror):
    return list(map(lambda x: "".join(x), map(list, zip(*mirror))))


def get_amount(mirror, part):
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
        mismatch = 0
        while condition and not is_break:
            is_break = False
            for r in range(len_rows):
                if mirror[r][left] != mirror[r][right]:
                    mismatch += 1
                    if mismatch > part - 1:
                        is_break = True
                        break
            dc += 1
            left = c - dc
            right = c + dc + 1
            condition = 0 <= left < right < len_cols
        c += 1
        if not is_break and mismatch == part - 1:
            line_is_found = True

    if c == len_cols:
        return get_amount(get_transposed(mirror), part=part) * 100
    else:
        return c


def get_answer(mirrors, part):
    return sum(map(lambda x: get_amount(x, part=part), mirrors))


def main():
    mirrors = get_mirrors("input")
    print(get_answer(mirrors, part=1))
    print(get_answer(mirrors, part=2))


if __name__ == "__main__":
    mirror_1 = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
    ]
    mirror_2 = [
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ]

    assert get_amount(mirror_1, part=1) == 5
    assert get_amount(mirror_2, part=1) == 400

    assert get_amount(mirror_1, part=2) == 300
    assert get_amount(mirror_2, part=2) == 100

    mirror = ["#.##..##.", "..#.##.#.", "##......#", "##......#"]
    t_mirror = ["#.##", "..##", "##..", "#...", ".#..", ".#..", "#...", "##..", "..##"]
    assert get_transposed(mirror) == t_mirror

    main()
