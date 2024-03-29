INPUT = "input"
MOVES_NUMBER = 2022
ROCKS = [
    [
        "..@@@@.",
    ],
    [
        "...@...",
        "..@@@..",
        "...@...",
    ],
    [
        "..@@@..",
        "....@..",
        "....@..",
    ],
    [
        "..@....",
        "..@....",
        "..@....",
        "..@....",
    ],
    [
        "..@@...",
        "..@@...",
    ],
]


def get_jets():
    with open(INPUT) as file:
        jets = file.read().strip()
    return jets


def is_can_be_shifted(chamber, jet):
    chamber_index = len(chamber) - 1
    while "@" not in chamber[chamber_index] and chamber_index >= 0:
        chamber_index -= 1
    keep_looking = "@" in chamber[chamber_index]
    can_be_shifted = keep_looking
    if jet == ">":
        comparison_index = -1
        comparison_tuple = ("@", "#")
    else:
        comparison_index = 0
        comparison_tuple = ("#", "@")
    while chamber_index >= 0 and keep_looking and can_be_shifted:
        string = chamber[chamber_index]
        can_be_shifted = string[comparison_index] != "@"
        string_index = 0
        while string_index < len(string) - 1 and can_be_shifted:
            if (string[string_index], string[string_index + 1]) == comparison_tuple:
                can_be_shifted = False
            string_index += 1
        chamber_index -= 1
        keep_looking = "@" in chamber[chamber_index]
    return can_be_shifted


def get_shifted_chamber(chamber, jet):
    new_chamber = chamber.copy()
    chamber_index = len(new_chamber) - 1
    while "@" not in chamber[chamber_index] and chamber_index >= 0:
        chamber_index -= 1
    keep_looking = "@" in new_chamber[chamber_index]

    while chamber_index >= 0 and keep_looking:
        if jet == ">":
            string = new_chamber[chamber_index]
        else:
            string = "".join(list(reversed(new_chamber[chamber_index])))
        len_string = len(string)
        string_index = len_string - 1
        new_string = ""
        while string_index >= 1:
            if string[string_index - 1] == "@":
                new_string = "@" + new_string
            else:
                if string[string_index] == "@":
                    new_string = "." + new_string
                else:
                    new_string = string[string_index] + new_string
            string_index -= 1
        if string[0] == "@":
            new_string = "." + new_string
        else:
            new_string = string[0] + new_string

        if jet == ">":
            new_chamber[chamber_index] = new_string
        else:
            new_chamber[chamber_index] = "".join(list(reversed(new_string)))
        chamber_index -= 1
        keep_looking = "@" in new_chamber[chamber_index]

    return new_chamber


def is_can_be_moved_down(chamber):
    chamber_index = len(chamber) - 1
    while "@" not in chamber[chamber_index] and chamber_index >= 0:
        chamber_index -= 1
    keep_looking = "@" in chamber[chamber_index]
    can_be_moved_down = keep_looking
    while chamber_index >= 1 and keep_looking and can_be_moved_down:
        string = chamber[chamber_index]
        next_string = chamber[chamber_index - 1]
        len_string = len(string)
        for i in range(len_string):
            if string[i] == "@" and next_string[i] not in (".", "@"):
                can_be_moved_down = False
        chamber_index -= 1
        keep_looking = "@" in chamber[chamber_index]
    if "@" in chamber[0]:
        can_be_moved_down = False
    return can_be_moved_down


def get_moved_down_chamber(chamber):
    new_chamber = chamber.copy()
    chamber_index = len(new_chamber) - 1
    while "@" not in chamber[chamber_index] and chamber_index >= 0:
        chamber_index -= 1
    keep_looking = "@" in new_chamber[chamber_index]
    len_string = len(new_chamber[0])
    indexes = []
    while chamber_index >= 0 and keep_looking:
        string = new_chamber[chamber_index]
        for i in range(len_string):
            if string[i] == "@":
                indexes.append((chamber_index, i))
        chamber_index -= 1
        keep_looking = "@" in new_chamber[chamber_index]

    for i, j in indexes:
        lst = list(new_chamber[i])
        lst[j] = "."
        string = "".join(lst)
        new_chamber[i] = string
    for i, j in indexes:
        lst = list(new_chamber[i - 1])
        lst[j] = "@"
        string = "".join(lst)
        new_chamber[i - 1] = string
    if new_chamber[-1] == ".......":
        del new_chamber[-1]
    return new_chamber


def get_frozen_chamber(chamber):
    new_chamber = chamber.copy()
    chamber_index = len(new_chamber) - 1
    while "@" not in chamber[chamber_index]:
        chamber_index -= 1
    keep_looking = "@" in new_chamber[chamber_index]
    len_lst = len(new_chamber[0])
    while chamber_index >= 0 and keep_looking:
        lst = list(new_chamber[chamber_index])
        for i in range(len_lst):
            if lst[i] == "@":
                lst[i] = "#"
        new_chamber[chamber_index] = "".join(lst)
        chamber_index -= 1
        keep_looking = "@" in new_chamber[chamber_index]
    return new_chamber


def get_chamber_after_moves(jets, moves_number):
    len_rocks = len(ROCKS)
    rock_index = 0
    len_jets = len(jets)
    jet_index = 0
    chamber = []
    n = 0
    while n < moves_number:
        rock_index = rock_index % len_rocks
        chamber += ["......."] * 3
        for rock_part in ROCKS[rock_index]:
            chamber.append(rock_part)

        jet_index = jet_index % len_jets
        jet = jets[jet_index]
        if is_can_be_shifted(chamber, jet):
            chamber = get_shifted_chamber(chamber, jet)
        jet_index += 1

        while is_can_be_moved_down(chamber):
            chamber = get_moved_down_chamber(chamber)

            jet_index = jet_index % len_jets
            jet = jets[jet_index]
            if is_can_be_shifted(chamber, jet):
                chamber = get_shifted_chamber(chamber, jet)
            jet_index += 1

        chamber = get_frozen_chamber(chamber)
        rock_index += 1
        n += 1
    return chamber


def main():
    jets = get_jets()

    answer_1 = get_chamber_after_moves(jets, MOVES_NUMBER)
    for i in reversed(answer_1):
        print(i)

    print(len(get_chamber_after_moves(jets, MOVES_NUMBER)))


if __name__ == "__main__":
    chamber = [
        "..####.",
        ".......",
        ".......",
        ".......",
        "...@...",
        "..@@@..",
        "...@...",
    ]
    assert is_can_be_shifted(chamber, ">") is True

    chamber = [
        "..####.",
        ".......",
        ".......",
        ".......",
        ".....@.",
        "....@@@",
        ".....@.",
    ]
    assert is_can_be_shifted(chamber, ">") is False

    chamber = [
        "..####.",
        ".......",
        ".......",
        ".......",
        "...@...",
        "..@@@..",
        "...@#..",
    ]
    assert is_can_be_shifted(chamber, ">") is False

    chamber = [
        "..####.",
        ".......",
        ".......",
        ".......",
        "...@...",
        "..@@@..",
        "...@...",
    ]
    assert is_can_be_shifted(chamber, "<") is True

    chamber = [
        "..####.",
        ".......",
        ".......",
        ".......",
        ".@.....",
        "@@@....",
        ".@.....",
    ]
    assert is_can_be_shifted(chamber, "<") is False

    chamber = [
        "..####.",
        ".......",
        ".......",
        ".......",
        "...@...",
        "..@@@..",
        "...#@..",
    ]
    assert is_can_be_shifted(chamber, "<") is False

    chamber = [
        "...#...",
        "..###..",
        "...#..",
    ]
    assert is_can_be_shifted(chamber, "<") is False

    chamber = [
        "#######",
    ]
    assert is_can_be_shifted(chamber, "<") is False

    chamber = [
        "@@@@@@@",
    ]
    assert is_can_be_shifted(chamber, "<") is False

    chamber = [
        ".....@#",
    ]
    assert is_can_be_shifted(chamber, ">") is False

    chamber = [
        "#@.....",
    ]
    assert is_can_be_shifted(chamber, "<") is False

    chamber = [
        "#@.....",
    ]
    assert is_can_be_shifted(chamber, ">") is True

    chamber = [
        "....#..",
        "..@@#..",
        "..@@#..",
        "....#..",
    ]
    assert is_can_be_shifted(chamber, ">") is False

    chamber = [
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert get_shifted_chamber(chamber, ">") == [
        ".......",
        ".......",
        "...@@@.",
        ".....@.",
        ".....@.",
    ]

    chamber = [
        "...#...",
        ".......",
        "##@@@..",
        "....@..",
        "....@..",
    ]
    assert get_shifted_chamber(chamber, ">") == [
        "...#...",
        ".......",
        "##.@@@.",
        ".....@.",
        ".....@.",
    ]

    chamber = [
        "....@..",
    ]
    assert get_shifted_chamber(chamber, "<") == [
        "...@...",
    ]

    chamber = [
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert get_shifted_chamber(chamber, "<") == [
        ".......",
        ".......",
        ".@@@...",
        "...@...",
        "...@...",
    ]

    chamber = [
        "...#...",
        "#######",
        "..@@@.#",
        "....@.#",
        "....@.#",
    ]
    assert get_shifted_chamber(chamber, "<") == [
        "...#...",
        "#######",
        ".@@@..#",
        "...@..#",
        "...@..#",
    ]

    chamber = [
        "....@@@",
    ]
    assert get_shifted_chamber(chamber, "<") == [
        "...@@@.",
    ]

    chamber = [
        "@@@....",
    ]
    assert get_shifted_chamber(chamber, ">") == [
        ".@@@...",
    ]

    chamber = [
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert is_can_be_moved_down(chamber) is True

    chamber = [
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert is_can_be_moved_down(chamber) is False

    chamber = [
        ".......",
        "...#...",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert is_can_be_moved_down(chamber) is False

    chamber = [
        "...@...",
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert is_can_be_moved_down(chamber) is False

    chamber = [
        ".......",
        "......#",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert is_can_be_moved_down(chamber) is True

    chamber = [
        "....#..",
        "..@@#..",
        "..@@#..",
        "....#..",
    ]
    assert is_can_be_moved_down(chamber) is True

    chamber = [
        "..####.",
        "...#...",
        "..###..",
        "#####..",
        "..#.#..",
        "..#.#..",
        "....#..",
        "....##.",
        "....##.",
        ".####..",
        "..#....",
        ".###...",
        "..####.",
        "....##.",
        "..@@##.",
        "..@@#..",
        "....#..",
    ]
    assert is_can_be_moved_down(chamber) is True

    chamber = [
        "...####",
        "......#",
        "......#",
        ".....@@",
        ".....@@",
    ]
    assert is_can_be_moved_down(chamber) is False

    chamber = [
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert get_moved_down_chamber(chamber) == [
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]

    chamber = [
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "#...@..",
    ]
    assert get_moved_down_chamber(chamber) == [
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
        "#......",
    ]

    chamber = [
        ".......",
        ".......",
        ".......",
        ".......",
        "..@@@@.",
    ]
    assert get_moved_down_chamber(chamber) == [
        ".......",
        ".......",
        ".......",
        "..@@@@.",
    ]

    chamber = [
        ".......",
        ".......",
        ".......",
        ".......",
        "@@@@@@@",
    ]
    assert get_moved_down_chamber(chamber) == [
        ".......",
        ".......",
        ".......",
        "@@@@@@@",
    ]

    chamber = [
        "..####.",
        "...#...",
        "..###..",
        "#####..",
        "..#.#..",
        "..#.#..",
        "....#..",
        "....##.",
        "....##.",
        ".####..",
        "..#....",
        ".###...",
        "..####.",
        "....##.",
        "..@@##.",
        "..@@#..",
        "....#..",
    ]
    assert get_moved_down_chamber(chamber) == [
        "..####.",
        "...#...",
        "..###..",
        "#####..",
        "..#.#..",
        "..#.#..",
        "....#..",
        "....##.",
        "....##.",
        ".####..",
        "..#....",
        ".###...",
        "..####.",
        "..@@##.",
        "..@@##.",
        "....#..",
        "....#..",
    ]

    chamber = [
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    assert get_frozen_chamber(chamber) == [
        ".......",
        ".......",
        "..###..",
        "....#..",
        "....#..",
    ]

    chamber = [
        ".......",
        ".......",
        ".......",
        "..@@@@.",
    ]
    assert get_frozen_chamber(chamber) == [
        ".......",
        ".......",
        ".......",
        "..####.",
    ]

    chamber = [
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "#...@..",
    ]
    assert get_frozen_chamber(chamber) == [
        ".......",
        ".......",
        "..###..",
        "....#..",
        "#...#..",
    ]

    chamber = [
        ".......",
        "@@@@@@@",
    ]
    assert get_frozen_chamber(chamber) == [
        ".......",
        "#######",
    ]

    chamber = [
        "..####.",
        "...#...",
        "..###..",
        "#####..",
        "..#.#..",
        "..#.#..",
        "....#..",
        "....##.",
        "....##.",
        ".####..",
        "..#....",
        ".###...",
        "######.",
        "##..##.",
        "....##.",
        "....#..",
        "....#..",
    ]
    jets = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    assert get_chamber_after_moves(jets, 10) == chamber

    main()
