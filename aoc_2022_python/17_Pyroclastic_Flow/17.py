INPUT = "test_input"
MOVES_NUMBER = 1
ROCKS = [
    [
        "..####.",
    ],
    [
        "...#...",
        "..###..",
        "...#...",
    ],
    [
        "..###..",
        "....#..",
        "....#..",
    ],
    [
        "..#....",
        "..#....",
        "..#....",
        "..#....",
    ],
    [
        "..##...",
        "..##...",
    ],
]


def get_jets():
    with open(INPUT) as file:
        jets = file.read().strip()
    return jets


def get_shifted_part(part, jet):
    if jet == ">":
        condition = any(map(lambda x: x[-1] == "#", part))
        n = -1
    else:
        condition = any(map(lambda x: x[0] == "#", part))
        n = 1

    if condition:
        return part

    for i in range(len(part)):
        part[i] = part[i][n:] + part[i][:n]
    return part


def get_answer_1(jets):
    len_rocks = len(ROCKS)
    rock_index = 0
    len_jets = len(jets)
    jet_index = 0
    chamber = []
    n = 0
    while n < MOVES_NUMBER:
        rock_index = rock_index % len_rocks
        chamber_part = [".......", ".......", "......."]
        for rock_part in reversed(ROCKS[rock_index]):
            chamber_part.append(rock_part)

        for _ in range(3):
            jet_index = jet_index % len_jets
            jet = jets[jet_index]
            chamber_part = get_shifted_part(chamber_part, jet)
            del chamber_part[0]
            jet_index += 1

        chamber += chamber_part
        rock_index += 1
        n += 1
    return chamber


def main():
    jets = get_jets()

    answer_1 = get_answer_1(jets)
    for i in reversed(answer_1):
        print(i)


if __name__ == "__main__":
    part = [
        "..###..",
        "....#..",
        "....#..",
        ".......",
        ".......",
    ]
    assert get_shifted_part(part, ">") == [
        "...###.",
        ".....#.",
        ".....#.",
        ".......",
        ".......",
    ]

    part = [
        "....###",
        "......#",
        "......#",
        ".......",
        ".......",
    ]
    assert get_shifted_part(part, ">") == [
        "....###",
        "......#",
        "......#",
        ".......",
        ".......",
    ]

    part = [
        "...#...",
        "..###..",
        "...#...",
        ".......",
        ".......",
    ]
    assert get_shifted_part(part, "<") == [
        "..#....",
        ".###...",
        "..#....",
        ".......",
        ".......",
    ]

    part = [
        ".#.....",
        "###....",
        ".#.....",
        ".......",
        ".......",
    ]
    assert get_shifted_part(part, "<") == [
        ".#.....",
        "###....",
        ".#.....",
        ".......",
        ".......",
    ]

    main()
