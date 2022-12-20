from collections import deque

INPUT = "input"


def read_input():
    with open(INPUT, "r") as file:
        data = [int(x) for x in file.read().strip().splitlines()]
    return data


def get_answer_1(data):
    queue = deque(enumerate(data))

    for x in enumerate(data):
        if x[1] == 0:
            continue
        index = queue.index(x)
        queue.rotate(-index)
        queue.popleft()
        queue.rotate(-x[1])
        if x[1] > 0:
            queue.appendleft(x)
        elif x[1] < 0:
            queue.append(x)
        else:
            print("error!")

    null = tuple(filter(lambda x: x[1] == 0, enumerate(data)))[0]
    index = queue.index(null)
    queue.rotate(-index)

    sum = 0
    for _ in range(3):
        queue.rotate(-1_000)
        sum += queue[0][1]

    return sum


def main():
    data = read_input()
    print(get_answer_1(data))


if __name__ == "__main__":
    main()
