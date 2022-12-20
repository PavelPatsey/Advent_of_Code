from collections import deque

INPUT = "input"


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

    null = tuple(filter(lambda x: x[1] == 0, enumerate(data)))[0]
    # null = [x for x in enumerate(data) if x[1] == 0 ]
    print(null)
    index = queue.index(null)
    queue.rotate(-index)
    print(queue)

    sum = 0
    for _ in range(3):
        queue.rotate(-1_000)
        sum += queue[0][1]
    print(sum)


if __name__ == "__main__":
    main()
