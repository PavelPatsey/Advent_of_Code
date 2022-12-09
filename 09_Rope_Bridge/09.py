INPUT = "input"

DX = {"U": 0, "D": 0, "L": -1, "R": 1}
DY = {"U": 1, "D": -1, "L": 0, "R": 0}


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def follow_head(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if abs(dx) <= 1 and abs(dy) <= 1:
        pass
    else:
        tail = (tail[0] + sign(dx), tail[1] + sign(dy))

    return tail[0], tail[1]


def read_input():
    with open(INPUT, "r") as file:
        commands = [x.split() for x in file.read().strip().splitlines()]
        commands = [[x[0], int(x[1])] for x in commands]
    return commands


def main():
    head = (0, 0)
    tail = (0, 0)
    tail_stack = set()
    tail_stack.add(tail)

    commands = read_input()
    for command in commands:
        direction, step_count = command[0], command[1]
        for _ in range(step_count):
            head = (head[0] + DX[direction], head[1] + DY[direction])
            tail = follow_head(head, tail)
            tail_stack.add(tail)

    print(len(tail_stack))


if __name__ == "__main__":
    assert follow_head((0, 0), (0, 0)) == (0, 0)
    assert follow_head((1, 0), (0, 0)) == (0, 0)
    assert follow_head((2, 0), (0, 0)) == (1, 0)
    assert follow_head((2, 1), (0, 0)) == (1, 1)
    assert follow_head((2, 4), (4, 3)) == (3, 4)
    main()
