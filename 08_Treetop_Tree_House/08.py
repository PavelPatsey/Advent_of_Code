import numpy as np

INPUT = "input"


def is_visible(trees, x, y):
    X = len(trees[0])
    Y = len(trees)

    if x == 0 or y == 0 or x == X - 1 or y == Y - 1:
        return True

    if all(map(lambda t: t < trees[y][x], trees[y][:x])):
        return True

    if all(map(lambda t: t < trees[y][x], trees[y][x + 1 :])):
        return True

    lst = []
    for j in range(y):
        lst.append(trees[j][x])
    if all(map(lambda t: t < trees[y][x], lst)):
        return True

    lst = []
    for j in range(y + 1, Y):
        lst.append(trees[j][x])
    if all(map(lambda t: t < trees[y][x], lst)):
        return True

    return False


def get_visible_trees(trees):
    X = len(trees[0])
    Y = len(trees)
    visible_trees = [[False for y in range(Y)] for x in range(X)]

    for y in range(Y):
        for x in range(X):
            visible_trees[y][x] = is_visible(trees, x, y)

    return visible_trees


def read_input():
    with open(INPUT, "r") as file:
        trees = [[int(y) for y in line] for line in file.read().strip().splitlines()]
    return trees


def main():
    trees = read_input()
    visible_trees = get_visible_trees(trees)

    X = len(visible_trees[0])
    Y = len(visible_trees)
    print(
        len(
            [
                visible_trees[x][y]
                for y in range(Y)
                for x in range(X)
                if visible_trees[x][y]
            ]
        )
    )


if __name__ == "__main__":
    trees = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]
    assert is_visible(trees, 0, 0) == True
    assert is_visible(trees, 1, 1) == True
    assert is_visible(trees, 1, 3) == False

    main()
