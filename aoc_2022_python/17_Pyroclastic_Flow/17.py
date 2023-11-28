INPUT = "test_input"
MOVES_NUMBER = 1
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
        while string_index < len(string) - 2 and can_be_shifted:
            if (string[string_index], string[string_index + 1]) == comparison_tuple:
                can_be_shifted = False
            string_index += 1
        chamber_index -= 1
        keep_looking = "@" in chamber[chamber_index]
    return can_be_shifted


def get_shifted_chamber(old_chamber, jet):
    chamber_index = old_chamber.copy()
    chamber_index = len(chamber) - 1
    keep_looking = "@" in chamber[chamber_index]

    if jet == ">":
        while chamber_index >= 0 and keep_looking:
            string = chamber[chamber_index]
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
            new_string = string[0] + new_string

            chamber[chamber_index] = new_string
            chamber_index -= 1
            keep_looking = "@" in chamber[chamber_index]
    else:
        while chamber_index >= 0 and keep_looking:
            string = chamber[chamber_index]
            len_string = len(string)
            string_index = 0
            new_string = ""
            while string_index <= len_string - 2:
                if string[string_index + 1] == "@":
                    new_string = new_string + "@"
                else:
                    if string[string_index] == "@":
                        new_string = new_string + "."
                    else:
                        new_string = new_string + string[string_index]
                string_index += 1
            new_string = new_string + string[len_string - 1]

            chamber[chamber_index] = new_string
            chamber_index -= 1
            keep_looking = "@" in chamber[chamber_index]

    return chamber


def get_answer_1(jets):
    len_rocks = len(ROCKS)
    rock_index = 0
    len_jets = len(jets)
    jet_index = 0
    chamber = []
    n = 0
    while n < MOVES_NUMBER:
        rock_index = rock_index % len_rocks
        chamber += ["......."] * 4
        for rock_part in ROCKS[rock_index]:
            chamber.append(rock_part)

        # проверка, что можно сдвинуть
        jet_index = jet_index % len_jets
        jet = jets[jet_index]
        can_be_shifted = is_can_be_shifted(chamber, jet)

        # jet_index += 1

        # падаем
        # мб удаляем "......." такую последнюю строчку
        rock_index += 1
        n += 1
    return chamber


def main():
    jets = get_jets()

    answer_1 = get_answer_1(jets)
    for i in reversed(answer_1):
        print(i)


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
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    shifted_chamber = get_shifted_chamber(chamber, ">")
    assert shifted_chamber == [
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
    shifted_chamber = get_shifted_chamber(chamber, ">")
    assert shifted_chamber == [
        "...#...",
        ".......",
        "##.@@@.",
        ".....@.",
        ".....@.",
    ]

    chamber = [
        "....@..",
    ]
    shifted_chamber = get_shifted_chamber(chamber, "<")
    assert shifted_chamber == [
        "...@...",
    ]

    chamber = [
        ".......",
        ".......",
        "..@@@..",
        "....@..",
        "....@..",
    ]
    shifted_chamber = get_shifted_chamber(chamber, "<")
    assert shifted_chamber == [
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
    shifted_chamber = get_shifted_chamber(chamber, "<")
    assert shifted_chamber == [
        "...#...",
        "#######",
        ".@@@..#",
        "...@..#",
        "...@..#",
    ]

    main()
