from typing import Dict, List

INPUT = "input"
MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def get_games():
    def _get_rounds(string: str) -> List:
        str_rounds = string.split(":")[-1].split(";")
        rounds = []
        for round_str in str_rounds:
            round_dict = {}
            cubes = round_str.strip().split(",")
            for cube in cubes:
                c = cube.strip().split()
                round_dict[c[1]] = int(c[0])
            rounds.append(round_dict)
        return rounds

    with open(INPUT, "r") as file:
        data = file.readlines()
    games = list(map(_get_rounds, data))
    return games


def is_game_possible(game: List[Dict]) -> bool:
    is_possible_game = True
    for cubes_dict in game:
        for key, value in cubes_dict.items():
            if key == "red" and value > MAX_RED_CUBES:
                is_possible_game = False
                break
            elif key == "green" and value > MAX_GREEN_CUBES:
                is_possible_game = False
                break
            elif key == "blue" and value > MAX_BLUE_CUBES:
                is_possible_game = False
                break
        if not is_possible_game:
            break
    return is_possible_game


def get_fewest_cubes_number(game):
    red, blue, green = 0, 0, 0
    for cubes_dict in game:
        for key, value in cubes_dict.items():
            if key == "red" and value > red:
                red = value
            elif key == "blue" and value > blue:
                blue = value
            elif key == "green" and value > green:
                green = value
    return red * blue * green


def get_answer_1(games):
    return sum(
        [index + 1 for index, game in enumerate(games) if is_game_possible(game)]
    )


def get_answer_2(games):
    return sum([get_fewest_cubes_number(game) for game in games])


def main():
    games = get_games()
    print(get_answer_1(games))
    print(get_answer_2(games))


if __name__ == "__main__":
    game = [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    assert is_game_possible(game) is True

    game = [
        {"green": 8, "blue": 6, "red": 20},
        {"blue": 5, "red": 4, "green": 13},
        {"green": 5, "red": 1},
    ]
    assert is_game_possible(game) is False

    game = [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    assert get_fewest_cubes_number(game) == 48

    game = [
        {"green": 8, "blue": 6, "red": 20},
        {"blue": 5, "red": 4, "green": 13},
        {"green": 5, "red": 1},
    ]
    assert get_fewest_cubes_number(game) == 1560

    main()
