from typing import List, Dict

INPUT = "input"
MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def get_games():
    def _get_rounds(string: str) -> List:
        str_rounds = string.split(":")[-1].split(";")
        rounds = []
        for cubes_set in str_rounds:
            round_dict = {}
            cubes = cubes_set.strip().split(",")
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
    for cubes_set in game:
        for key, value in cubes_set.items():
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


def get_answer_1(games):
    indexes = []
    for index, game in enumerate(games):
        if is_game_possible(game):
            indexes.append(index)

    return sum(map(lambda x: x + 1, indexes))


def main():
    games = get_games()
    print(get_answer_1(games))


if __name__ == "__main__":
    # game = [{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}]
    # assert is_game_possible(game) is True
    #
    # game = [
    #     {"green": 8, "blue": 6, "red": 20},
    #     {"blue": 5, "red": 4, "green": 13},
    #     {"green": 5, "red": 1},
    # ]
    # assert is_game_possible(game) is False

    main()
