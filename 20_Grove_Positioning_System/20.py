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


def get_coordinates_sum(data, queue):
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

    queue = deque(enumerate(data))
    mix_queue(data, queue)
    print(get_coordinates_sum(data, queue))

    new_data = [x * 811589153 for x in data]
    queue = deque(enumerate(new_data))
    for _ in range(10):
        mix_queue(new_data, queue)
    print(get_coordinates_sum(new_data, queue))


if __name__ == "__main__":
    main()
