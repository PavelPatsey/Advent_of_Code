from functools import reduce

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


def get_score(trees, x, y):
    X = len(trees[0])
    Y = len(trees)
    counter_stack = []

    i = y
    counter = 0
    tree_is_found = False
    while i > 0 and not tree_is_found:
        if trees[i - 1][x] >= trees[y][x]:
            tree_is_found = True
        counter += 1
        i -= 1
    counter_stack.append(counter)

    i = y
    counter = 0
    tree_is_found = False
    while i < Y - 1 and not tree_is_found:
        if trees[i + 1][x] >= trees[y][x]:
            tree_is_found = True
        counter += 1
        i += 1
    counter_stack.append(counter)

    j = x
    counter = 0
    tree_is_found = False
    while j > 0 and not tree_is_found:
        if trees[y][j - 1] >= trees[y][x]:
            tree_is_found = True
        counter += 1
        j -= 1
    counter_stack.append(counter)

    j = x
    counter = 0
    tree_is_found = False
    while j < X - 1 and not tree_is_found:
        if trees[y][j + 1] >= trees[y][x]:
            tree_is_found = True
        counter += 1
        j += 1
    counter_stack.append(counter)

    return reduce(lambda acc, x: acc * x, counter_stack, 1)


def read_input():
    with open(INPUT, "r") as file:
        trees = [[int(y) for y in line] for line in file.read().strip().splitlines()]
    return trees


def main():
    trees = read_input()

    X = len(trees[0])
    Y = len(trees)

    visible_trees = [[is_visible(trees, x, y) for y in range(Y)] for x in range(X)]
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

    trees_score = [[get_score(trees, x, y) for y in range(Y)] for x in range(X)]
    print(max([trees_score[x][y] for y in range(Y) for x in range(X)]))


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

    assert get_score(trees, 2, 1) == 4
    assert get_score(trees, 2, 3) == 8
    assert get_score(trees, 0, 0) == 0

    main()
