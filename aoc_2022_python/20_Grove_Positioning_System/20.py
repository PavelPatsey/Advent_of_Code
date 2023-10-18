from collections import deque

INPUT = "input"


def read_input():
    with open(INPUT, "r") as file:
        data = [int(x) for x in file.read().strip().splitlines()]
    return data


def mix_queue(data, queue):

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


def get_grove_coordinates(data, queue):
    null = tuple(filter(lambda x: x[1] == 0, enumerate(data)))[0]
    index = queue.index(null)
    N = len(data)
    return (
        queue[(index + 1_000) % N][1],
        queue[(index + 2_000) % N][1],
        queue[(index + 3_000) % N][1],
    )


def main():
    data = read_input()

    queue = deque(enumerate(data))
    mix_queue(data, queue)
    print(sum(get_grove_coordinates(data, queue)))

    new_data = [x * 811589153 for x in data]
    queue = deque(enumerate(new_data))
    for _ in range(10):
        mix_queue(new_data, queue)
    print(sum(get_grove_coordinates(new_data, queue)))


if __name__ == "__main__":
    main()
