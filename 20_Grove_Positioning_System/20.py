from collections import deque

INPUT = "test_input"


def read_input():
    with open(INPUT, "r") as file:
        data = [int(x) for x in file.read().strip().splitlines()]
    return data


def main():
    data = read_input()
    print(data)
    queue = deque(enumerate(data))
    print(queue)
    print()

    for x in enumerate(data):
        index = queue.index(x)
        queue.rotate(-index)
        print(x)
        print(queue)
        if x[1] == 0:
            continue
        if x[1] > 0:
            queue.popleft()
            queue.rotate(-x[1])
            queue.appendleft(x)
        if x[1] < 0:
            queue.popleft()
            queue.rotate(-x[1])
            queue.append(x)
        print(queue)
        print()

    print(queue)


if __name__ == "__main__":
    main()
